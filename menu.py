import customtkinter as ctk
import customMenu

root = ctk.CTk()
root.title("Custom Menu")
root.geometry("300x200")

menu = customMenu.Menu(root)

file_menu = menu.menu_bar(text="File", tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()