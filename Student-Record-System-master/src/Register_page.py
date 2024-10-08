from tkinter import *
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, window):
        self.window = window
        self.window.title('Register')
        self.window.geometry('925x500+300+200')
        self.window.configure(bg='#fff')
        self.window.resizable(False, False)

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="project"
        )

        self.mycursor = self.mydb.cursor()

        # Background Image
        self.img = PhotoImage(file='img/login.png')
        Label(self.window, image=self.img, bg='white', height=400, width=400).place(x=50, y=50)

        # Frame
        self.frame = Frame(self.window, width=350, height=350, bg='white', border=0)
        self.frame.place(x=480, y=70)

        # Heading
        self.heading = Label(self.frame, text='Register', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        # User Name Entry
        self.user = Entry(self.frame, width=25, fg='black', bd=0, bg='white', highlightthickness=0, font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_enter)
        self.user.bind('<FocusOut>', self.on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        # Password Entry
        self.code = Entry(self.frame, width=25, fg='black', border=0, bg='white', highlightthickness=0, font=('Microsoft YaHei UI Light', 11), show='')
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', self.on_enter)
        self.code.bind('<FocusOut>', self.on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        # Confirm Password Entry
        self.confirmp = Entry(self.frame, width=25, fg='black', bd=0, bg='white', highlightthickness=0, font=('Microsoft YaHei UI Light', 11), show='')
        self.confirmp.place(x=30, y=220)
        self.confirmp.insert(0, 'Confirm Password')
        self.confirmp.bind('<FocusIn>', self.on_enter)
        self.confirmp.bind('<FocusOut>', self.on_leave)

        Frame(self.frame, width=300, height=2, bg='black').place(x=25, y=247)

        # Register Button
        Button(self.frame, width=32, pady=7, text='Register', bg='#57a1f8', fg='white', border=0, command=self.register).place(x=35, y=280)
        Label(self.frame, text="Already have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=49, y=333)

        # To go login page
        def open_login():
            from login_page import Login
            Login(self.window)

        self.sign_up = Button(self.frame, width=2, text='Login', border=0, bg='white', highlightthickness=0, cursor='hand2', fg='#57a1f8', command=open_login)
        self.sign_up.place(x=209, y=328)

    def register(self):
        username = self.user.get()
        password = self.code.get()
        confirm_password = self.confirmp.get()

        if password == confirm_password:
            sql = "INSERT INTO user (userName, userPassword) VALUES (%s, %s)"
            self.mycursor.execute(sql, (username, password))
            self.mydb.commit()
            messagebox.showinfo('Success', 'Your registration is successful! Please login again.')
            
            self.open_login()
            
        else:
            messagebox.showerror('Invalid', 'Confirm Password and Password did not match')

    def open_login(self):
        from login_page import Login
        Login(self.window)

    # Bind function
    def on_enter(self, e):
        widget = e.widget
        if widget == self.user and widget.get() == 'Username':
            widget.delete(0, 'end')
        elif widget == self.code and widget.get() == 'Password':
            widget.delete(0, 'end')
            widget.config(show='*')
        elif widget == self.confirmp and widget.get() == 'Confirm Password':
            widget.delete(0, 'end')
            widget.config(show='*')

    def on_leave(self, e):
        widget = e.widget
        if widget == self.user and widget.get() == '':
            widget.insert(0, 'Username')
        elif widget == self.code and widget.get() == '':
            widget.insert(0, 'Password')
            widget.config(show='')
        elif widget == self.confirmp and widget.get() == '':
            widget.insert(0, 'Confirm Password')
            widget.config(show='')


if __name__ == '__main__':
    window = Tk()
    app = Register(window)
    window.mainloop()
