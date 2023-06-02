
from flask import Flask, redirect, render_template, request, url_for
from temperature import convert
# Temperature Conversion: Create a program that converts temperature values between Celsius, Fahrenheit, and Kelvin.
# Implement the conversion formulas and provide a command-line interface or a graphical user interface (GUI) to interact with the program.
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def template():
    in_temp = ['Celsius', 'Fahrenheit', 'Kelvin']
    out_temp = ['Celsius', 'Fahrenheit', 'Kelvin']

    if request.method == 'POST':
        input_temperature = request.form.get('input_temperature')
        output_temperature = request.form.get('output_temperature')
        temperature_value = request.form.get('temperature_value')

        convert_value = convert(input_temperature, output_temperature, temperature_value)
        return render_template('temperature.html', in_temp=input_temperature, out_temp=output_temperature, new_value=convert_value)
    
    return render_template("/index.html", in_temp=in_temp, out_temp=out_temp)


if __name__ == '__main__':
    app.run(debug=True)


