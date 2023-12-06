import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a database cursor.
    cur = conn.cursor()
    
    # Add the Entries table.
    add_entries_table(cur)
    
    # Add rows to the Entries table.
    add_entries(cur)
    
    # Commit the changes.
    conn.commit()

    # Display the entries.
    display_entries(cur)
    
    # Close the connection.
    conn.close()

# The add_entries_table adds the Entries table to the database.
def add_entries_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Entries')

    # Create the table.
    cur.execute('''CREATE TABLE Entries (EntryID INTEGER PRIMARY KEY NOT NULL,
                                         Name TEXT,
                                         Phone TEXT)''')

# The add_entries function adds 5 rows to the Entries table.
def add_entries(cur):
    entries_list = [(1,'Jason Lee','555-1212'),
                    (2,'Amanda Green','555-0101'),
                    (3,'Jenna Jacobs','555-9090'),
                    (4,'Alfredo Greer','555-1234'),
                    (5,'Jules Landis','555-2345')]
    
    for row in entries_list:
        cur.execute('''INSERT INTO Entries (EntryID, Name, Phone)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

# The display_entries function displays the contents of
# the Entries table.
def display_entries(cur):
    print('Contents of phonebook.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]}')

# Execute the main function.
if __name__ == '__main__':
    main()