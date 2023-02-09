def main():
    my_order()

def my_order():
    total = 0
    
    taqueria = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            print("")
            break
        if item in taqueria:
            total += taqueria[item]
            print(f"Total: ${total:.2f}")

if __name__ == '__main__':
    main()
