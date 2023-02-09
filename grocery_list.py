def main():
    grocery_list()

def grocery_list():
    gl = {}
    while True:
        try:
            item = input("")
        except EOFError:
            for item in sorted(gl):
                print (f"{gl[item]} {item.upper()}")
            break
        if item in gl:
            gl[item] += 1
        else:
            gl[item] = 1


if __name__ == '__main__':            
    main()