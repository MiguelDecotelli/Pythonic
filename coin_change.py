
def main():
    # Declaring variable cents.
    cents = get_cents()    

    # Declaring variables inside main for all types of coins.
    # Using 4 declared functions to obtain numbers of dollars
    quarters = total_quarters(cents)

    cents = cents - quarters * 25

    dimes = total_dimes(cents)
    cents = cents - dimes * 10

    nickels = total_nickels(cents)
    cents = cents - nickels * 5

    pennies = total_pennies(cents)
    cents = cents - pennies * 1

    coins = quarters + dimes + nickels + pennies
    # Adding the total of coins after getting the maximum amount of each and then printing it.
    print(f'{coins:,.0f} coin(s)')

# Declaring function to request number of cents from input.


def get_cents():
    # Continue requesting "change owned" until cents are higher than 0.
    while True:
        cents = float(input("Change owned: "))
        if cents > 0:
            break
    # Returning and storing cents for later usage.
    return cents
# Declaring functions for all 4 types of coins using dollars as a parameter.


def total_quarters(dollars):
    # Declaring variable quarters as the amount of dollars divided by 25.
    quarters = dollars // 25
    # Returning and storing quarters for later usage.
    return quarters
# For all my functions I shall divide dollars by the correspondent coin to obtain the number of each.


def total_dimes(dollars):
    # Declaring variable dimes as the amount of dollars divided by 10.
    dimes = dollars // 10
    # Returning and storing dimes for later usage.
    return dimes


def total_nickels(dollars):
    # Declaring variable nickels as the amount of dollars divided by 5.
    nickels = dollars // 5
    # Returning and storing nickels for later usage.
    return nickels


def total_pennies(dollars):
    # Declaring variable pennies as the amount of dollars divided by 1.
    pennies = dollars // 1
    # Returning and storing pennies for later usage.
    return pennies

if __name__ == "__main__":
    main()