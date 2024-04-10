#!/usr/bin/python3
import sys

init_money = 0
record = []

def init_pymoney():
    try:
        init_m = int(input('How much money do you have? '))
    except ValueError:
        sys.stderr.write('Invalid value for money. Set to 0 by default\n')
    return init_m 

try:
    fh_rec_r = open('./records.txt', 'r')
    contents = fh_rec_r.readlines()
    init_money = int(contents[0])

    for i in range(1, len(contents)):
        record.append(contents[i].split())
except FileNotFoundError:
    init_money = init_pymoney()
except :
    sys.stderr.write('Invalid format in records.txt. Deleting the contents.\n')
    init_money = init_pymoney()    
else:
    print('Welcome back!')
finally:
    fh_rec_r.close()

with open('./records.txt', 'w+') as fh_rec:
    while True:
        cmd = input("\nWhat do you want to do (add / view / delete / exit)? ")
        if cmd == "add":
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
                    record.append(r)
        elif cmd == "view":
            total_money = init_money
            print("Here's your expense and income records:")
            print(f"{'Description':<15s}{'Amount':<8s}{'idx':<4s}")
            print("=" * 30)
            for i, rec in enumerate(record):
                print(f"{rec[0]:<15s}{rec[1]:<8s}{(i + 1):<4d}")
                total_money += int(record[i][1])
            print("=" * 30)
            print(f"Now you have {total_money} dollars.")
        elif cmd == "delete":
            try:
                idx = int(input("Which record do you want to delete? "))
                record.pop(idx - 1)
            except ValueError:
                sys.stderr.write('Invalid format. Fail to delete a record.\n')
            except IndexError:
                sys.stderr.write(f"There's no record with {idx}. Fail to delete a record.\n")
        elif cmd == "exit":
            # print(record)
            fh_rec.writelines(str(init_money) + '\n')
            for line in record:
                fh_rec.writelines(' '.join(line) + '\n')
            break
        else:
            sys.stderr.write('Invalid command. Try again.\n')


