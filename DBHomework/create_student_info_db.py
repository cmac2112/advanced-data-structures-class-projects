import sqlite3




#commented extra stuff out, student_info.db already has existing created tables
#can uncomment these and run to remove existing data,
#student_info_db is attached



def main():
    # Connect to the database.
    conn = sqlite3.connect('student_info.db')

    # Get a Cursor object.
    cur = conn.cursor()
    
    
    #Drop the Majors, Departments, and Students tables, if they exist.
    #cur.execute('DROP TABLE IF EXISTS Majors')
    #cur.execute('DROP TABLE IF EXISTS Departments')
    #cur.execute('DROP TABLE IF EXISTS Students')

    # Enable Foreign Key Enforcement.
    #cur.execute('PRAGMA foreign_keys=ON')

    # Create the tables.
    #cur.execute('''CREATE TABLE Majors (MajorID INTEGER PRIMARY KEY NOT NULL, 
                                        #MajorName TEXT)''')
    #cur.execute('''CREATE TABLE Departments (DeptID INTEGER PRIMARY KEY NOT NULL, 
                                             #DeptName TEXT)''')
    #cur.execute('''CREATE TABLE Students (StudentID INTEGER PRIMARY KEY NOT NULL, 
                                          #StudentName TEXT,
                                          #MajorID INTEGER,
                                          #DeptID INTEGER,
                                          #FOREIGN KEY(MajorID) REFERENCES Majors(MajorID),
                                          #FOREIGN KEY(DeptID) REFERENCES Departments(DeptID)
                                          #)''')

    #adding a couple items
    #major_entry = [(1, 'Software'),
                   #(2,'Mathematics'),
                   #(3,'Physics')]

    #for row in major_entry:
        #cur.execute('''INSERT INTO Majors (MajorID, MajorName)
                    #    VALUES (?, ?)''', (row[0], row[1]))
    #depart_entry = [(1, 'Math'),
                    #(2, 'Sciences'),
                    #(3, 'Psych')]
    #for row in depart_entry:
        #cur.execute('''INSERT INTO Departments (DeptID, DeptName)
                    #    VALUES (?, ?)''', (row[0], row[1]))

    #student_entry = [(1, 'Bruh', '1', '1'),
                     #(2, 'mcgee', '1', '1'),
                     #(3, 'jamal', '2', '3')]
    #for row in student_entry:
                    #cur.execute('''INSERT INTO Students (StudentID, StudentName,
                   # MajorID, DeptID) VALUES (?, ?, ?, ?)''',(row[0], row[1],
                                                            # row[2], row[3]))

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()
main()
