#!/usr/bin/python3
import sys

class Record:
    '''Represent a record.'''
    def __init__(self, cat, desc, amount) -> None:
        self._category = cat
        self._description = desc
        self._amount = amount
    
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
        def flatten(L):
            '''
            return a flat list that contains all element in the nested list L\n
            for example, flatten([1,2,[3,[4],5]]) returns [1,2,3,4,5]
            '''
            if type(L) == list:
                result = []
                for child in L:
                    result.extend(flatten(child))
                return result
            else:
                return [L]
        def finding_subcat(category: str = category_name, categories = self._categories):
            if type(categories) == list:
                for v in categories:
                    p = find_subcategories(category, v)
                    if p == True:
                        index = categories.index(v)
                        if index + 1 < len(categories) and type(categories[index + 1] == list):
                            return flatten(categories[index:index + 2])
                        else:
                            return [v]
                    if p != []:
                        return p
            return True if categories == category else []
        return finding_subcat(category_name)

class Records:
    '''Maintain a list of all the 'Record's and the initial amount of money.'''
    def init_pymoney(self):
        '''When facing exceptions that need to reset initial_moeny, 
            call this function to do so'''
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
        self._records = []
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
        total_moeny = self._init_money
    def delete(self):

    def find(self):

    def save(self):


def initialize_categories():
    '''
    categories initialization
    '''
    ret_list = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    return ret_list

def view_categories(categories, depth: int = -1):
    '''
    print out all categories
    '''
    if categories == None:
        return
    
    if type(categories) == list:
        for cat in categories:
            view_categories(cat, depth + 1)
    elif type(categories) == str:
        print(f'{" " * depth * 2}{"- " + categories}')
        return

def is_category_valid(category, categories):
    '''
    return True if category is in categories, otherwise False
    '''
    if type(categories) == list:
        for cat in categories:
            ret = is_category_valid(category, cat)
            if ret == True:
                return True
        return False
    return category == categories

def find(records, categories):
    '''
    print out the filtered records and report the total amount of money of the listed records.
    '''
    category = input('Which category do you want to find? ')
    find_sub_list = find_subcategories(category, categories)
    result = list(filter(lambda rec: rec[0] in find_sub_list, records))
    # print(result)

    total_amount = 0
    print(f"Here's your expense and income records under category \"{category}\":")
    print(f"{'Category':<15s}{'Description':<15s}{'Amount':<8s}{'idx':<4s}")
    print("=" * 50)
    
    for i, rec in enumerate(result):
        print(f"{rec[0]:<15s}{rec[1]:<15s}{rec[2]:<8s}{(i + 1):<4d}")
        total_amount += int(result[i][2])
    
    print("=" * 50)
    print(f"Now you have {total_amount} dollars.")
    return None

def find_subcategories(category, categories):
    '''
    takes a category name to find, 
    and returns a non-nested list containing the specified category and all the subcategories under it (if any).
    '''
    if type(categories) == list:
        for v in categories:
            p = find_subcategories(category, v)
            if p == True:
                index = categories.index(v)
                if index + 1 < len(categories) and type(categories[index + 1] == list):
                    return flatten(categories[index:index + 2])
                else:
                    return [v]
            if p != []:
                return p
    return True if categories == category else []

def flatten(L):
    '''
    return a flat list that contains all element in the nested list L\n
    for example, flatten([1,2,[3,[4],5]]) returns [1,2,3,4,5]
    '''
    if type(L) == list:
        result = []
        for child in L:
            result.extend(flatten(child))
        return result
    else:
        return [L]

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
            int(r[2])
            record.append(r)
    except FileNotFoundError:
        init_money = init_pymoney()
    except :
        sys.stderr.write('Invalid format in records.txt. Deleting the contents.\n')
        fh_rec_r.close()
        init_money = init_pymoney()
        record.clear()
    else:
        fh_rec_r.close()
        print('Welcome back!')
    finally:
        return (init_money, record)

def add(records: list = [], categories: list = []):
    '''
    add func: used to add user-defined record and store it into records list
    '''
    
    print('''Add an expense or income record with description and amount:
cat1 desc1 amt1, cat2 desc2 amt2, cat3 desc3 amt3, ...''')
    for rec in input().split(','):
        r = rec.split()
        try:
            int(r[2])
            assert is_category_valid(r[0], categories) == True
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
            records.append(r)
                
    return records

def view(initial_money: int, records: list):
    '''
    view func: view all records input by user
    '''
    total_money = initial_money
    print("Here's your expense and income records:")
    print(f"{'Category':<15s}{'Description':<15s}{'Amount':<8s}{'idx':<4s}")
    print("=" * 50)
    
    print(f"{' ' * 15}{'initial money':<15s}{initial_money:<8d}")
    for i, rec in enumerate(records):
        print(f"{rec[0]:<15s}{rec[1]:<15s}{rec[2]:<8s}{(i + 1):<4d}")
        total_money += int(records[i][2])
    
    print("=" * 50)
    print(f"Now you have {total_money} dollars.")
    return None

def delete(records: list):
    '''
    delete func: delete specified record
    '''
    try:
        idx = int(input("Which record do you want to delete? "))
        records.pop(idx - 1)
    except ValueError:
        sys.stderr.write('Invalid format. Fail to delete a record.\n')
    except IndexError:
        sys.stderr.write(f"There's no record with {idx}. Fail to delete a record.\n")
    return records

def save(initial_money: int, records: list):
    '''
    save func: save all records in records.txt
    '''
    fh_rec = open('./records.txt', 'w')
    fh_rec.writelines(str(initial_money) + '\n')
    for line in records:
        fh_rec.writelines(' '.join(line) + '\n')
    fh_rec.close()
    return None

initial_money, records = initialize()
categories = initialize_categories()
while True:
    cmd = input("\nWhat do you want to do (add / view / delete / view categories / find / exit)? ")
    if cmd == "add":
        records = add(records, categories)
    elif cmd == "view":
        view(initial_money, records)
    elif cmd == "delete":
        records = delete(records)
    elif cmd == 'view categories':
        view_categories(categories)
    elif cmd == 'find':
        find(records, categories)
    elif cmd == "exit":
        # print(record)
        save(initial_money, records)
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')
