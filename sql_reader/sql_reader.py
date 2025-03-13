
import sys
import sqlite3
import os
from prettytable import PrettyTable

if len(sys.argv) > 1:
    connection = sqlite3.connect(sys.argv[1])
else:
    connection = sqlite3.connect(input('Enter the path to the database: '))

cursor = connection.cursor()
tables = [i[0] for i in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]



digit = None


def input_keyboard():
    return int(input('>>>'))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

menu_dict = {'0': 'Exit', '1': 'Execute sql query', '2': 'Settings'}
for i in range(len(tables)):
    menu_dict[str(i+3)] = tables[i]
    

ADD = 10
MAX_STR_LEN = 48
def setting():
    global ADD, MAX_STR_LEN
    setting = {'1': f'Change the number of displayed rows (current {ADD})', '2': f'Change maximum cell length (current {MAX_STR_LEN})'}
    clear()
    print('Settings')
    print('0. Menu')
    for key, value in setting.items():
        print(f'{key}. {value}')

    choice = input_keyboard()

    if choice == 0:
        return
    elif choice == 1:
        add = int(input(f'Enter the number of displayed rows: '))
        ADD = add
        return
    elif choice == 2:
        max_str_len = int(input(f'Enter maximum cell length: '))
        MAX_STR_LEN = max_str_len
        return



def start_menu():
    clear()
    print("""
███ ████  █      ████ ███ ████ ████  ███ ████
█   █  █  █      █  █ █   █  █ █  ██ █   █  █
███ █ ██  █      ████ ███ ████ █  ██ ███ ████
  █ █  █  █      █ █  █   █  █ █  ██ █   █ █ 
███ █████ ███    █ █  ███ █  █ ████  ███ █ █ 
""")
    

    for key, value in sorted(menu_dict.items()):
        print(f'{key}. {value}')
        
    if len(menu_dict) > 10:
        return int(input())
    else:
        return input_keyboard()
    

def sql_query():
    
    clear()
    print('Enter for exit. cls - clear consloe')
    while True:
        input_query = input('Enter SQL Query: ')
        if input_query.strip() in ['exit', '0', '']:
            return
        if input_query in ['cls', 'clear']:
            clear()
            print('0 or Enter for exit. cls - clear consloe')
            continue
        try:
            print(cursor.execute(input_query).fetchall())
            connection.commit()
        except Exception as e:
            print(e)
        print()


def table_infotmation(table_name):
    clear()
    print(f'Table size: {len(cursor.execute(f"SELECT * FROM {table_name}").fetchall())}')
    schema = cursor.execute(f'PRAGMA table_info("{table_name}")').fetchall()

    print('Schema: ')
    print(f'  {table_name} (')
    for _, field_name, field_type, not_null, default_value, is_primary in schema:
        sql_field = f"{field_name} {field_type}"

        if not_null == 1:
            sql_field += " NOT NULL"
        
        if default_value is not None:
            sql_field += f" DEFAULT '{default_value}'"
        
        if is_primary:
            sql_field += " PRIMARY KEY"

        print(f'    {sql_field},')
    print('  )\n')
    print('Enter to exit')
    input()


def table_sortby(table):
    clear()
    objects = [None] + table.field_names
    print('Sort by: ')
    for i in range(len(objects)):
        print(f'{i}. {objects[i]}')

    if len(objects) > 9:
        choice = int(input())
    else:
        choice = input_keyboard()

    if choice >= len(objects)-1:
        return None

    return objects[choice]


def table(table_name: str):
    global ADD
    global MAX_STR_LEN
    start = 0
    
    table = PrettyTable()
    colums_name = [i[1] for i in cursor.execute(f'PRAGMA table_info("{table_name}")').fetchall()]
    table.field_names = colums_name 

    values = cursor.execute(f'SELECT * FROM {table_name}').fetchall()
    for row in values:
            processed_row = []
            for cell in row:
                if isinstance(cell, str):
                    cell = cell.replace('\n', ' ')
                    if len(cell) > MAX_STR_LEN:
                        cell = cell[:MAX_STR_LEN] + '...'
                processed_row.append(cell)
            table.add_row(processed_row)

    sortby = None
    while True:
        
        clear()
        print(table.get_string(start=start, end=start+ADD, sortby=sortby))
        sortby_str = '' if sortby is None else f'(sort by {sortby})'
        print(f'0. Menu\n1. <<<\n2. >>>\n3. Execute sql query\n4. Sort by {sortby_str}\n5. Settings\n6. Table information')
        choice = input_keyboard()
        
        if choice == 0:
            return

        elif choice == 1:
            start -= ADD
            if start < 0:
                start = 0
        elif choice == 2:
            if not start + ADD > len(cursor.execute(f'SELECT * FROM {table_name}').fetchall()) - 1:
                start += ADD

        elif choice == 3:
            sql_query()

        elif choice == 4:
            sortby = table_sortby(table)
            start = 0

        elif choice == 5:
            setting()

        elif choice == 6:
            table_infotmation(table_name)

while True:
    
    choice = start_menu()

    if choice == 0:
        break
    
    if choice == 1:
        sql_query()
    
    elif choice == 2:
        setting()
    
    else:
        table(tables[choice-3])
    
