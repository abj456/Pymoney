#!/usr/bin/python3
import sys

def init_pymoney():
    '''When facing exceptions that need to reset initial_moeny, 
        call this function to do so'''
    try:
        init_m = int(input('How much money do you have? '))
    except ValueError:
        sys.stderr.write('Invalid value for money. Set to 0 by default\n')
    return init_m 

def initialize():
    '''Called when this program started.\n
    If there is a records.txt file, read that file and recover all stored data.\n
    If not, set initial_money and records[] to default value.\n
    '''
    init_money = 0
    record = []
    try:
        fh_rec_r = open('./records.txt', 'r')
        contents = fh_rec_r.readlines()
        init_money = int(contents[0])

        for i in range(1, len(contents)):
            r = contents[i].split()
            int(r[1])
            record.append(r)
    except FileNotFoundError:
        init_money = init_pymoney()
    except :
        sys.stderr.write('Invalid format in records.txt. Deleting the contents.\n')
        init_money = init_pymoney()
        record.clear()
    else:
        print('Welcome back!')
    finally:
        fh_rec_r.close()
        return (init_money, record)

def add(records: list = []):
    '''
    add func: used to add user-defined record and store it into records list
    '''
    
    print('''Add an expense or income record with description and amount:
desc1 amt1, desc2 amt2, desc3 amt3, ...''')
    for rec in input().split(','):
        r = rec.split()
        try:
            int(r[1])
        except IndexError:
            sys.stderr.write(f'Wrong record: {r}\n')
            sys.stderr.write('The format of a record should be like this: breakfast -50.\n')
            sys.stderr.write('Fail to add a record.\n')
        except ValueError:
            sys.stderr.write(f'Wrong record: {r}\n')
            sys.stderr.write('Invalid value for money.\n')
            sys.stderr.write('Fail to add a record.\n')
        else:
            records.append(r)
    return records

def view(initial_money: int, records: list):
    total_money = initial_money
    print("Here's your expense and income records:")
    print(f"{'Description':<15s}{'Amount':<8s}{'idx':<4s}")
    print("=" * 30)
    for i, rec in enumerate(records):
        print(f"{rec[0]:<15s}{rec[1]:<8s}{(i + 1):<4d}")
        total_money += int(records[i][1])
    print("=" * 30)
    print(f"Now you have {total_money} dollars.")
    return None

def delete(records: list):
    try:
        idx = int(input("Which record do you want to delete? "))
        records.pop(idx - 1)
    except ValueError:
        sys.stderr.write('Invalid format. Fail to delete a record.\n')
    except IndexError:
        sys.stderr.write(f"There's no record with {idx}. Fail to delete a record.\n")
    return records

def save(initial_money: int, records: list):
    fh_rec = open('./records.txt', 'w')
    fh_rec.writelines(str(initial_money) + '\n')
    for line in records:
        fh_rec.writelines(' '.join(line) + '\n')
    return None

initial_money, records = initialize()

while True:
    cmd = input("\nWhat do you want to do (add / view / delete / exit)? ")
    if cmd == "add":
        records = add(records)
    elif cmd == "view":
        view(initial_money, records)
    elif cmd == "delete":
        records = delete(records)
    elif cmd == "exit":
        # print(record)
        save(initial_money, records)
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')
