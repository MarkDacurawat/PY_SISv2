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
        self.pages = [self.user_type_page, self.login_form_page , self.student_form_page, self.dashboard_page, self.signup_form_page]
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        
        # Regex
        self.lrn_pattern = re.compile(r'^\d{12}$')
        self.first_name_pattern = re.compile(r'^[A-Za-z]{1,30}(?: [A-Za-z]{1,30})?$')
        self.middle_name_pattern = re.compile(r'^[A-Za-z]+(?: [A-Za-z]+)?$')
        self.last_name_pattern = re.compile(r'^[A-Za-z]{1,30}(?: [A-Za-z]{1,30})?$')
        self.address_pattern = re.compile(r'^[A-Za-z0-9\s\.,#-]{1,100}$')
        self.age_pattern = re.compile(r'^\d+$')
        self.birthday_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        self.phone_number_pattern = re.compile(r'^\d{11}$')
        
        # Admin Login
        self.userLoggedIn = False
        self.userDetails = None
        self.key_pressed = None
        
        self.main_frame = customtkinter.CTkFrame(self, fg_color='transparent')
        self.main_frame.pack(fill=BOTH, expand=YES)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.load_main_widgets()
        
        def on_closing(event=None):
            confirmation = messagebox.askokcancel("Exit", "Are you sure you want to exit?")
            if confirmation:
                app.destroy()
        self.bind("<Escape>", on_closing)
        self.protocol("WM_DELETE_WINDOW", on_closing)
        
        
        
        
    def load_main_widgets(self):
        self.create_pager_container()
        self.pages[self.current_page_index]()
    
    def clearFrames(self, frame):
        for child in frame.winfo_children():
            child.destroy()
        
        
    def create_pager_container(self):
        self.page_container = customtkinter.CTkFrame(self.main_frame, fg_color='transparent')
        self.page_container.pack(fill=BOTH, expand=YES)
    
    def changePage(self, page_name, student=None):
        self.clearFrames(self.page_container)
        self.unbind("<Return>")
        
        match page_name:
            case "user_type_page":
                self.pages[0]()
                self.current_page_index = 0
            case "login_form_page":
                self.pages[1]()
                self.current_page_index = 1
            case "student_form_page":
                self.pages[2](method="SAVE")
                self.current_page_index = 2
            case "view_student_page":
                self.pages[2](method="UPDATE", student=student)
                self.current_page_index = 2
            case "dashboard_page":
                self.pages[3]()
                self.current_page_index = 3
            case "signup_form_page":
                self.pages[4]()
                self.current_page_index = 4
                
    def windowTitle(self, parent, title):
        fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path),size=(60,60))
        pageTitle = customtkinter.CTkLabel(parent, text=f" {title}", font=("Arial", 30, "bold"),image=fepc_logo,compound=LEFT)
        pageTitle.pack(pady=20, anchor="center")
            
        
    def user_type_page(self):
        def openLoginWindow():
            self.changePage("login_form_page")

        def openStudentForm():
            self.changePage("student_form_page")

        self.clearFrames(self.page_container)
        self.user_type_container = customtkinter.CTkFrame(self.page_container, fg_color='transparent')
        self.user_type_container.pack(fill=BOTH, expand=YES)
        
        self.windowTitle(self.user_type_container, "STUDENT INFORMATION SYSTEM")
        
        self.accountPickerFrame = customtkinter.CTkFrame(self.user_type_container, width=1000, height=500)
        self.accountPickerFrame.pack(pady=20, anchor="center")
        
        self.studentChoiceFrame = customtkinter.CTkFrame(self.accountPickerFrame,width=300,height=400)
        self.studentChoiceFrame.pack(pady=20, side=LEFT, padx=40)
        
        self.graduationCapImage = customtkinter.CTkImage(Image.open(os.path.join(current_directory, 'images', 'student.png')),size=(100,100))
        self.studentImage = customtkinter.CTkLabel(self.studentChoiceFrame,text="",bg_color="transparent", fg_color="transparent" , font=("Arial", 20, "bold"),image=self.graduationCapImage)
        self.studentImage.place(x=20,y=150)
        
        self.studentText = customtkinter.CTkLabel(self.studentChoiceFrame,text="I am Student",bg_color="transparent", fg_color="transparent" , font=("Arial", 35, "bold"))
        self.studentText.place(x=20,y=270)
        
        self.studentButton = customtkinter.CTkButton(self.studentChoiceFrame,text="CHOOSE", width=260, height=50,command=openStudentForm)
        self.studentButton.place(x=20,y=320)
        
        self.adminChoiceFrame = customtkinter.CTkFrame(self.accountPickerFrame,width=300,height=400)
        self.adminChoiceFrame.pack(pady=20, side=RIGHT, padx=40)
        
        self.graduationCapImage = customtkinter.CTkImage(Image.open(os.path.join(current_directory, 'images', 'admin.png')),size=(100,100))
        self.adminImage = customtkinter.CTkLabel(self.adminChoiceFrame,text="",bg_color="transparent", fg_color="transparent" , font=("Arial", 20, "bold"),image=self.graduationCapImage)
        self.adminImage.place(x=20,y=150)
        
        self.adminText = customtkinter.CTkLabel(self.adminChoiceFrame,text="I am Admin",bg_color="transparent", fg_color="transparent" , font=("Arial", 35, "bold"))
        self.adminText.place(x=20,y=270)
        
        self.adminButton = customtkinter.CTkButton(self.adminChoiceFrame,text="CHOOSE",fg_color="blue", hover_color="darkblue" , width=260, height=50, command=openLoginWindow)
        self.adminButton.place(x=20,y=320)
    
    def login_form_page(self):
        
        def authenticate(event=None):
            username = self.usernameEntry.get()
            password = self.passwordEntry.get()
            result = sisDatabase.authenticateAdmin(username, password)
            if result:
                user = result[1]
                messagebox.showinfo("Login Successfully!", f"Welcome! Admin {user}")
                self.userLoggedIn = True
                self.userDetails = user
                self.changePage("dashboard_page")
            else:
                messagebox.showerror("Login Error", "Invalid username or password")
                
        self.bind("<Return>", authenticate)
        
        self.login_container = customtkinter.CTkFrame(self.page_container, width=700, height=400)
        self.login_container.pack(pady=120, anchor=CENTER)
        
        self.backButton = customtkinter.CTkButton(self.login_container, text="Back", width=100, height=50, command=lambda: self.changePage("user_type_page"))
        self.backButton.place(x=0, y=0)
        
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
        
        
        
    def signup_form_page(self):
        
        # Validate Registration Entry
        def validate():
            usernamePattern = re.compile(r'^[a-zA-Z0-9]{3,20}(?:_[a-zA-Z0-9]{3,20})?$')
            passwordPattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
                    
            username = self.usernameEntry.get()
            password = self.passwordEntry.get()
                    
            if not usernamePattern.match(username):
                messagebox.showwarning("Warning", "Invalid username. Only alphanumeric characters (A-Z, a-z, 0-9) are allowed, with at most one underscore. Username must be between 3 to 20 characters.")
                return False
            if not passwordPattern.match(password):
                messagebox.showwarning('Warning','''
        Invalid password. Please ensure your password meets the following criteria:
                                            
        - At least one lowercase letter (a-z)
        - At least one uppercase letter (A-Z)
        - At least one digit (0-9)
        - Minimum length of 8 characters
                                            ''')
                return False
            return True
        
        def register(event=None):
            username = self.usernameEntry.get()
            password = self.passwordEntry.get()
            
            if not validate():
                return
            
            # Check if username already exists
            if sisDatabase.check_username_exists(username):
                messagebox.showerror("Username Already Exists", "Username already exists!")
                return
           
            success = sisDatabase.register_admin(username, password)
            messagebox.showinfo("Signup Successful!", "You have successfully signed up!")
            self.changePage("dashboard_page")
            
        self.bind("<Return>", register)
            
        self.signup_container = customtkinter.CTkFrame(self.page_container, width=700, height=400)
        self.signup_container.pack(pady=120, anchor=CENTER)
        
        self.backButton = customtkinter.CTkButton(self.signup_container, text="Back", width=100, height=50, command=lambda: self.changePage("dashboard_page"))
        self.backButton.place(x=0, y=0)

        
        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path), size=(300, 300))
        self.signupLogo = customtkinter.CTkLabel(self.signup_container, image=self.fepc_logo, text="")
        self.signupLogo.place(x=40, y=50)

        self.inputsFrame = customtkinter.CTkFrame(self.signup_container, width=400, height=300, fg_color='transparent')
        self.inputsFrame.place(x=360, y=50)

        customtkinter.CTkLabel(self.inputsFrame, text="Sign Up Form", font=("Arial", 35, "bold")).place(x=20, y=0)

        self.usernameLabel = customtkinter.CTkLabel(self.inputsFrame, text="Username:", font=('Arial', 12, 'bold')).place(x=20, y=70)
        self.usernameEntry = customtkinter.CTkEntry(self.inputsFrame, placeholder_text="Enter Your Username", width=280, height=35)
        self.usernameEntry.place(x=20, y=95)

        self.passwordLabel = customtkinter.CTkLabel(self.inputsFrame, text="Password:", font=('Arial', 12, 'bold')).place(x=20, y=140)
        self.passwordEntry = customtkinter.CTkEntry(self.inputsFrame, placeholder_text="Enter Your Password", show="*", width=280, height=35)
        self.passwordEntry.place(x=20, y=165)

        self.signupButton = customtkinter.CTkButton(self.inputsFrame, width=280, height=40, text="SIGN UP", command=register)
        self.signupButton.place(x=20, y=220)



    def dashboard_page(self):
        
        def createTotalFrame(parent, totalTitle, totalText, totalCount,color ,  row_position, column_position):
            totalFrame = customtkinter.CTkFrame(parent, width=300, height=150, fg_color=f"{color}")
            totalFrame.grid(row=row_position, column=column_position, padx=10, pady=10, stick="w")
            totalTitle = customtkinter.CTkLabel(totalFrame, text=f"{totalTitle}", font=("Arial", 28, "bold"), text_color="white")
            totalTitle.place(x=20, y=20)
            totalLabel = customtkinter.CTkLabel(totalFrame, text=f"Total {totalText}: {totalCount}", font=("Arial",18, "bold"), text_color="white")
            totalLabel.place(x=20, y=100)
        
        def findStudentByLRN():
            lrn = self.findStudentEntry.get()
            if self.lrn_pattern.match(lrn):
                student = sisDatabase.findStudentByLRN(lrn)
                if student:
                    self.changePage("view_student_page", student=student)
                else:
                    messagebox.showerror("No Student Found", "No student found with that LRN!")
            else:
                messagebox.showerror("Invalid LRN", "LRN must be a 12 digit number!")
            
        
        totalStudents = sisDatabase.countStudents()
        totalAdmins = sisDatabase.countAdmins()
        totalBSCS = sisDatabase.countBSCS()
        totalBSTM = sisDatabase.countBSTM()
        totalBSHM = sisDatabase.countBSHM()
        totalBSBA = sisDatabase.countBSBA()
        totalBTVTed = sisDatabase.countBTVTed()
        totalGraduated = sisDatabase.countGraduatedStudents()
        
        self.dashboard_container = customtkinter.CTkFrame(self.page_container, fg_color='transparent')
        self.dashboard_container.pack(fill=BOTH, expand=YES)
        
        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path),size=(60,60))
        self.pageTitle = customtkinter.CTkLabel(self.dashboard_container, text=" DASHBOARD WINDOW", font=("Arial", 30, "bold"),image=self.fepc_logo,compound=LEFT)
        self.pageTitle.pack(pady=20, anchor="center")
        
        self.addAdminButton = customtkinter.CTkButton(self.dashboard_container, text="Add New Admin", height=45, command=lambda: self.changePage("signup_form_page"))
        self.addAdminButton.place(x=1030, y=45)
        
        self.addStudentButton = customtkinter.CTkButton(self.dashboard_container, text="Add Student", height=45, command=lambda: self.changePage("student_form_page"))
        self.addStudentButton.place(x=1180, y=45)
        
        self.actionsFrame = customtkinter.CTkFrame(self.dashboard_container)
        self.actionsFrame.pack(fill=X, padx=30)
        
        self.welcomeAdminLabel = customtkinter.CTkLabel(self.actionsFrame, text="Welcome Admin "+f"{self.userDetails}".upper(), font=("Arial", 15, "bold"))
        self.welcomeAdminLabel.pack(side=LEFT, padx=10, pady=10)
        
        self.findStudentButton = customtkinter.CTkButton(self.actionsFrame, text="Find Student", fg_color="yellow", hover_color="yellow", text_color="black" , height=45, command=findStudentByLRN)
        self.findStudentButton.pack(side=RIGHT, pady=10, padx=10)
        
        self.findStudentEntry = customtkinter.CTkEntry(self.actionsFrame, placeholder_text="Enter a Student LRN", width=220, height=45)
        self.findStudentEntry.pack(side=RIGHT, pady=10)
        
        self.totalsFrame = customtkinter.CTkFrame(self.dashboard_container)
        self.totalsFrame.pack(fill=X, padx=30, pady=10)
        
        # ['B.S Computer Science', 'B.S Tourism Mngt.', 'B.S Hospitality Mngt.', 'B.S Bus. Administration', 'BTVTed Education']
        createTotalFrame(self.totalsFrame, "Students", "student", totalStudents, "#486581",0,0)
        createTotalFrame(self.totalsFrame, "Computer Science", "BSCS student", totalBSCS, "#800000", 0,1)
        createTotalFrame(self.totalsFrame, "Hospitality Mngt", "BSHM student", totalBSHM, "#41B06E",0,2)
        createTotalFrame(self.totalsFrame, "Tourism Mngt", "BSTM student", totalBSTM, "#5E1675", 0,3)
        createTotalFrame(self.totalsFrame, "Admins", "admins", totalAdmins, "#486581", 1, 0)
        createTotalFrame(self.totalsFrame, "Bus. Administration", "BSBA student", totalBSBA, "#FFD23F", 1, 1)
        createTotalFrame(self.totalsFrame, "Education", "BTVTed student", totalBTVTed, "#074173", 1, 2)
        createTotalFrame(self.totalsFrame, "Graduated", "Graduated student", totalGraduated, "#481E14", 1, 3)
    
        self.logoutButton = customtkinter.CTkButton(self.dashboard_container, text="LOGOUT", fg_color="red", hover_color="darkred", height=50, command=self.logout)
        self.logoutButton.place(x=1180, y=550)
       

    def logout(self):
        confirmation = messagebox.askokcancel("Logout", "Are you sure you want to logout?")
        if confirmation:
            self.changePage("login_form_page")
            self.userLoggedIn = False
            self.userDetails = None
        
        

    def student_form_page(self, method="UPDATE", student=None):
        
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
        
        def configEntries():
            self.lrn_entry.insert(0, student[1])
            self.firstname_entry.insert(0, student[2])
            self.middlename_entry.insert(0, student[3])
            self.lastname_entry.insert(0, student[4])
            self.age_entry.insert(0, student[5])
            self.birthday_entry.insert(0, student[6])
            self.address_entry.insert(0, student[7])
            self.phonenumber_entry.insert(0, student[8])
            self.gender_option.set(student[9])
            self.yearlevel_option.set(student[10])
            self.course_option.set(student[11])
            self.semester_option.set(student[12])
            
            
        
        self.student_form_container = customtkinter.CTkFrame(self.page_container, width=1920, height=680, fg_color='transparent')
        self.student_form_container.pack(fill=BOTH, expand=YES)

        self.windowTitle(self.student_form_container, "STUDENT FORM WINDOW")
        
        if self.userLoggedIn:
            self.backButton = customtkinter.CTkButton(self.student_form_container, text="Back", height=45,fg_color="blue",  hover_color="darkblue" , command=lambda: self.changePage("dashboard_page"))
            self.backButton.place(x=30, y=20)
        else:
            self.backButton = customtkinter.CTkButton(self.student_form_container, text="Back", height=45, command=lambda: self.changePage("user_type_page"))
            self.backButton.place(x=30, y=20)

        self.create_forms(method=method)

        if method == "UPDATE" and  student:
            configEntries()
        
        
    def validate_entry(self, value, pattern):
        if pattern.match(value):
            return True
        else:
            return False
        
    def create_forms(self, method="SAVE"):
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
        self.course_option  =  self.create_form_option_menu(self.formsFrame, "COURSE:", ['B.S Computer Science', 'B.S Tourism Mngt', 'B.S Hospitality Mngt', 'B.S Bus. Administration', 'BTVTed Education'],self.row["third"], self.column["third"])
        self.semester_option  =  self.create_form_option_menu(self.formsFrame, "SEMESTER:", ["1st Semester", "2nd Semester"],self.row["fourth"], self.column["third"])
        
        if self.userLoggedIn and method == "UPDATE":
            self.yearlevel_option.configure(values=['1st Year', '2nd Year', '3rd Year', '4th Year', 'Graduated'])

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
        def save_student_info(event=None):
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
            
            sisDatabase.insert_new_student(lrn, firstname, middlename, lastname, age, birthday, address, phonenumber, gender, yearlevel, course, semester)
            
            messagebox.showinfo("Success Message", "Student information saved.")
            
            if not self.userLoggedIn:
                self.changePage('user_type_page')
            else:
                self.changePage('dashboard_page')
            
        def update_student_info(event=None):
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
            
            sisDatabase.update_student(lrn, firstname, middlename, lastname, age, birthday, address, phonenumber, gender, yearlevel, course, semester)
            
            messagebox.showinfo("Success Message", "Student information saved.")
            self.changePage("dashboard_page")


        if(method == "SAVE"):
            self.saveButton = customtkinter.CTkButton(self.formsFrame, width=1200, height=40, text="SAVE", command=save_student_info)
            self.saveButton.place(y=320, x=55)
            self.bind("<Return>", save_student_info)
        else:
            self.updateButton = customtkinter.CTkButton(self.formsFrame, width=1200, height=40,fg_color="blue", hover_color="darkblue", text="UPDATE" , command=update_student_info)
            self.updateButton.place(y=320, x=55)
            self.bind("<Return>", update_student_info)
        
        
        
        
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
    # sisDatabase.insert_admin("admin","12345")
    
    # Drop Tables
    # sisDatabase.drop_tables()
    
    app = App()
    app.mainloop()
        