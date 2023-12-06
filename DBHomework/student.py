import sqlite3
def execute_choice(conn, choice, cur):
        if choice == 1:
            add_student(conn, cur)
        elif choice == 2:    #determine choice
            search_student(conn, cur)
        elif choice == 3:
            update_student(conn, cur)
        elif choice == 4:
            delete_student(conn, cur)
        elif choice == 5:
            view_student(conn, cur)
        elif choice == 6:
                done(conn)
def view_student(conn, cur):
        cur.execute('SELECT StudentID, StudentName, MajorID, DeptID FROM Students')

        results = cur.fetchall()
        # for visual refrence what major/dept they are in
        cur.execute('''SELECT MajorID, MajorName FROM Majors''')
        majornames = cur.fetchall()
        cur.execute('''SELECT DeptID, DeptName FROM Departments''')
        departnames = cur.fetchall()

        #display
        print('ID, Name, MajorID, DeptID')
        for row in results:
               print(row)
        print('MajorID, Majors')
        for row in majornames:
                print(row)
        print('DepartmentID, Departments')
        for row in departnames:
                print(row)
        print()
def add_student(conn, cur):
    # Add student function
    student_id = int(input('ID:'))
    student_name = input('Name:')

    # Retrieve valid major IDs from the database
    cur.execute('SELECT MajorID, MajorName FROM Majors')
    majorids = [row[0] for row in cur.fetchall()] #get first row which contains ids
    print(f'Valid Major IDs: {majorids}')

    # Prompt for major ID and validate it
    major = int(input('Enter Major ID:'))
    if major not in majorids:
        print('Invalid Major ID')
        return

    # Retrieve valid department IDs from the database
    cur.execute('SELECT DeptID FROM Departments')
    deptids = [row[0] for row in cur.fetchall()]
    print(f'Valid Department IDs: {deptids}')

    # Prompt for department ID and validate it
    department = int(input('Enter Department ID:'))
    if department not in deptids:
        print('Invalid Department ID')
        return

    # Insert new student record into the database
    cur.execute('''INSERT INTO Students (StudentID, StudentName, MajorID, DeptID)
                VALUES (?, ?, ?, ?)''', (student_id, student_name, major, department))
    print('New entry added')
    conn.commit() #commit changes
                
    

    #insert to database
    
def update_student(conn, cur):
    choice = 0
    print('Enter (1) to update student name/id')
    choice = int(input('Enter (2) to update student major/department:'))
    if choice == 1:
        # get name to be searched
        name = input('Name to search:')
        cur.execute('''SELECT StudentID, StudentName FROM Students
                        WHERE StudentName LIKE ?''', (name,))
        results = cur.fetchall() #get results
        if len(results) > 0: #if results exist..
            print(f'{"ID":3} {"StudentName":20}')
            for row in results: #print for each row in results
                print(f'{row[0]:<3}{row[1]:20}') #format
            id = int(input('Enter the Id of the entry to update:'))
            if contains_id(results, id): #validate entry
                new_name = input('Enter new name:') #enter new name and execute
                cur.execute('''UPDATE Students SET StudentNAME = ? WHERE
                                    StudentID == ?''', (new_name, id))
                conn.commit()#commit changes
                print('Name updated')
            else:
                print('Invalid ID')
            print()
        else:
            print('Not found.')
    else: #change major/department
        name = input('Name to search:')
        cur.execute('''SELECT StudentID, StudentName, MajorID, DeptID FROM Students
                        WHERE StudentName Like ?''', (name,))
        results = cur.fetchall()
        if len(results) > 0: #if exists
            for row in results:
                print(f'{row[0]:<3}{row[1]:20}{row[2]:20}')
            id = int(input('Enter StudentID to update:'))
            if contains_id(results, id): #validate id exists
                new_major = 0
                cur.execute('''SELECT MajorID FROM Majors''')#get all major ids
                majorids = cur.fetchall() #'load' them all
                print(f'Valid Major Ids: {majorids}') #display valid majors
                new_major = int(input('Enter new Major Id, Enter same id to keep:'))
                # validate
                val = cur.execute('''SELECT * FROM Majors WHERE MajorID = ?''', (new_major,))
                if val.fetchone() is not None: #if exists
                    print('Valid')
                    deptids = 0
                    cur.execute('''SELECT DeptID FROM Departments''')
                    # create list from id's to validate later
                    deptlist = [dept[0] for dept in cur.fetchall()]
                    print(f'Valid Department Ids: {deptlist}') #valid ids
                    deptids = int(input('Enter new Department Id:'))
                    if deptids in deptlist:
                        cur.execute('''UPDATE Students SET MajorID = ? WHERE
                                            StudentID == ?''', (new_major, id))
                        cur.execute('''UPDATE Students SET DeptID = ? WHERE
                                            StudentID == ?''', (deptids, id))
                        print('Updated')
                        conn.commit()
                    else:
                        print('Invalid Department ID')
                        main()
                else:
                    print('Invalid Major ID') 
                    main()
            else:
                print('Invalid Id')
            print()
        else:
            print('Not Found')
def delete_student(conn, cur):
    cur.execute('SELECT StudentName FROM Students')
    Stulist = [row[0] for row in cur.fetchall()]
    print(Stulist)
    delete = input('Enter name to be deleted')
    delete = '%' + delete + '%'

    cur.execute('''SELECT StudentID, StudentName FROM Students Where StudentName LIKE
                ?''',(delete,))
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
                cur.execute('DELETE FROM Students WHERE StudentID == ?', (id,))
                conn.commit() #commit changes
                print('Entry deleted.\n')
        else:
            print('Not a valid ID.')
        print()
    else:
        print('Not found.\n')
def search_student(conn, cur):
        name = input('Student name to search:')
        name = '%' + name + '%'

        cur.execute('''SELECT StudentName, StudentID, MajorID, DeptID FROM Students Where
                        StudentName Like ?''', (name,))

        results = cur.fetchall()
        print(results)
        if len(results) > 0:
                for row in results:
                        print('Found')
                print()
        else:
                print('Not found.\n')
def display_menu():
        print('menu')
        print('-----')
        print('1. Add Students')
        print('2. Search Students')
        print('3. Update Students')
        print('4. Delete Students')
        print('5. View all Students')
        print('6 Exit')
        print('-----')

#get choice from menu
def get_menu_choice():
    display_menu()
    choice = int(input('Enter Option...'))
        #validate
    while choice < 1 or choice > 6:
        choice = int(input('Invalid, Enter a valid choice...'))
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
    conn.close()


    
def done(conn):
        conn.commit()
        conn.close()
        print('Done')
        quit()
def contains_id(results, id):
    status = False
    for row in results:
        if row[0] == id:
            status = True
    return status  
main()
