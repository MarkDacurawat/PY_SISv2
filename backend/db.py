import sqlite3
import os

# Get the current working directory
current_directory = os.getcwd()

# Construct the full path to the database file using os.path.join()
db_file_path = os.path.join(current_directory, 'backend', 'sis.sqlite')

try:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)
    
    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    print("Successfully connected to SQLite database")
    
    def createTables():
        try:
        
            # Create Student Table
            cursor.execute(""" 
                        CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY,
                            lrn VARCHAR(10) UNIQUE,
                            first_name VARCHAR(50),
                            middle_name VARCHAR(50),
                            last_name VARCHAR(50),
                            gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')),
                            year_level INTEGER,
                            address VARCHAR(255),
                            phone_number VARCHAR(15),
                            course VARCHAR(50)
                        )
            """)
            
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS admin (
                                id INTEGER PRIMARY KEY,
                                username VARCHAR(50) UNIQUE,
                                password VARCHAR(255)
                            )
            """)
            
            # Commit Changes
            conn.commit()
            
            # Close Connection
            conn.close()
        
        except Exception as e:
            print("Internal Server Error ", e)
except sqlite3.Error as e:
    # Handle any errors that occur during the connection process
    print("Error connecting to SQLite database:", e)
