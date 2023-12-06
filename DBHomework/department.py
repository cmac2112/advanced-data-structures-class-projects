#department

import sqlite3

def add_dpart(conn, cur):
    dpartid = input('ID:') #get input
    dpartName = input('Department Name:')
    #insert added department
    cur.execute('''INSERT INTO Departments (DeptID, DeptName)
                VALUES (?, ?)''', ((dpartid), (dpartName)))
    conn.commit() #commit changes (main was not working to do this
    #dont know why
    print('success')

def view_dpart(conn, cur):
    #get values from database
    cur.execute('SELECT DeptID, DeptName FROM Departments')

    results = cur.fetchall()

    print() #display
    for row in results:
        print(row)
    print()
def search_dpart(conn, cur):
    name = input('Department to search:')
    name = '%' + name + '%'

    #search for value
    cur.execute('''SELECT DeptID, DeptName FROM Departments Where DeptName LIKE ?'''
                , (name,))
    conn.commit()

    results = cur.fetchall()
    print(results)
    if len(results) > 0: #display and determine if exists
        for row in results:
            print('found')
        print()
    else:
        print('Not found.\n')
def delete_dpart(cur):
    #get name to delete
    name = input('Name to Delete')

    name = '%' + name + '%'

    #search for row containing needed entry
    cur.execute('''SELECT DeptID, DeptName FROM Departments Where DeptName LIKE
                ?''',(name,))

    results = cur.fetchall()

    if len(results) > 0: #determine if exists
        print(f'{"ID":3} {"Name":20}')
        for row in results: #show existing values
            print(f'{row[0]:<3} {row[1]:20}')
        id = int(input('Enter the ID of the entry you wish to delete: '))
        if contains_id(results, id): #check if exists
            r_u_sure = input('Are you sure? (y/n): ')
            if (r_u_sure == 'y' or r_u_sure == 'Y'):
                cur.execute('DELETE FROM Departments WHERE DeptId == ?', (id,))
                conn.commit() #commit delete
                print('Entry deleted.\n')
        else:
            print('Not a valid ID.')
        print()
    else:
        print('Not found.\n')

def update_dpart(conn, cur):
    #get name to update
    name = input('Department name to update:')

    name = '%' + name + '%'

    #search for needed entry
    cur.execute('''SELECT DeptID, DeptName FROM Departments Where DeptName Like
                ?''',(name,))
    results = cur.fetchall()

    if len(results) > 0: #same as delete but updating instead
        print(f'{"DeptID":1} {"DeptName":1}')
        for row in results:
            print(f'{row[0]:<3} {row[1]:10}')
        id = int(input('Enter the ID of the entry you wish to update:'))
        if contains_id(results, id):
            new_name = input('Enter new name for the department:')
            new_id = input('Enter new Id for the department:')
            cur.execute('''UPDATE Departments SET DeptName = ?, DeptID = ?
                        Where DeptID == ?''', (new_name, new_id, id))
            conn.commit()
            print('Updated')
        else:
            print('invalid ID entered.')
        print()
    else:
        print('Not found.\n')
def end(conn):
    conn.commit()
    conn.close()
    print('done')
    quit()
    


def execute_choice(conn, choice, cur):
        if choice == 1:
            add_dpart(conn, cur)
        elif choice == 2:    #determine choice
            search_dpart(conn, cur)
        elif choice == 3:
            update_dpart(conn, cur)
        elif choice == 4:
            delete_dpart(conn, cur)
        elif choice == 5:
            view_dpart(conn, cur)
        elif choice == 6:
            end(conn)

def display_menu():
    print('Department Menu')
    print('--------')
    print('1. Add Department')
    print('2. Search Departments')
    print('3. Update Departments')
    print('4. Delete Department')
    print('5. View all Departments')
    print('6 Exit')

def get_menu_choice():
    display_menu()
    choice = int(input('Enter Option...'))
        #validate
    while choice < 1 or choice > 6:
        choice = int(input('Invalid, Enter a valid choice...'))
        if choice == 6:
            print('End')
    return choice

def main():
    ch = 0

    #connect to db
    conn = sqlite3.connect('student_info.db')

    #cursor database
    cur = conn.cursor()

    while ch != 6:
        choice = get_menu_choice()
        execute_choice(conn, choice, cur)
    #close connection when done
    conn.commit()
    conn.close()
def contains_id(results, id):
    status = False
    for row in results:
        if row[0] == id:
            status = True
    return status
main()
