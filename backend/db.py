import sqlite3
import os
import hashlib

class SisDatabase:
    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        self.conn = None
        self.cursor = None
    
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file_path)
            self.cursor = self.conn.cursor()
            print("Successfully connected to SQLite database")
        except sqlite3.Error as e:
            print("Error connecting to SQLite database:", e)
    
    def create_tables(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS course (
                    id INTEGER PRIMARY KEY,
                    course_name VARCHAR(50) UNIQUE
                )
            """)
        
            self.cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    lrn VARCHAR(10) UNIQUE,
                    first_name VARCHAR(50),
                    middle_name VARCHAR(50),
                    last_name VARCHAR(50),
                    age INTEGER,
                    birthday VARCHAR(10),
                    address VARCHAR(255),
                    phone_number VARCHAR(15),
                    gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')),
                    year_level INTEGER,
                    course_id INTEGER,
                    semester VARCHAR(10),
                    FOREIGN KEY(course_id) REFERENCES course(id)
                )
            """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS admin (
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(50) UNIQUE,
                    password VARCHAR(255)
                )
            """)
            
            self.conn.commit()
            print("Tables created successfully")
        except Exception as e:
            print("Internal Server Error ", e)
            
    def authenticateAdmin(self, username, password):
        try:
            # Compute the MD5 hash of the password
            password_hash = hashlib.md5(password.encode()).hexdigest()
            
            self.cursor.execute("SELECT * FROM admin WHERE username = ? AND password = ?", (username, password_hash))
            result = self.cursor.fetchone()
            
            if result:
                return result
            else:
                return False
        except Exception as e:
            print("Internal Server Error ", e)
    
    def insert_admin(self, username, password):
        try:
            # Compute the MD5 hash of the password
            password_hash = hashlib.md5(password.encode()).hexdigest()
            
            # Insert the admin into the database
            self.cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", (username, password_hash))
            
            self.conn.commit()
            print("Admin inserted successfully!")
            
        except sqlite3.Error as e:
            print("Error inserting admin:", e)
            
    def register_admin(self, username, password):
        try:
            # Compute the MD5 hash of the password
            password_hash = hashlib.md5(password.encode()).hexdigest()

            # Insert the user into the database
            self.cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", (username, password_hash))

            self.conn.commit()
            print("User registered successfully!")
        except sqlite3.Error as e:
            print("Error registering user:", e)
    
    # Check if admin exist
    def check_username_exists(self, username):
        try:
            self.cursor.execute("SELECT * FROM admin WHERE username = ?", (username,))
            result = self.cursor.fetchone()

            if result:
                return True
            else:
                return False
        except Exception as e:
            print("Internal Server Error ", e)
    
    def insert_new_student(self, lrn, first_name, middle_name, last_name, age, birthday, address, phone_number, gender, year_level, course_id, semester):
        try:
            self.cursor.execute("INSERT INTO students (lrn, first_name, middle_name, last_name, age, birthday, address, phone_number, gender, year_level, course_id, semester) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (lrn, first_name, middle_name, last_name, age, birthday, address, phone_number, gender, year_level, course_id, semester))
            self.conn.commit()
            print("Student inserted successfully!")
        except sqlite3.Error as e:
            print("Error inserting student:", e)
            
    def countStudents(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM students")
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print("Internal Server Error ", e)
    
    def countCourses(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM course")
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print("Internal Server Error ", e)
            
    def countAdmins(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM admin")
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print("Internal Server Error ", e)

    
    def drop_tables(self):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS students")
            self.cursor.execute("DROP TABLE IF EXISTS course")
            self.cursor.execute("DROP TABLE IF EXISTS admin")
            self.conn.commit()
            print("Tables dropped successfully")
        except Exception as e:
            print("Internal Server Error ", e)
    
    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection closed successfully")