import os
# from cs50 import SQL
from flask import flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_user, login_required, logout_user
from finance.forms import LoginForm, RegistrationForm, QuoteForm, BuyForm, SellForm
from finance.models import User, Portfolio, Transactions
from finance.my_functions import apology, lookup, usd
from finance import app, db
from werkzeug.security import check_password_hash, generate_password_hash

# Ensuring templates are auto-reloaded.
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Customizing filter.
app.jinja_env.filters["usd"] = usd

# Making sure API key is set.
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# @app.after_request
# def after_request(response):
#     """Ensure responses aren't cached"""
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    form = RegistrationForm()

    if form.validate_on_submit():

        user = User(username=form.username.data,
                    password=form.password.data,
                    )
        try:             
            db.session.add(user)
            db.session.commit()
        except Exception:
            return apology('Username is already taken!')        

        flash("Registered!")
        return redirect(url_for("login"))

    return render_template("/register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            return apology("Invalid username or password", 403)
        
        login_user(user)
        flash('Welcome!')
        
        return redirect(url_for("index"))
    
    return render_template("/login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    
    logout_user()
    flash('See you soon!')
    return redirect(url_for('index'))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    form = QuoteForm()

    if form.validate_on_submit():

        # Ensure Symbol was submitted
        if not request.form.get("symbol"):
            return apology("Missing symbol", 400)

        # Call lookup to get ticker information and pass it via template
        try:
            ticker = lookup(request.form.get("symbol"))
            return render_template("quoted.html", name=ticker["name"], symbol=ticker["symbol"], price=ticker["price"])

        # Ensure it is a valid symbol
        except (KeyError, TypeError, ValueError):
            return apology("Invalid ticker symbol", 400)

    return render_template("quote.html", form=form)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    form = BuyForm

    if form.validate_on_submit():

        user_id = session["user_id"]

        # Ensure Symbol was submitted
        if not request.form.get("symbol"):
            return apology("Missing symbol", 400)

        # How much cash does the user have?
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # Requesting the number of shares and check if it is an integer
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Must be integer", 400)

        # Requesting the stock user wants to acquire by calling lookup making sure it's a valid symbol
        try:
            ticker = lookup(request.form.get("symbol"))
            current_purchase = ticker["price"] * float(shares)
        except (KeyError, TypeError, ValueError):
            return apology("Invalid ticker symbol", 400)

        # Ensure it is a positive number
        if shares <= 0:
            return apology("Must be positive number", 400)

        # Can the user afford this amount of stocks?
        if current_purchase > cash:
            return apology("Can't afford", 400)

        # Insert acquisition into tables and update cash
        else:
            my_stocks = db.execute("INSERT INTO portfolio (symbol, name, shares) VALUES (?, ?, ?)",
                                   ticker["symbol"], ticker["name"], shares)
            db.execute("INSERT INTO transactions (stock_id, time, price, total, user_id) VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?)",
                       my_stocks, ticker["price"], (ticker["price"]*shares), user_id)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - current_purchase, user_id)
            flash("Bought!")

        # Redirect to home page
        return redirect("/")

    return render_template("buy.html")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    # Query of Stocks and shares
    my_shares = db.execute(
        "SELECT symbol, name, SUM(shares) as sum_shares, price, total FROM portfolio JOIN transactions ON portfolio.id = transactions.stock_id WHERE user_id = ? GROUP BY name ORDER BY symbol", user_id)

    # Creating a temporary list
    shares_list = []

    # Setting up updated price by calling lookup
    for i in range(len(my_shares)):
        current_price = lookup(my_shares[i]["symbol"])
        current_price = current_price["price"]

        # Setting updated total based on current price
        total = current_price * int(my_shares[i]["sum_shares"])
        print(f'total: {total}')

        # Creating a dictionary for updated prices
        new_dictionary = {
            "symbol": my_shares[i]["symbol"],
            "name": my_shares[i]["name"],
            "shares": my_shares[i]["sum_shares"],
            "price": current_price,
            "total": total
        }

        # Attaching the content of new_dictionary into my list
        shares_list.append(new_dictionary)

        print(f' new dict: {new_dictionary["symbol"]}')
        bought = new_dictionary["shares"] * new_dictionary["price"]
        print(f' bought {bought}')

    # Checking avaiable cash and total cash from purchase and sell of shares
    avaiable_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    print(f' avaiable cash: {avaiable_cash}')
    shares_bought = db.execute(
        "SELECT SUM(total) FROM transactions WHERE stock_id IN (SELECT id FROM portfolio WHERE shares > 0) AND user_id = ?", user_id)[0]["SUM(total)"]
    print(f' shares bought: {shares_bought}')
    shares_sold = db.execute(
        "SELECT SUM(total) FROM transactions WHERE stock_id IN (SELECT id FROM portfolio WHERE shares < 0) AND user_id = ?", user_id)[0]["SUM(total)"]
    print(f' shares sold: {shares_sold}')

    # New users have None shares_bought
    if shares_bought == None:
        total_cash = avaiable_cash
    # Ensure user has already sold any shares
    elif shares_sold == None:
        total_cash = avaiable_cash + shares_bought
    # Add balances to get total amount of cash and render it into template with all future (current) acquired and sold shares
    else:
        total_cash = avaiable_cash + shares_bought - shares_sold

    return render_template("index.html", shares_list=shares_list, avaiable_cash=avaiable_cash, total_cash=total_cash)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]

    # How much cash the user still have
    cash = db.execute(
        "SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    # Query the stock's symbols user have acquired
    my_stocks = db.execute(
        "SELECT symbol, shares FROM portfolio WHERE id IN (SELECT stock_id FROM transactions WHERE user_id = ?) AND shares > 0 GROUP BY symbol", user_id)
    print(f' shares: {my_stocks}')

    if request.method == "POST":

        # Call lookup for valid symbols
        ticker = lookup(request.form.get("symbol"))

        # Ensure Symbol was submitted
        if not request.form.get("symbol"):
            return apology("Missing symbol", 400)

        # Requesting the number of shares and check if it is an integer
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Must be integer", 400)

        # Query the total number of shares from a particular stock the user has
        my_shares = db.execute("SELECT shares FROM portfolio WHERE symbol = ?", ticker["symbol"])[0]["shares"]

        # Ensure user has enough shares
        if shares > my_shares:
            return apology("Not enough shares", 400)

        # Ensure it is a positive number
        elif shares <= 0:
            return apology("Must be positive number", 400)

        # Update tables with new amount of shares, stocks and avaiable cash user has after sell
        else:
            my_sell = db.execute("INSERT INTO portfolio (symbol, name, shares) VALUES (?, ?, ?)",
                                 ticker["symbol"], ticker["name"], (-1 * shares))
            db.execute("INSERT INTO transactions (stock_id, time, price, total, user_id) VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?)",
                       my_sell, ticker["price"], (ticker["price"] * shares), user_id)
            current_sell = ticker["price"] * float(shares)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + current_sell, user_id)
            flash("Sold!")

        # Redirect to home page
        return redirect("/")

    return render_template("sell.html", my_stocks=my_stocks)
    # db.execute("INSERT INTO transactions (stock_id, time, price, total, user_id) VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?)", my_stocks, ticker["price"], (ticker["price"]*shares), user_id)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    # Show history of transactions user made rendering it via template
    history = db.execute(
        "SELECT symbol, shares, price, time FROM portfolio JOIN transactions ON portfolio.id = transactions.stock_id WHERE user_id = ? ORDER BY time", user_id)

    return render_template("history.html", history=history)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add more cash into user's account"""
    user_id = session["user_id"]

    # Query user's current cash avaiable
    current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    # Query for user's password
    user_password = db.execute("SELECT hash FROM users WHERE id = ?", user_id)[0]["hash"]

    if request.method == "POST":

        # Add the desired amount of cash and update balance
        add_cash = int(request.form.get("add_cash"))
        add_card = request.form.get("add_card")

        if not check_password_hash(user_password, request.form.get("password")):
            return apology("Password is incorrect!", 400)
        else:
            new_amount = current_cash + add_cash
            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_amount, user_id)

        flash("Cash Added!")

        # Redirect user to home page
        return redirect("/")

    return render_template("add_cash.html")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change username's password"""
    user_id = session["user_id"]

    # Query for user's current password
    user_password = db.execute("SELECT hash FROM users WHERE id = ?", user_id)[0]["hash"]

    if request.method == "POST":

        # Ensure password was submitted
        if not request.form.get("old_password"):
            return apology("must provide password", 400)

        # Setting information passed from user through form
        old_password = request.form.get("old_password")
        new_password = generate_password_hash(request.form.get("new_password"))
        confirmation = request.form.get("confirmation")

        # Ensure old password is correct
        if not check_password_hash(user_password, old_password):
            return apology("Password is incorrect!", 400)

        # Ensure new passwords are matching
        if request.form.get("new_password") != confirmation:
            return apology("Passwords are no match!", 400)

        # Update password inside database
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_password, user_id)

        # Flash message!
        flash("Password changed!")
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("change_password.html")





# Put site on air
if __name__ == "__main__":
    app.run(debug=True)

