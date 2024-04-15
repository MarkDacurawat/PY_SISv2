import sqlite3
import os

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
                    gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')),
                    year_level INTEGER,
                    address VARCHAR(255),
                    phone_number VARCHAR(15),
                    course_id INTEGER,
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