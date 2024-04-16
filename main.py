from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
import os
import re

from backend.db import SisDatabase

sisDatabase = SisDatabase('backend/sis.sqlite')

current_directory = os.getcwd()
fepc_logo_path = os.path.join(current_directory, 'images', 'fepc-logo.png')
# Frame Switching
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Far Eastern Polytechnic College | Student Information System")
        self.geometry("1360x690+0+0")
        self.resizable(width=FALSE, height=FALSE)
        self.current_page_index = 0
        self.pages = [self.user_type_page, self.login_form_page , self.student_form_page, self.dashboard_page]
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        
        self.main_frame = customtkinter.CTkFrame(self, fg_color='transparent')
        self.main_frame.pack(fill=BOTH, expand=YES)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.load_main_widgets()
        
    def load_main_widgets(self):
        self.create_pager_container()
        self.pages[self.current_page_index]()
    
    def clearFrames(self, frame):
        for child in frame.winfo_children():
            child.destroy()
        
        
    def create_pager_container(self):
        self.page_container = customtkinter.CTkFrame(self.main_frame, fg_color='transparent')
        self.page_container.pack(fill=BOTH, expand=YES)
    
    def changePage(self, page_name):
        self.clearFrames(self.page_container)
        
        match page_name:
            case "user_type_page":
                self.pages[0]()
                self.current_page_index = 0
            case "login_form_page":
                self.pages[1]()
                self.current_page_index = 1
            case "student_form_page":
                self.pages[2]()
                self.current_page_index = 2
            case "dashboard_page":
                self.pages[3]()
                self.current_page_index = 3
        
    def user_type_page(self):
        def openLoginWindow():
            self.changePage("login_form_page")

        def openStudentForm():
            self.changePage("student_form_page")

        self.clearFrames(self.page_container)
        self.user_type_container = customtkinter.CTkFrame(self.page_container, fg_color='transparent')
        self.user_type_container.pack(fill=BOTH, expand=YES)
        
        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path),size=(60,60))
        self.pageTitle = customtkinter.CTkLabel(self.user_type_container, text=" STUDENT INFORMATION SYSTEM", font=("Arial", 30, "bold"),image=self.fepc_logo,compound=LEFT)
        self.pageTitle.pack(pady=20, anchor="center")
        
        # Student Or Admin Button
        self.accountPickerFrame = customtkinter.CTkFrame(self.user_type_container,width=380,height=50,fg_color='transparent')
        self.accountPickerFrame.pack(pady=70, anchor="center")
        
        self.studentButton = customtkinter.CTkButton(self.accountPickerFrame,text="Student", width=180, height=50, command=openStudentForm)
        self.studentButton.place(x=0,y=0)
        self.adminButton = customtkinter.CTkButton(self.accountPickerFrame,text="Admin",  width=180, height=50, command=openLoginWindow)
        self.adminButton.place(x=200,y=0)
    
    def login_form_page(self):
        
        def authenticate():
            username = self.usernameEntry.get()
            password = self.passwordEntry.get()
            result = sisDatabase.authenticateAdmin(username, password)
            if result:
                user = result[1]
                messagebox.showinfo("Login Successfully!", f"Welcome! Admin {user}")
                self.changePage("dashboard_page")
            else:
                messagebox.showerror("Login Error", "Invalid username or password")

        self.clearFrames(self.page_container)
        
        self.login_container = customtkinter.CTkFrame(self.page_container, width=700, height=400)
        self.login_container.pack(pady=120, anchor=CENTER)
        
        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path), size=(300, 300))
        self.loginLogo = customtkinter.CTkLabel(self.login_container, image=self.fepc_logo, text="")
        self.loginLogo.place(x=40, y=50)

        self.inputsFrame = customtkinter.CTkFrame(self.login_container, width=400, height=300, fg_color='transparent')
        self.inputsFrame.place(x=360, y=50)

        customtkinter.CTkLabel(self.inputsFrame, text="Login Form", font=("Arial", 35, "bold")).place(x=20, y=0)

        self.usernameLabel = customtkinter.CTkLabel(self.inputsFrame, text="Username:", font=('Arial', 12, 'bold')).place(x=20, y=70)
        self.usernameEntry = customtkinter.CTkEntry(self.inputsFrame, placeholder_text="Enter Your Username", width=280, height=35)
        self.usernameEntry.place(x=20, y=95)

        self.passwordLabel = customtkinter.CTkLabel(self.inputsFrame, text="Password:", font=('Arial', 12, 'bold')).place(x=20, y=140)
        self.passwordEntry = customtkinter.CTkEntry(self.inputsFrame, placeholder_text="Enter Your Password", show="*", width=280, height=35)
        self.passwordEntry.place(x=20, y=165)

        self.loginButton = customtkinter.CTkButton(self.inputsFrame, width=280, height=40, text="LOGIN", command=authenticate)
        self.loginButton.place(x=20, y=220)
        
    def dashboard_page(self):
        self.clearFrames(self.page_container)
        self.dashboard_container = customtkinter.CTkFrame(self.page_container, fg_color='transparent')
        self.dashboard_container.pack(fill=BOTH, expand=YES)

        # Dashboard Title
        customtkinter.CTkLabel(self.dashboard_container, text="Dashboard", font=("Arial", 30, "bold")).pack(pady=20)

        # Quick Stats Frame
        quick_stats_frame = customtkinter.CTkFrame(self.dashboard_container, fg_color='white')
        quick_stats_frame.pack(fill=BOTH, expand=YES, padx=20, pady=10)

        # Add Quick Stats Widgets
        customtkinter.CTkLabel(quick_stats_frame, text="Quick Stats", font=("Arial", 20, "bold")).pack(pady=10)

        # You can add more widgets here for quick stats display, like total students, pending tasks, etc.
        # Example:
        customtkinter.CTkLabel(quick_stats_frame, text="Total Students: 1000").pack()
        customtkinter.CTkLabel(quick_stats_frame, text="Pending Tasks: 5").pack()

        # Recent Activities Frame
        recent_activities_frame = customtkinter.CTkFrame(self.dashboard_container, fg_color='white')
        recent_activities_frame.pack(fill=BOTH, expand=YES, padx=20, pady=10)

        # Add Recent Activities Widgets
        customtkinter.CTkLabel(recent_activities_frame, text="Recent Activities", font=("Arial", 20, "bold")).pack(pady=10)

        # You can add more widgets here for recent activities display, like recent logins, submissions, etc.
        # Example:
        customtkinter.CTkLabel(recent_activities_frame, text="1. Logged in as admin (2 minutes ago)").pack(anchor="w", padx=10)
        customtkinter.CTkLabel(recent_activities_frame, text="2. Submitted new student information (5 minutes ago)").pack(anchor="w", padx=10)

        # Logout Button
        customtkinter.CTkButton(self.dashboard_container, text="Logout", width=10, command=self.logout).pack(pady=20)

    def logout(self):
        # Add your logout logic here, for example, switch back to the login page
        self.changePage("login_form_page")

    def student_form_page(self):
        self.lrn_pattern = re.compile(r'^\d{12}$')
        self.first_name_pattern = re.compile(r'^[A-Za-z]{1,30}(?: [A-Za-z]{1,30})?$')
        self.middle_name_pattern = re.compile(r'^[A-Za-z]+(?: [A-Za-z]+)?$')
        self.last_name_pattern = re.compile(r'^[A-Za-z]{1,30}(?: [A-Za-z]{1,30})?$')
        self.address_pattern = re.compile(r'^[A-Za-z0-9\s\.,#-]{1,100}$')
        self.age_pattern = re.compile(r'^\d+$')
        self.birthday_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        self.phone_number_pattern = re.compile(r'^\d{11}$')
        
        # X and Y positioning
        self.column = {
            "first": 55,
            "second": 475,
            "third": 895,
        }
        
        self.row = {
            "first": 25,
            "second": 90,
            "third": 155,
            "fourth": 220,
        }
        self.student_form_container = customtkinter.CTkFrame(self.page_container, width=1920, height=680, fg_color='transparent')
        self.student_form_container.pack(fill=BOTH, expand=YES)

        # Load logo
        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path), size=(60, 60))

        # GUI Components
        self.pageTitle = customtkinter.CTkLabel(self.student_form_container, text="STUDENT INFORMATION SYSTEM", font=("Arial", 30, "bold"), image=self.fepc_logo, compound=LEFT)
        self.pageTitle.pack(pady=20, anchor="center")

        self.create_forms()
        
    def validate_entry(self, value, pattern):
        if pattern.match(value):
            return True
        else:
            return False
        
    def create_forms(self):
        # Forms Frame
        self.formsFrame = customtkinter.CTkFrame(self.student_form_container, height=400)
        self.formsFrame.pack(fill=X, padx=30)

        self.lrn_entry  =  self.create_form_entry(self.formsFrame, "STUDENT LRN:", "e.g 107921324321", self.row["first"], self.column["first"])
        self.firstname_entry  =  self.create_form_entry(self.formsFrame, "FIRST NAME:", "e.g Mark", self.row["second"], self.column["first"])
        self.middlename_entry =  self.create_form_entry(self.formsFrame, "MIDDLE NAME:", "e.g Resma", self.row["third"], self.column["first"])
        self.lastname_entry  =  self.create_form_entry(self.formsFrame, "LAST NAME:", "e.g Dacurawat", self.row["fourth"], self.column["first"])
        self.age_entry  =  self.create_form_entry(self.formsFrame, "AGE:", "e.g 19", self.row["first"], self.column["second"])
        self.birthday_entry  =  self.create_form_entry(self.formsFrame, "BIRTHDAY:", "e.g 1998-01-01",self.row["second"], self.column["second"])
        self.address_entry  =  self.create_form_entry(self.formsFrame, "ADDRESS:", "e.g Blk 50 Lot 2 ...",self.row["third"], self.column["second"])
        self.phonenumber_entry  =  self.create_form_entry(self.formsFrame, "PHONE #:", "e.g 09212121212",self.row["fourth"], self.column["second"])
        self.gender_option  =  self.create_form_option_menu(self.formsFrame, "GENDER:", ['Male', 'Female'],self.row["first"], self.column["third"])
        self.yearlevel_option  =  self.create_form_option_menu(self.formsFrame, "YEAR LEVEL:", ['1st Year', '2nd Year', '3rd Year', '4th Year'],self.row["second"], self.column["third"])
        self.course_option  =  self.create_form_option_menu(self.formsFrame, "COURSE:", ['B.S Computer Science', 'B.S Tourism Mngt.', 'B.S Hospitality Mngt.', 'B.S Bus. Administration', 'BTVTed Education'],self.row["third"], self.column["third"])
        self.semester_option  =  self.create_form_option_menu(self.formsFrame, "SEMESTER:", ["1st Semester", "2nd Semester"],self.row["fourth"], self.column["third"])

        def validate(): 
            lrn = self.lrn_entry.get()
            firstname = self.firstname_entry.get()
            middlename = self.middlename_entry.get()
            lastname = self.lastname_entry.get()
            age = self.age_entry.get()
            birthday = self.birthday_entry.get()
            address = self.address_entry.get()
            phonenumber = self.phonenumber_entry.get()
            gender = self.gender_option.get()
            
        
            if not self.validate_entry(lrn, self.lrn_pattern):
                messagebox.showerror("Error Message", "Invalid LRN.")
                return False
            if not self.validate_entry(firstname, self.first_name_pattern):
                messagebox.showerror("Error Message", "First name must be a string and allowed one space.")
                return False
            if not self.validate_entry(middlename, self.middle_name_pattern):
                messagebox.showerror("Error Message", "Middle name must be a string and allowed one space.")
                return False
            if not self.validate_entry(lastname, self.last_name_pattern):
                messagebox.showerror("Error Message", "Last name must be a string and allowed one space.")
                return False
            if not self.validate_entry(age, self.age_pattern):
                messagebox.showerror("Error Message", "Age must be a number.")
                return False
            if not self.validate_entry(birthday, self.birthday_pattern):
                messagebox.showerror("Error Message", "Birthday must be in the format YYYY-MM-DD.")
                return False
            if not self.validate_entry(address, self.address_pattern):
                messagebox.showerror("Error Message", "Address must be 100 characters or less.")
                return False
            if not self.validate_entry(phonenumber, self.phone_number_pattern):
                messagebox.showerror("Error Message", "Phone number must be 11 digits.")
                return False
            return True
        def save_student_info():
            if not validate():
                return
            
            lrn = self.lrn_entry.get()
            firstname = self.firstname_entry.get()
            middlename = self.middlename_entry.get()
            lastname = self.lastname_entry.get()
            age = self.age_entry.get()
            birthday = self.birthday_entry.get()
            address = self.address_entry.get()
            phonenumber = self.phonenumber_entry.get()
            gender = self.gender_option.get()
            yearlevel = self.yearlevel_option.get()
            course = self.course_option.get()
            semester = self.semester_option.get()
            
            print(lrn, firstname, middlename, lastname, age, birthday, address, mobilenumber, gender, yearlevel, course, semester)


        self.saveButton = customtkinter.CTkButton(self.formsFrame, width=100, height=40, text="SAVE", command=save_student_info)
        self.saveButton.place(y=250, x=55)
        
        
    def create_form_entry(self, frame, label_text, placeholder_text, y_position, x_position):
        entryFrame = customtkinter.CTkFrame(frame, width=380, height=35, fg_color='transparent')
        entryFrame.place(x=x_position, y=y_position)
        label = customtkinter.CTkLabel(entryFrame, text=label_text, font=('Arial', 13, 'bold'))
        label.place(x=0, y=3)
        entry = customtkinter.CTkEntry(entryFrame, placeholder_text=placeholder_text, width=250, height=35)
        entry.place(x=110, y=1)
        return entry
        

    def create_form_option_menu(self, frame, label_text, options, y_position, x_position):
        optionFrame = customtkinter.CTkFrame(frame, width=380, height=35, fg_color='transparent')
        optionFrame.place(x=x_position, y=y_position)
        label = customtkinter.CTkLabel(optionFrame, text=label_text, font=('Arial', 13, 'bold'))
        label.place(x=0, y=3)
        option = customtkinter.CTkOptionMenu(optionFrame, width=250, height=35, values=options)
        option.place(x=110, y=1)
        return option
    
    
        

if __name__ == "__main__":
    # Connect From Database
    sisDatabase.connect()
    
    # Create Tables
    sisDatabase.create_tables()
    # sisDatabase.insert_admin("admin", "12345")
    
    # Drop Tables
    # sisDatabase.drop_tables()
    
    app = App()
    app.mainloop()
        