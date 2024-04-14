from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import os
import re
from backend.db import createTables

class StudentForm(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Information System")
        self.geometry("1920x680+-5+5")
        self.attributes('-topmost', True)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        self.current_directory = os.getcwd()
        self.fepc_logo_path = os.path.join(self.current_directory, 'images', 'fepc-logo.png')

        # Functions
        self.lrn_pattern = re.compile(r'^\d{12}$')
        self.first_name_pattern = re.compile(r'^[A-Za-z]{1,30}(?: [A-Za-z]{1,30})?$')
        self.middle_name_pattern = re.compile(r'^[A-Za-z]+(?: [A-Za-z]{1,30})*$')
        self.last_name_pattern = re.compile(r'^[A-Za-z]{1,30}(?: [A-Za-z]{1,30})?$')
        self.address_pattern = re.compile(r'^[A-Za-z0-9\s\.,#-]{1,100}$')
        self.phone_number_pattern = re.compile(r'^\d{11}$')

        # Load logo
        self.fepc_logo = customtkinter.CTkImage(Image.open(self.fepc_logo_path), size=(60, 60))

        # GUI Components
        self.pageTitle = customtkinter.CTkLabel(self, text="STUDENT INFORMATION SYSTEM", font=("Arial", 30, "bold"), image=self.fepc_logo, compound=LEFT)
        self.pageTitle.pack(pady=20, anchor="center")

        self.create_forms()

    def create_forms(self):
        # Forms Frame
        formsFrame = customtkinter.CTkFrame(self, height=220)
        formsFrame.pack(fill=X, padx=30)

        self.create_form_entry(formsFrame, "STUDENT LRN:", "e.g 107921324321", 25, 55, self.lrn_pattern)
        self.create_form_entry(formsFrame, "FIRST NAME:", "e.g Mark", 90, 55, self.first_name_pattern)
        self.create_form_entry(formsFrame, "MIDDLE NAME:", "e.g Resma", 155, 55, self.middle_name_pattern)
        self.create_form_entry(formsFrame, "LAST NAME:", "e.g Dacurawat", 25, 475, self.last_name_pattern)
        self.create_form_option_menu(formsFrame, "GENDER:", ['Male', 'Female'], 90, 475)
        self.create_form_entry(formsFrame, "ADDRESS:", "e.g Blk 50 Lot 2 ...", 155, 475, self.address_pattern)
        self.create_form_entry(formsFrame, "MOBILE NUM:", "e.g 09212121212", 25, 895, self.phone_number_pattern)
        self.create_form_option_menu(formsFrame, "YEAR LEVEL:", ['1st Year', '2nd Year', '3rd Year', '4th Year'], 90, 895)
        self.create_form_option_menu(formsFrame, "COURSE:", ['B.S Computer Science', 'B.S Tourism Mngt.', 'B.S Hospitality Mngt.', 'B.S Bus. Administration', 'BTVTed Education'], 155, 895)

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
    createTables()
    app = StudentForm()
    app.mainloop()
