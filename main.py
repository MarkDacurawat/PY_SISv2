from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import os
import re

current_directory = os.getcwd()
fepc_logo_path = os.path.join(current_directory, 'images', 'fepc-logo.png')
# Frame Switching
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Account Picker")
        self.geometry("1360x690+0+0")
        self.resizable(width=FALSE, height=FALSE)
        self.current_page_index = 0
        self.pages = [self.user_type_page, self.login_form_page , self.student_form_page]
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
    
    def changePage(self, page_index):
        self.clearFrames(self.page_container)
        self.current_page_index = page_index
        self.pages[page_index]()
        
    def user_type_page(self):
        def openLoginWindow():
            self.changePage(1)

        def openStudentForm():
            self.changePage(2)

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
        
        def nextPage():
            self.changePage(1)
        
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

        self.loginButton = customtkinter.CTkButton(self.inputsFrame, width=280, height=40, text="LOGIN", command=nextPage)
        self.loginButton.place(x=20, y=220)
        
        
    
    def student_form_page(self):
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
        self.student_form_container = customtkinter.CTkFrame(self.page_container, width=1920, height=680, fg_color='transparent')
        self.student_form_container.pack(fill=BOTH, expand=YES)

        # Load logo
        self.fepc_logo = customtkinter.CTkImage(Image.open(fepc_logo_path), size=(60, 60))

        # GUI Components
        self.pageTitle = customtkinter.CTkLabel(self.student_form_container, text="STUDENT INFORMATION SYSTEM", font=("Arial", 30, "bold"), image=self.fepc_logo, compound=LEFT)
        self.pageTitle.pack(pady=20, anchor="center")

        self.create_forms()

    def create_forms(self):
        # Forms Frame
        self.formsFrame = customtkinter.CTkFrame(self.student_form_container, height=400)
        self.formsFrame.pack(fill=X, padx=30)

        self.create_form_entry(self.formsFrame, "STUDENT LRN:", "e.g 107921324321", self.row["first"], self.column["first"], self.lrn_pattern)
        self.create_form_entry(self.formsFrame, "FIRST NAME:", "e.g Mark", self.row["second"], self.column["first"], self.first_name_pattern)
        self.create_form_entry(self.formsFrame, "MIDDLE NAME:", "e.g Resma", self.row["third"], self.column["first"], self.middle_name_pattern)
        self.create_form_entry(self.formsFrame, "LAST NAME:", "e.g Dacurawat", self.row["fourth"], self.column["first"], self.last_name_pattern)
        self.create_form_option_menu(self.formsFrame, "GENDER:", ['Male', 'Female'], self.row["first"], self.column["second"])
        self.create_form_entry(self.formsFrame, "ADDRESS:", "e.g Blk 50 Lot 2 ...", self.row["second"], self.column["second"], self.address_pattern)
        self.create_form_entry(self.formsFrame, "MOBILE NUM:", "e.g 09212121212", self.row["third"], self.column["second"], self.phone_number_pattern)
        self.create_form_option_menu(self.formsFrame, "YEAR LEVEL:", ['1st Year', '2nd Year', '3rd Year', '4th Year'], self.row["fourth"], self.column["second"])
        self.create_form_option_menu(self.formsFrame, "COURSE:", ['B.S Computer Science', 'B.S Tourism Mngt.', 'B.S Hospitality Mngt.', 'B.S Bus. Administration', 'BTVTed Education'], self.row["first"], self.column["third"])

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
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
        