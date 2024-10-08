from tkinter import *
from tkinter import ttk, filedialog
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry

class Student:

    def __init__(self, root):
        self.root = root
        self.root.title('Student Record System')
        self.root.geometry('1730x550+0+0')
        
        self.StudentName = StringVar()
        self.RollNo = StringVar()
        self.NRC = StringVar()
        self.Dob = StringVar()
        self.FatherName = StringVar()
        self.Address = StringVar()
        self.PhoneNo = StringVar()
        self.Grade = StringVar()
        self.Gender = StringVar()
        self.Year = StringVar()
        
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "project"
        )

        self.mycursor = self.mydb.cursor()
        

        ##########################Frame...........
        self.MainFrame = Frame(self.root, bg='cadet blue')
        self.MainFrame.grid()

        DataFrame2=Frame(self.MainFrame,bd=1,width=2000,height=400,padx=5,pady=20, bg='cadet blue')
        DataFrame2.pack(side='bottom')

        ButtonFrame=Frame(DataFrame2,bd=2,width=2000,height=40,padx=5,pady=20, bg='cadet blue')
        ButtonFrame.pack(side='bottom',expand=False)

        DataFrame=Frame(self.MainFrame,bd=1,width=4000,height=6000,padx=2,pady=20, bg='cadet blue')
        DataFrame.pack(side='top')

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=2000, height=1000, bg='cadet blue', font=('Arial', 20, 'bold'), text='Student Details\n')
        DataFrameLeft.pack(side='left', fill='both', expand=True)

        self.DataFrameRight = LabelFrame(DataFrame, bd=1, width=2000, height=1000, padx=5, pady=8, bg='powder blue', font=('Arial', 20, 'bold'), text='All Student Details\n')
        self.DataFrameRight.pack(side='right', fill='both', expand=True)

        sql="select RollNo,StudentName,Gender,StudentClass,Grade,Dob,NRC,FatherName,Address,Phone_No from Student"
        self.mycursor.execute(sql)
        r_set=self.mycursor.fetchall()
        trv=ttk.Treeview(self.DataFrameRight,selectmode='browse')
        trv.grid(row=1,column=1,padx=20,pady=20)
        trv['columns']=('1','2','3','4','5','6','7','8','9','10')
        trv['show']='headings'
        trv.column('1',width=80,anchor='c')
        trv.column('2',width=130,anchor='c')
        trv.column('3',width=100,anchor='c')
        trv.column('4',width=100,anchor='c')
        trv.column('5',width=130,anchor='c')
        trv.column('6',width=130,anchor='c')
        trv.column('7',width=130,anchor='c')
        trv.column('8',width=130,anchor='c')
        trv.column('9',width=130,anchor='c')
        trv.column('10',width=130,anchor='c')
        trv.heading('1',text='Roll No')
        trv.heading('2',text='Name')
        trv.heading('3',text='Gender')
        trv.heading('4',text='Year')
        trv.heading('5',text='Grade')
        trv.heading('6',text='Dob')
        trv.heading('7',text='NRC')
        trv.heading('8',text='Father Name')
        trv.heading('9',text='Address')
        trv.heading('10',text='Phone No')
        for dt in r_set:
            trv.insert('','end',values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9]))

        ##########################Widget...........
        #row 1
        self.lblRoll = Label(DataFrameLeft, font=('Arial',14,'bold'), text='Roll No', padx=5, pady=3 , bg='cadet blue')
        self.lblRoll.grid(row=4, column=0, sticky='w')
        self.txtRoll = Entry(DataFrameLeft, font=('Arial',14,'bold'), textvariable=self.RollNo, width=30 )
        self.txtRoll.grid(row=4, column=1)

        #row 2
        self.lblName = Label(DataFrameLeft, font=('Arial',14,'bold'), text='Student Name', padx=5, pady=3 , bg='cadet blue')
        self.lblName.grid(row=5, column=0, sticky='w')
        self.txtName = Entry(DataFrameLeft, font=('Arial',14,'bold'), textvariable=self.StudentName, width=30)
        self.txtName.grid(row=5, column=1)

        #row 3
        self.lblGender = Label(DataFrameLeft, font=('Arial',14,'bold'), text='Gender', padx=2 , bg='cadet blue')
        self.lblGender.grid(row=6, column=0, sticky='w')
        self.cboGender = ttk.Combobox(DataFrameLeft, textvariable=self.Gender, state='readonly', font=('Arial',14,'bold'), width=29)
        self.cboGender['value'] = ('', 'Male', 'Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=6, column=1, pady=3, padx=20)

        #row 4
        self.lblYear = Label(DataFrameLeft, font=('Arial',14,'bold'), text='Year', padx=5, pady=3 , bg='cadet blue')
        self.lblYear.grid(row=7, column=0, sticky='w')
        self.txtYear = Entry(DataFrameLeft, font=('Arial',14,'bold'), textvariable=self.Year, width=30)
        self.txtYear.grid(row=7, column=1)

        #row 5
        self.lblGrade = Label(DataFrameLeft, font=('Arial',14,'bold'), text='Grade', padx=5, pady=3 , bg='cadet blue')
        self.lblGrade.grid(row=8, column=0, sticky='w')
        self.txtGrade = Entry(DataFrameLeft, font=('Arial',14,'bold'), textvariable=self.Grade, width=30 )
        self.txtGrade.grid(row=8, column=1)

        #row 6
        self.lblDob = Label(DataFrameLeft, font=('Arial',14,'bold'), text='Date Of Birth', padx=5, pady=3 , bg='cadet blue')
        self.lblDob.grid(row=9, column=0, sticky='w')
        self.txtDob = DateEntry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.Dob, width=30, background='darkblue', foreground='white')
        self.txtDob.grid(row=9, column=1, padx=10, sticky='w')

        #row 7
        self.lblNRC = Label(DataFrameLeft, font=('Arial',14,'bold'), text='NRC', padx=5, pady=3 , bg='cadet blue')
        self.lblNRC.grid(row=10, column=0, sticky='w')
        self.txtNRC = Entry(DataFrameLeft, font=('Arial',14,'bold'), textvariable=self.NRC, width=30)
        self.txtNRC.grid(row=10, column=1)

        #row 8
        self.lblFatherName = Label(DataFrameLeft, font=('Arial',14,'bold'), text="Father's Name", padx=5, pady=3 , bg='cadet blue')
        self.lblFatherName.grid(row=11, column=0, sticky='w')
        self.txtFatherName = Entry(DataFrameLeft, font=('Arial',14,'bold'), textvariable=self.FatherName, width=30)
        self.txtFatherName.grid(row=11, column=1)

        #row 9
        self.lblAddress = Label(DataFrameLeft, font=('Arial',14,'bold'), text='Address', padx=5, pady=3 , bg='cadet blue')
        self.lblAddress.grid(row=12, column=0, sticky='w')
        self.txtAddress = Entry(DataFrameLeft, font=('Arial',14,'bold'), textvariable=self.Address, width=30)
        self.txtAddress.grid(row=12, column=1)

        #row 10
        self.lblPhone = Label(DataFrameLeft, font=('Arial',14,'bold'), text='Phone', padx=5, pady=3 , bg='cadet blue')
        self.lblPhone.grid(row=13, column=0, sticky='w')
        self.txtPhone = Entry(DataFrameLeft, font=('Arial',14,'bold'), textvariable=self.PhoneNo, width=30)
        self.txtPhone.grid(row=13, column=1)

        #row 11
        self.btnUploadPhoto = Button(DataFrameLeft, text='Upload Photo', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, command=self.upload_photo)
        self.btnUploadPhoto.grid(row=14, column=1)

        ######################################button........................
        self.btnAddInsert = Button(ButtonFrame, text='Add Student', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, bg='lightblue', fg='black', command=self.insert_student)
        self.btnAddInsert.grid(row=0, column=1)

        self.btnAddShow = Button(ButtonFrame, text='Search Student', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, bg='lightgreen', fg='black', command=self.show_student_page)
        self.btnAddShow.grid(row=0, column=2)

        self.btnUpdate = Button(ButtonFrame, text='Update Student', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, bg='#FFFACD', fg='black', command=self.Update_student_page)
        self.btnUpdate.grid(row=0, column=3)

        self.btnDelete = Button(ButtonFrame, text='Delete Student', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, bg='lightcoral', fg='black', command=self.Delete_student_page)
        self.btnDelete.grid(row=0, column=4)

        self.btnDelete = Button(ButtonFrame, text='Add Mark', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, bg='lightpink', fg='black', command=self.AddMark_student_page)
        self.btnDelete.grid(row=0, column=5)

        self.btnDelete = Button(ButtonFrame, text='Logout', font=('Arial',12,'bold'), height=1, width=16, bd=2, padx=13, bg='red', fg='black', command=self.logout)
        self.btnDelete.grid(row=0, column=6)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title="Select a Photo", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            self.PhotoPath = file_path  # Set the file path attribute
            messagebox.showinfo("Photo Selected", f"Photo selected: {file_path}")
        else:
            messagebox.showwarning("No Photo Selected", "Please select a photo.")

    def insert_student(self):
        try:
            # Read photo data
            with open(self.PhotoPath, 'rb') as file:
                photo_data = file.read()

            # SQL insert query
            query = "INSERT INTO Student (RollNo, StudentName, Gender, StudentClass, Grade, Dob, NRC, FatherName, Address, Phone_No, StudentPhoto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            # Execute the query with parameters
            self.mycursor.execute(query, (
                self.RollNo.get(), 
                self.StudentName.get(), 
                self.Gender.get(), 
                self.Year.get(), 
                self.Grade.get(), 
                self.Dob.get(), 
                self.NRC.get(), 
                self.FatherName.get(), 
                self.Address.get(), 
                self.PhoneNo.get(), 
                photo_data  # Pass photo data as binary
            ))
            # Commit the transaction
            self.mydb.commit()
            sql="select RollNo,StudentName,Gender,StudentClass,Grade,Dob,NRC,FatherName,Address,Phone_No from Student"
            self.mycursor.execute(sql)
            r_set=self.mycursor.fetchall()
            trv=ttk.Treeview(self.DataFrameRight,selectmode='browse')
            trv.grid(row=1,column=1,padx=20,pady=20)
            trv['columns']=('1','2','3','4','5','6','7','8','9','10')
            trv['show']='headings'
            trv.column('1',width=80,anchor='c')
            trv.column('2',width=130,anchor='c')
            trv.column('3',width=100,anchor='c')
            trv.column('4',width=100,anchor='c')
            trv.column('5',width=130,anchor='c')
            trv.column('6',width=130,anchor='c')
            trv.column('7',width=130,anchor='c')
            trv.column('8',width=130,anchor='c')
            trv.column('9',width=130,anchor='c')
            trv.column('10',width=130,anchor='c')
            trv.heading('1',text='Roll No')
            trv.heading('2',text='Name')
            trv.heading('3',text='Gender')
            trv.heading('4',text='Year')
            trv.heading('5',text='Grade')
            trv.heading('6',text='Dob')
            trv.heading('7',text='NRC')
            trv.heading('8',text='Father Name')
            trv.heading('9',text='Address')
            trv.heading('10',text='Phone No')
            for dt in r_set:
                trv.insert('','end',values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9]))
            # Show success messagebox
            messagebox.showinfo("Success", "Student record added successfully!")
        except mysql.connector.Error as err:
            # Handle any potential MySQL errors
            messagebox.showerror("Error", f"Error: {err}")



    def show_student_page(self):
        from show_page import ShowStudent
        Show_window = Toplevel(self.root)
        ShowStudent(Show_window)

    def Update_student_page(self):
        from Update_page import UpdateStudent
        update_window = Toplevel(self.root)
        UpdateStudent(update_window)

    def Delete_student_page(self):
        from delete_page import DeleteStudent
        delete_window = Toplevel(self.root)
        DeleteStudent(delete_window)

    def AddMark_student_page(self):
        from AddMark_Student_page import AddMark
        delete_window = Toplevel(self.root)
        AddMark(delete_window)

    def logout(self):
        from login_page import Login
        delete_window = Toplevel(self.root)
        Login(delete_window)

if __name__=='__main__':
    root=Tk()
    application=Student(root)
    root.mainloop()
