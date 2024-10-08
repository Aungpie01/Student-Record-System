from tkinter import *
from tkinter import messagebox
import mysql.connector
from add_informatin import Student
from Register_page import Register

class Login:

    def __init__(self, root):
        self.window = root
        self.window.title('Login')
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

        self.img = PhotoImage(file='img/login.png')
        Label(self.window, image=self.img, bg='white', height=400, width=400).place(x=50, y=50)

        self.frame = Frame(self.window, width=350, height=350, bg='white', border=0)
        self.frame.place(x=480, y=70)

        self.heading = Label(self.frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        self.user = Entry(self.frame, width=25, fg='black', bd=0, bg='white', highlightthickness=0, font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.code = Entry(self.frame, width=25, fg='black', border=0, bg='white', highlightthickness=0, font=('Microsoft YaHei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', self.on_enter_code)
        self.code.bind('<FocusOut>', self.on_leave_code)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button(self.frame, width=32, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=self.signin).place(x=35, y=204)
        label = Label(self.frame, text="Don't you have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=45, y=270)

        def callclass():
            Register(root)

        sign_up = Button(self.frame, width=6, text='Sign Up', border=0, bg='white', highlightthickness=0, cursor='hand2', fg='#57a1f8', command=callclass)
        sign_up.place(x=217, y=266)

    def callFun(self):
        login_window = Toplevel(self.window)
        Student(login_window)

    def callfunGPA(self):
        from GPA_Student import GPA
        login_window = Toplevel(self.window)
        GPA(login_window)

    def signin(self):
        username = self.user.get()
        password = self.code.get()

        if username == 'admin' and password == 'adm1n':
            self.callFun()

        elif username!='admin' and password!='adm1n':
            sql='Select * from user where userName=%s and userPassword=%s'
            self.mycursor.execute(sql,(username,password))
            Student=self.mycursor.fetchone()
            messagebox.showinfo('Success','Your Login is Successful!!!')
            self.callfunGPA()
        else:
            messagebox.showerror('Invalid', 'Invalid username or password')

    def on_enter_user(self, e):
        if self.user.get() == 'username':
            self.user.delete(0, 'end')

    def on_leave_user(self, e):
        if self.user.get() == '':
            self.user.insert(0, 'username')

    def on_enter_code(self, e):
        if self.code.get() == 'Password':
            self.code.delete(0, 'end')

    def on_leave_code(self, e):
        if self.code.get() == '':
            self.code.insert(0, 'Password')

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
