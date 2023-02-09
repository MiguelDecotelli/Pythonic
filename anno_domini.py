def main():
    print(anno_domini())

def anno_domini():

    months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]



    while True:
        try:
            date = input("Date: ")
            if "," in date:
                date = date.replace(",", "")
                m, d, y = date.split(" ")
                m = m.capitalize()
                if m in months and int(d) <= 31:
                    return (f"{int(y):04}-{int(months.index(m) + 1):02}-{int(d):02}")
            else:
                m, d, y = date.split("/")
                if int(m) <= 12 and int(d) < 31:
                    return (f"{int(y):04}-{int(m):02}-{int(d):02}")
        except ValueError:
            pass

if __name__ == '__main__':
    main()
