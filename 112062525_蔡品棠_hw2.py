#!/usr/bin/python3
import sys

init_money = 0
record = []

try:
    fh_rec = open('./records.txt', 'r')
    contents = fh_rec.readlines()
    init_money = int(contents[0])

    for i in range(1, len(contents)):
        record.append(contents[i].split())

    fh_rec.close()

    print('Welcome back!')

except FileNotFoundError:
    try:
        init_money = int(input('How much money do you have? '))
    except ValueError:
        sys.stderr.write('Invalid value for money. Set to 0 by default')


with open('./records.txt', 'w+') as fh_rec:
    while True:
        cmd = input("\nWhat do you want to do (add / view / delete / exit)? ")
        if cmd == "add":
            print('''Add an expense or income record with description and amount:
desc1 amt1, desc2 amt2, desc3 amt3, ...''')
            for rec in input().split(','):
                record.append(rec.split())
        elif cmd == "view":
            total_money = init_money
            print("Here's your expense and income records:")
            description = 'Description'
            amount = 'Amount'
            print(f"{'Description':<15s}{'Amount':<8s}{'idx':<4s}")
            print("=" * 30)
            for i, rec in enumerate(record):
                print(f"{rec[0]:<15s}{rec[1]:<8s}{(i + 1):<4d}")
                total_money += int(record[i][1])
            print("=" * 30)
            print(f"Now you have {total_money} dollars.")
        elif cmd == "delete":
            idx = int(input("Which record do you want to delete? "))
            record.pop(idx - 1)
        elif cmd == "exit":
            # print(record)
            fh_rec.writelines(str(init_money) + '\n')
            for line in record:
                fh_rec.writelines(' '.join(line) + '\n')
            break
        else:
            sys.stderr.write('Invalid command. Try again.')


