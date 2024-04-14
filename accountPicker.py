from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import re
import os

from main import mainpageOutput

class AccountPicker(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Account Picker")
        self.minsize(600, 300)
        self.maxsize(600, 300)
        self.current_directory = os.getcwd()
        self.fepc_logo_path = os.path.join(self.current_directory,'images/fepc-logo.png')

        self.fepc_logo = customtkinter.CTkImage(Image.open(self.fepc_logo_path),size=(60,60))
        self.pageTitle = customtkinter.CTkLabel(self, text=" STUDENT INFORMATION SYSTEM", font=("Arial", 30, "bold"),image=self.fepc_logo,compound=LEFT)
        self.pageTitle.pack(pady=20, anchor="center")
        
        # Student Or Admin Button
        self.accountPickerFrame = customtkinter.CTkFrame(self,width=380,height=50,fg_color='transparent')
        self.accountPickerFrame.pack(pady=70, anchor="center")
        
        self.studentButton = customtkinter.CTkButton(self.accountPickerFrame,text="Student", width=180, height=50)
        self.studentButton.place(x=0,y=0)
        self.adminButton = customtkinter.CTkButton(self.accountPickerFrame,text="Admin",  width=180, height=50, command=self.closeWindow)
        self.adminButton.place(x=200,y=0)

    def closeWindow(self):
        self.destroy()

app = AccountPicker()
app.mainloop()