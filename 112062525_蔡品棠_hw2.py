#!/usr/bin/python3
# print('How much money do you have?', end = ' ')
init_money = int(input('How much money do you have? '))
record = []

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
        print(f"{'Description' : <15s}{'Amount' : <8s}{'idx' : <4s}")
        print("=" * 30)
        for i, rec in enumerate(record):
            print(f"{rec[0] : <15s}{rec[1] : <8s}{i + 1}")
            total_money += int(record[i][1])
        print("=" * 30)
        print(f"Now you have {total_money} dollars.")
    elif cmd == "delete":
        idx = int(input("Which record do you want to delete? "))
        record.pop(idx - 1)
    elif cmd == "exit":
        break



# print("Here's your expense and income records:")
# for rec in record:
#     print(' '.join(rec))
#     total_money.append(int(rec[1]))

# print(f'Now you have {sum(total_money)} dollars.')

