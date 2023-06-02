from random import randint

def random_number_generator():
    random_numbers = []
    
    while True:
        try:
            start, end = input('Please select range of numbers: ').split()
            start, end = int(start), int(end)
            amount = int(input('Now select the amount of numbers: '))
            break
        except(ValueError, TypeError):
             print("You must select a valid number")
             
    for _ in range(amount):
        number = randint(start, end)
        random_numbers.append(number)
    for index, number in enumerate(random_numbers):
        print(f'{(index + 1)} --> {number}')

    # return random_numbers