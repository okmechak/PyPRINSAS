from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
import webbrowser
import os

# docs https://tkdocs.com/tutorial/

class Window(Frame):
        supported_file_types = [('all files', '*'), ('text files', '*.txt'), ('access 97', '*.mdb'), ('access', '*.accdb')]

        def __init__(self, master = None, cnf = {}, **kw):
            Frame.__init__(self, master)
            self.master = master


        def init_window(self):
            self.master.title("PyPRINSAS")
            
            # allowing the widget to take the full space of the root window
            self.pack(fill=BOTH, expand=1)

            #creation of menu bar
            #menubar
            menubar = Menu(root)
            self.master.config(menu = menubar)
            
            #Data IO
            file = Menu(menubar, tearoff=0)
            file.add_command(label = "New SANS Raw Data", command = self.open_file_dialog)
            file.add_command(label = "New USANS Raw Data", command = self.open_file_dialog)
            file.add_command(label = "New Processed Data", command = self.open_file_dialog)
            file.add_separator()
            file.add_command(label = "Summary of Data", command = self.donothing)
            file.add_command(label = "Edit Data", command = self.donothing)
            file.add_command(label = "Print", command = self.donothing)
            file.add_separator()
            file.add_command(label = "Open DataBase", command = self.open_file_dialog)
            file.add_command(label = "Save DataBase", command = self.save_file_dialog)
            file.add_command(label = "Add Data(SANS/USANS/Processed) to DataBase", command = self.donothing)
            file.add_separator()
            file.add_command(label = "Exit", command = root.quit)
            menubar.add_cascade(label = "Data Form", menu = file)
            
            #Data Processing
            editmenu = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label = "Data Processing", menu = editmenu)
            
            #Help
            helpmenu = Menu(menubar, tearoff = 0)
            helpmenu.add_command(label = "GitHub Help", command = self.open_pyprinsas_wiki)
            helpmenu.add_command(label = "GitHub repository", command = self.open_pyprinsas_repo)
            helpmenu.add_command(label = "Report Issues", command = self.open_pyprinsas_issues)
            menubar.add_cascade(label = "Help", menu = helpmenu)

        def open_file_dialog(self):
            name = filedialog.askopenfilename(filetypes = self.supported_file_types)
            showerror("Answer", "Sorry, not implemented yet. File Path: " + name)
        
        def save_file_dialog(self):
            name = filedialog.asksaveasfilename()
            showerror("Answer", "Sorry, not implemented yet. File Path: " + name)

        def donothing(self):
            showerror("Answer", "Sorry, not implemented yet.")

        def open_pyprinsas_wiki(self):
            webbrowser.open("https://github.com/okmechak/PyPRINSAS/wiki")
        
        def open_pyprinsas_repo(self):
            webbrowser.open("https://github.com/okmechak/PyPRINSAS")
        
        def open_pyprinsas_issues(self):
            webbrowser.open("https://github.com/okmechak/PyPRINSAS/issues")
            

  
root = Tk()
root.geometry("400x300")
app = Window(root)
app.init_window()
root.mainloop()