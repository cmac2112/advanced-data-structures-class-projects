#majors
import sqlite3
def add_major(conn, cur):
    #add major function
    Major_id = input('ID:') #get input
    Major_name = input('Name:')

    #insert to database
    cur.execute('''INSERT INTO Majors (MajorID, MajorName)
                                VALUES (?, ?)''', ((Major_id), (Major_name)))
    conn.commit() #commit changes
    print('Success')

def view_major(conn, cur):
    cur.execute('SELECT MajorID, MajorName FROM Majors')

    results = cur.fetchall()

    print()
    for row in results: #display each row
            print(row)
    print()
def search_major(conn, cur):
    name = input('Major name to search for:')

    name = '%' + name + '%'
    #search for a row containing value
    cur.execute('''SELECT MajorName, MajorID FROM Majors Where MajorName LIKE ?'''
                , (name,))
    #get found results
    results = cur.fetchall()
    print(results)
    #print results determine if found
    if len(results) > 0:
        for row in results:
            print('Found')
        print()
    else:
        print('Not found.\n')
def update_major(conn, cur):
    #update function, get name to update
    name = input('Major name to update:')
    name = '%' + name + '%'

    #search for entry
    cur.execute('''SELECT MajorID, MajorName FROM Majors Where MajorName Like
                ?''',(name,))
    #fetch found results
    results = cur.fetchall()
    #print and determine
    if len(results) > 0:
        print('ID, Name')
        for row in results:
            print(f'{row[0]:<3} {row[1]:10}')
        id = int(input('Enter the ID of the entry you wish to update:'))
        if contains_id(results, id): #check if exists
            new_name = input('Enter new name for the Major:')
            new_id = input('Enter new Id for the Major:')
            cur.execute('''UPDATE Majors SET MajorName = ?, MajorID = ?
                        Where MajorID == ?''', (new_name, new_id, id)) #update
            conn.commit() #commit changes
            print('Updated')
        else:
            print('invalid ID entered.')
        print()
    else:
        print('Not found.\n')
def delete_major(conn,cur):
    #get name to delete
    name = input('Name to Delete')

    name = '%' + name + '%'

    #search for row containing needed entry
    cur.execute('''SELECT MajorID, MajorName FROM Majors Where MajorName LIKE
                ?''',(name,))
    #get results
    results = cur.fetchall()
    #only run if results are found
    if len(results) > 0:
        print(f'{"ID":3} {"Name":20}')
        for row in results: #display all rows of matching data
            print(f'{row[0]:<3} {row[1]:20}')
        id = int(input('Enter the ID of the entry you wish to delete: '))
        if contains_id(results, id): # check if id exists
            r_u_sure = input('Are you sure? (y/n): ')
            if (r_u_sure == 'y' or r_u_sure == 'Y'):
                #delete from database
                cur.execute('DELETE FROM Majors WHERE MajorID == ?', (id,))
                conn.commit()
                print('Entry deleted.\n')
        else:
            print('Not a valid ID.')
        print()
    else:
        print('Not found.\n')
    
#direction function
def execute_choice(conn, choice, cur):
        if choice == 1:
            add_major(conn, cur)
        elif choice == 2:    #determine choice
            search_major(conn, cur)
        elif choice == 3:
            update_major(conn, cur) #not broke so im not fixing it
        elif choice == 4:
            delete_major(conn, cur)
        elif choice == 5:
            view_major(conn, cur)
        elif choice == 6:
            done(conn)

def display_menu():
        print('menu')
        print('-----')
        print('1. Add Major')
        print('2. Search Major')
        print('3. Update Major')
        print('4. Delete Major')
        print('5. View all Majors')
        print('6 Exit')

#get choice from menu
def get_menu_choice():
    display_menu()
    choice = int(input('Enter Option...'))
        #validate
    while choice < 1 or choice > 6:
        choice = int(input('Invalid, Enter a valid choice...'))
        if choice == 6:
            print('End') #this is not broke so im not fixing it
            quit()
    return choice

def done(conn):
    conn.commit()
    conn.close()
    print('Done')
    quit() #closes program
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
