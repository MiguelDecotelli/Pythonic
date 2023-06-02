def convert(input, output, temperature):
    if input == 'Celsius':
        if output == 'Kelvin':
            return int(temperature) + 273.15
        elif output == 'Fahrenheit':
            return int(temperature) * (9/5) + 32
    elif input == 'Fahrenheit':
        if output == 'Kelvin':
            return (int(temperature) - 32) * (5/9) + 273.15
        elif output == 'Celsius':
            return (int(temperature) - 32) * (5/9)
    elif input == 'Kelvin':
        if output == 'Celsius':
            return int(temperature) - 273.15
        elif output == 'Fahrenheit':
            return (int(temperature) - 273.15) * (9/5) + 32
    