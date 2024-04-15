from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import os
import re
from backend.db import SisDatabase

sisDatabase = SisDatabase('backend/sis.sqlite')

current_directory = os.getcwd()
fepc_logo_path = os.path.join(current_directory, 'images', 'fepc-logo.png')
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Account Picker")
        self.minsize(600, 300)
        self.maxsize(600, 300)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path),size=(60,60))
        self.pageTitle = customtkinter.CTkLabel(self, text=" STUDENT INFORMATION SYSTEM", font=("Arial", 30, "bold"),image=self.fepc_logo,compound=LEFT)
        self.pageTitle.pack(pady=20, anchor="center")
        
        # Student Or Admin Button
        self.accountPickerFrame = customtkinter.CTkFrame(self,width=380,height=50,fg_color='transparent')
        self.accountPickerFrame.pack(pady=70, anchor="center")
        
        self.studentButton = customtkinter.CTkButton(self.accountPickerFrame,text="Student", width=180, height=50, command=self.openStudentForm)
        self.studentButton.place(x=0,y=0)
        self.adminButton = customtkinter.CTkButton(self.accountPickerFrame,text="Admin",  width=180, height=50, command=self.openLoginWindow)
        self.adminButton.place(x=200,y=0)
        
    def openStudentForm(self):
        StudentForm()
        self.withdraw()
    
    def openLoginWindow(self):
        LoginWindow()
        self.withdraw()

class StudentForm(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Student Information System")
        self.geometry("1920x680+-5+5")
        self.attributes('-topmost', True)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        

        # Functions
        self.lrn_pattern = re.compile(r'^\d{12}$')
        self.first_name_pattern = re.compile(r'^[A-Za-z]{1,30}(?: [A-Za-z]{1,30})?$')
        self.middle_name_pattern = re.compile(r'^[A-Za-z]+(?: [A-Za-z]{1,30})*$')
        self.last_name_pattern = re.compile(r'^[A-Za-z]{1,30}(?: [A-Za-z]{1,30})?$')
        self.address_pattern = re.compile(r'^[A-Za-z0-9\s\.,#-]{1,100}$')
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

        # Load logo
        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path), size=(60, 60))

        # GUI Components
        self.pageTitle = customtkinter.CTkLabel(self, text="STUDENT INFORMATION SYSTEM", font=("Arial", 30, "bold"), image=self.fepc_logo, compound=LEFT)
        self.pageTitle.pack(pady=20, anchor="center")

        self.create_forms()

    def create_forms(self):
        # Forms Frame
        formsFrame = customtkinter.CTkFrame(self, height=400)
        formsFrame.pack(fill=X, padx=30)

        self.create_form_entry(formsFrame, "STUDENT LRN:", "e.g 107921324321", self.row["first"], self.column["first"], self.lrn_pattern)
        self.create_form_entry(formsFrame, "FIRST NAME:", "e.g Mark", self.row["second"], self.column["first"], self.first_name_pattern)
        self.create_form_entry(formsFrame, "MIDDLE NAME:", "e.g Resma", self.row["third"], self.column["first"], self.middle_name_pattern)
        self.create_form_entry(formsFrame, "LAST NAME:", "e.g Dacurawat", self.row["fourth"], self.column["first"], self.last_name_pattern)
        self.create_form_option_menu(formsFrame, "GENDER:", ['Male', 'Female'], self.row["first"], self.column["second"])
        self.create_form_entry(formsFrame, "ADDRESS:", "e.g Blk 50 Lot 2 ...", self.row["second"], self.column["second"], self.address_pattern)
        self.create_form_entry(formsFrame, "MOBILE NUM:", "e.g 09212121212", self.row["third"], self.column["second"], self.phone_number_pattern)
        self.create_form_option_menu(formsFrame, "YEAR LEVEL:", ['1st Year', '2nd Year', '3rd Year', '4th Year'], self.row["fourth"], self.column["second"])
        self.create_form_option_menu(formsFrame, "COURSE:", ['B.S Computer Science', 'B.S Tourism Mngt.', 'B.S Hospitality Mngt.', 'B.S Bus. Administration', 'BTVTed Education'], self.row["first"], self.column["third"])

    def create_form_entry(self, frame, label_text, placeholder_text, y_position, x_position, pattern):
        entryFrame = customtkinter.CTkFrame(frame, width=380, height=35, fg_color='transparent')
        entryFrame.place(x=x_position, y=y_position)
        label = customtkinter.CTkLabel(entryFrame, text=label_text, font=('Arial', 13, 'bold'))
        label.place(x=0, y=3)
        entry = customtkinter.CTkEntry(entryFrame, placeholder_text=placeholder_text, width=250, height=35)
        entry.place(x=110, y=1)

    def create_form_option_menu(self, frame, label_text, options, y_position, x_position):
        optionFrame = customtkinter.CTkFrame(frame, width=380, height=35, fg_color='transparent')
        optionFrame.place(x=x_position, y=y_position)
        label = customtkinter.CTkLabel(optionFrame, text=label_text, font=('Arial', 13, 'bold'))
        label.place(x=0, y=3)
        optionMenu = customtkinter.CTkOptionMenu(optionFrame, width=250, height=35, values=options)
        optionMenu.place(x=110, y=1)

class LoginWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("710x400")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path), size=(300, 300))
        self.loginLogo = customtkinter.CTkLabel(self, image=self.fepc_logo, text="")
        self.loginLogo.place(x=40, y=50)

        self.inputsFrame = customtkinter.CTkFrame(self, width=400, height=300, fg_color='transparent')
        self.inputsFrame.place(x=360, y=50)

        customtkinter.CTkLabel(self.inputsFrame, text="Login Form", font=("Arial", 35, "bold")).place(x=20, y=0)

        self.usernameLabel = customtkinter.CTkLabel(self.inputsFrame, text="Username:", font=('Arial', 12, 'bold')).place(x=20, y=70)
        self.usernameEntry = customtkinter.CTkEntry(self.inputsFrame, placeholder_text="Enter Your Username", width=280, height=35)
        self.usernameEntry.place(x=20, y=95)

        self.passwordLabel = customtkinter.CTkLabel(self.inputsFrame, text="Password:", font=('Arial', 12, 'bold')).place(x=20, y=140)
        self.passwordEntry = customtkinter.CTkEntry(self.inputsFrame, placeholder_text="Enter Your Password", show="*", width=280, height=35)
        self.passwordEntry.place(x=20, y=165)

        self.loginButton = customtkinter.CTkButton(self.inputsFrame, width=280, height=40, text="LOGIN", command=self.authenticate)
        self.loginButton.place(x=20, y=220)
    def authenticate(self):
        self.withdraw()
        App().deiconify()

if __name__ == "__main__":
    # Connect From Database
    sisDatabase.connect()
    
    # Create Tables
    sisDatabase.create_tables()
    
    # Drop Tables
    # sisDatabase.drop_tables()
    
    App().mainloop()
