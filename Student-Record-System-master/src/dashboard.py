from tkinter import *
from PIL import Image
from login_page import Login
from Register_page import Register

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title('Dashboard')
        self.root.geometry('500x500')
        self.root.resizable(False, False)

        self.bg_color = '#57a1f8'

        # Icon Create
        self.login_admin_icon = PhotoImage(file='img/login_teacher_img.png')
        self.exit_icon = PhotoImage(file='img/exit_img.png')

        # Frame Create
        self.welcome_page_fm = Frame(self.root, highlightbackground=self.bg_color, highlightthickness=3, width=400)

        #Heading Create
        self.heading_lb = Label(self.welcome_page_fm, bg=self.bg_color, text='Welcome To Student Record \n && Management System', fg='black', font=('Bold', 18))
        self.heading_lb.place(x=0, y=0, width=400)

        # Login Teacher Button
        self.admin_login_btn = Button(self.welcome_page_fm, text='Login', bg=self.bg_color, fg='black', font=('Bold', 15), bd=0,command=self.open_login)
        self.admin_login_btn.place(x=100, y=125, width=200)

        #Register Button
        self.admin_register_btn = Button(self.welcome_page_fm, text='Register', bg=self.bg_color, fg='black', font=('Bold', 15), bd=0,command=self.open_register)
        self.admin_register_btn.place(x=100, y=225, width=200)

        #Exit Button
        self.exit_btn = Button(self.welcome_page_fm, text='Exit', bg=self.bg_color, fg='black', font=('Bold', 15), bd=0)
        self.exit_btn.place(x=100, y=325, width=200)

        #Frame Pack to window
        self.welcome_page_fm.pack(pady=30)
        self.welcome_page_fm.pack_propagate(False)
        self.welcome_page_fm.configure(width=400, height=420)

    def open_login(self):
        login_window = Toplevel(self.root)
        Login(login_window)

    def open_register(self):
        register_window = Toplevel(self.root)
        Register(register_window)

if __name__ == '__main__':
    root = Tk()
    app = Dashboard(root)
    root.mainloop()
