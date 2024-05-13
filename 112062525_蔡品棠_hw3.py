#!/usr/bin/python3
import sys

class Record:
    '''Represent a record.'''
    def __init__(self, cat, desc, amount) -> None:
        self._category: str = cat
        self._description: str = desc
        self._amount: int = amount
    
    @property
    def amount(self):
        return self._amount
    @property
    def category(self):
        return self._category
    @property
    def description(self):
        return self._description

class Categories:
    '''Maintain the category list and provide some methods.'''
    def __init__(self):
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    
    def view(self):
        '''print out all categories in class'''
        def view_categories(categories: list, depth: int = -1):
            '''inner function in Categories.view()'''
            if categories == None:
                return
            if type(categories) == list:
                for cat in categories:
                    view_categories(cat, depth + 1)
            elif type(categories) == str:
                print(f'{" " * depth * 2}{"- " + categories}')
                return
        view_categories(self._categories)
    
    def is_category_valid(self, category_name: str):
        '''return True if category is in categories, otherwise False'''
        def check_category(category_name: str = category_name, categories = self._categories):
            '''inner function in Categories.is_category_valid()'''
            if type(categories) == list:
                for cat in categories:
                    ret = check_category(category_name, cat)
                    if ret == True:
                        return True
                return False
            return category_name == categories
        return check_category(category_name)
    
    def find_subcategories(self, category_name: str):
        '''
        takes a category name to find, 
        and returns a non-nested list containing the specified category and all the subcategories under it (if any).
        '''
        def find_subcategories_gen(category: str, categories = self._categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) and type(categories[index + 1]) == list:
                        yield from find_subcategories_gen(child, categories[index + 1], True)
            else:
                if categories == category or found == True:
                    yield categories

        return [cat for cat in find_subcategories_gen(category_name)]
    


class Records:
    '''Maintain a list of all the 'Record's and the initial amount of money.'''
    def init_pymoney(self):
        '''When facing exceptions that need to reset initial_moeny, 
            call this function to do so'''
        init_m = 0
        try:
            init_m = int(input('How much money do you have? '))
        except ValueError:
            sys.stderr.write('Invalid value for money. Set to 0 by default\n')
        return init_m 

    def __init__(self) -> None:
        '''Called when this program started.\n
        If there is a records.txt file, read that file and recover all stored data.\n
        If not, set initial_money and records[] to default value.\n
        '''
        self._init_money = 0
        self._total_money = 0
        self._records: list[Record] = []
        try:
            fh_rec_r = open('./records.txt', 'r')
            contents = fh_rec_r.readlines()
            self._init_money = int(contents[0])

            for i in range(1, len(contents)):
                r = contents[i].split()
                int(r[2])
                self._records.append(Record(r[0], r[1], int(r[2])))
        except FileNotFoundError:
            self._init_money = self.init_pymoney()
        except:
            sys.stderr.write('Invalid format in records.txt. Deleting the contents.\n')
            fh_rec_r.close()
            self._init_money = self.init_pymoney()
            self._records.clear()
        else:
            fh_rec_r.close()
            print('Welcome back!')
    
    def add(self, record: str, categories: Categories):
        '''add func: used to add user-defined record and store it into records list'''
        for rec in record.split(','):
            r = rec.split()
            try:
                int(r[2])
                assert categories.is_category_valid(r[0]) == True
            except IndexError:
                sys.stderr.write(f'Wrong record: {r}\n')
                sys.stderr.write('The format of a record should be like this: meal breakfast -50.\n')
                sys.stderr.write('Fail to add a record.\n')
            except ValueError:
                sys.stderr.write(f'Wrong record: {r}\n')
                sys.stderr.write('Invalid value for money.\n')
                sys.stderr.write('Fail to add a record.\n')
            except AssertionError:
                sys.stderr.write('The specified category is not in the category list.\n')
                sys.stderr.write('You can check the category list by command "view categories".\n')
                sys.stderr.write('Fail to add a record.\n')
            else:
                self._records.append(Record(r[0], r[1], int(r[2])))
    
    def view(self):
        '''view func: view all records input by user'''
        self._total_money = self._init_money
        print("Here's your expense and income records:")
        print(f"{'Category':<15s}{'Description':<15s}{'Amount':<8s}{'idx':<4s}")
        print("=" * 50)
        
        print(f"{' ' * 15}{'initial money':<15s}{self._init_money:<8d}")
        for i, rec in enumerate(self._records):
            print(f"{rec.category:<15s}{rec.description:<15s}{rec.amount:<8d}{(i + 1):<4d}")
            self._total_money += rec.amount
        
        print("=" * 50)
        print(f"Now you have {self._total_money} dollars.")

    def delete(self, delete_record_idx: int):
        '''delete func: delete specified record'''
        try:
            self._records.pop(delete_record_idx)
        except ValueError:
            sys.stderr.write('Invalid format. Fail to delete a record.\n')
        except IndexError:
            sys.stderr.write(f"There's no record with {delete_record_idx}. Fail to delete a record.\n")
        

    def find(self, target_categories: list):
        '''print out the filtered records and report the total amount of money of the listed records.'''
        result = list(filter(lambda rec: rec.category in target_categories, self._records))

        total_amount = 0
        print(f"{'Category':<15s}{'Description':<15s}{'Amount':<8s}")
        print("=" * 40)
    
        for rec in result:
            print(f"{rec.category:<15s}{rec.description:<15s}{rec.amount:<8d}")
            total_amount += rec.amount

        print("=" * 40)
        print(f"The total amount above is {total_amount}.")

        
    def save(self):
        '''save func: save all records in records.txt'''
        fh_rec = open('./records.txt', 'w')
        fh_rec .writelines(str(self._init_money) + '\n')
        for rec in self._records:
            line = rec.category + ' ' + rec.description + ' ' + str(rec.amount) + '\n'
            fh_rec.writelines(line)
        fh_rec.close()

categories = Categories()
records = Records()

while True:
    cmd = input("\nWhat do you want to do (add / view / delete / view categories / find / exit)? ")
    if cmd == "add":
        record = input('Add some expense or income records with category, description, and amount\
(separate by spaces):\ncat1 desc1 amt1, cat2 desc2 amt2, cat3 desc3 amt3, ...\n')
        records.add(record, categories)
    elif cmd == "view":
        records.view()
    elif cmd == "delete":
        delete_record_idx = int(input("Which record do you want to delete? "))
        records.delete(delete_record_idx - 1)
    elif cmd == 'view categories':
        categories.view()
    elif cmd == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        print(f"Here's your expense and income records under category \"{category}\":")
        records.find(target_categories)
        
    elif cmd == "exit":
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')


# Explain code
# class Record, class Records.add(), class Records.find(), and all method of class Categories

# QA section
# 1. property的功用？
# 2. generator裡面yield和yield from的差別？