def main():
    fruit = input("Item: ")
    fruit = fruit.lower()
    print(get_fruit(fruit))

def get_fruit(fruit):
    fruits = [
        {"Item": "apple", "Calories": 130},
        {"Item": "avocado", "Calories": 50},
        {"Item": "banana", "Calories": 110},
        {"Item": "cantaloupe", "Calories": 50},
        {"Item": "grapefruit", "Calories": 60},
        {"Item": "grapes", "Calories": 90},
        {"Item": "honeydew melon", "Calories": 50},
        {"Item": "kiwifruit", "Calories": 90},
        {"Item": "lemon", "Calories": 15},
        {"Item": "lime", "Calories": 20},
        {"Item": "nectarine", "Calories": 60},
        {"Item": "orange", "Calories": 80},
        {"Item": "peach", "Calories": 60},
        {"Item": "pear", "Calories": 100},
        {"Item": "pineapple", "Calories": 50},
        {"Item": "plums", "Calories": 70},
        {"Item": "strawberries", "Calories": 50},
        {"Item": "sweet cherries", "Calories": 100},
        {"Item": "tangerine", "Calories": 50},
        {"Item": "watermelon", "Calories": 80},
    ]

    for i in fruits:
        if fruit in i["Item"]:
            return f"Calories: {i['Calories']}"
    return ""

if __name__ == '__main__':            
    main()