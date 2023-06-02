from menu import menu
from arithmetric_operations import selected_operation

def main():
    while True:
        operation = input(menu).capitalize()
        print(selected_operation(operation))

if __name__ == '__main__':
    main()