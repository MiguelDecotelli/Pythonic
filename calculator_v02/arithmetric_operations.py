import sys

def addition():
    try:
        x = float(input("Type 1st number: "))
        y = float(input("Type 2nd number: "))
        return f'\nAddition => {x} + {y} = {(x + y)}'
    except ValueError:
        return ('You must enter a valid number\n')


def subtraction():
    try:
        x = float(input("Type 1st number: "))
        y = float(input("Type 2nd number: "))
        return f'\nSubtraction => {x} - {y} = {(x - y)}'
    except ValueError:
        return ('You must enter a valid number\n')


def multiplication():
    try:
        x = float(input("Type 1st number: "))
        y = float(input("Type 2nd number: "))
        return f'\nMultiplication => {x} * {y} = {(x * y)}'
    except ValueError:
        return ('You must enter a valid number\n')


def division():
    try:
        x = float(input("Type 1st number: "))
        y = float(input("Type 2nd number: "))
        return f'\nDivision => {x} / {y} = {(x / y):.02}'
    except (ValueError, ZeroDivisionError):
        return ('You must enter a valid number, higher than "0"\n')
    

def selected_operation(operation):
    if operation == 'A':
        return addition()
    elif operation == 'S':
        return subtraction()
    elif operation == 'M':
        return multiplication()
    elif operation == 'D':
        return division()
    elif operation == 'E':
        sys.exit("\nSee you again!")
