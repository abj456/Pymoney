#!/usr/bin/python3
print('How much money do you have?', end = ' ')
total_money = int(input())

print('Add an expense or income record with description and amount:')
record = input().split()
amount = int(record[1])

total_money += amount
print(f'Now you have {total_money} dollars.')
