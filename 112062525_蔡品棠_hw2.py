#!/usr/bin/python3
# print('How much money do you have?', end = ' ')
total_money = [int(input('How much money do you have? '))]

print('''Add an expense or income record with description and amount:
desc1 amt1, desc2 amt2, desc3 amt3, ...''')
record = [rec.split() for rec in input().split(',')]

print("Here's your expense and income records:")
for rec in record:
    print(' '.join(rec))
    total_money.append(int(rec[1]))

print(f'Now you have {sum(total_money)} dollars.')

