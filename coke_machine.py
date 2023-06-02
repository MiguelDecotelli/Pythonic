def main():
    changes()
    # print(f"Amount Due: {changes(change_owed)}")

def changes():
    change_owed = 50
    while change_owed > 0:
        coins = int(input("Insert Coin: "))
        if coins != 25 and coins != 10 and coins != 5:
            print(f"Amount Due: {change_owed}")
            continue
        else:
            change_owed = change_owed - coins
            if change_owed > 0:
                print(f"Amount Due: {change_owed}")
            elif change_owed < 0:
                print(f"Change Owed: {change_owed * -1}")
            elif change_owed == 0:
                print(f"No change owed")

if __name__ == '__main__':            
    main()
    