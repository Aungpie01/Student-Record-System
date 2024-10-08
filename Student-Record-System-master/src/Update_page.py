from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from add_informatin import Student

class UpdateStudent:

    def __init__(self, root):
        self.root = root
        self.root.title('Update Student Information')
        self.root.geometry('1350x750+0+0')
        
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
        self.RollSearch=StringVar()

        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "project"
        )

        self.mycursor = self.mydb.cursor()

        ##########################Frame...........
        self.MainFrame = Frame(self.root, bg="white")
        self.MainFrame.pack(fill=BOTH, expand=1, padx=20, pady=20)
        

        # Title
        self.lblTitle = Label(self.MainFrame, font=('Arial', 20, 'bold'), text='Update Student Details', padx=2, pady=2, bg="white")
        self.lblTitle.grid(row=0, column=0, columnspan=5, pady=(0, 20))
        
        
        ##########################Widget...........
        self.rollS = Label(self.MainFrame, font=('Arial',14,'bold'), text=' Enter Roll No That You Want To Search', padx=2, pady=2, bg='White')
        self.rollS.grid(row=2, column=0, sticky='w')
        self.txtSearchroll = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.RollSearch, width=28 , bg="white")
        self.txtSearchroll.grid(row=2, column=1)

        #row 1
        self.roll = Label(self.MainFrame, font=('Arial',14,'bold'), text='Roll No', padx=2, pady=2, bg='White')
        self.roll.grid(row=4, column=0, sticky='w')
        self.txtroll = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.RollNo, width=28 , bg="white")
        self.txtroll.grid(row=4, column=1)

        #row 2
        self.Name = Label(self.MainFrame, font=('Arial',14,'bold'), text='Student Name', padx=2, pady=2 , bg="white")
        self.Name.grid(row=5, column=0, sticky='w')
        self.txtName = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.StudentName, width=28 , bg="white")
        self.txtName.grid(row=5, column=1)

        #row 3
        self.lblGender = Label(self.MainFrame, font=('Arial',14,'bold'), text='gender', padx=2 , bg="white")
        self.lblGender.grid(row=6, column=0, sticky='w')
        self.cboGender = ttk.Combobox(self.MainFrame, textvariable=self.Gender, state='readonly', font=('Arial',14,'bold'), width=27) 
        self.cboGender['value'] = ('', 'Male', 'Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=6, column=1, pady=3, padx=20)

        #row 4
        self.lbYear = Label(self.MainFrame, font=('Arial',14,'bold'), text='Year', padx=2, pady=2 , bg="white")
        self.lbYear.grid(row=7, column=0, sticky='w')
        self.txtYear = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Year, width=28 , bg="white")
        self.txtYear.grid(row=7, column=1)

        #row 5
        self.lblGrade = Label(self.MainFrame, font=('Arial',14,'bold'), text='Grade', padx=2, pady=2 , bg="white")
        self.lblGrade.grid(row=8, column=0, sticky='w')
        self.txtGrade = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Grade, width=28 , bg="white")
        self.txtGrade.grid(row=8, column=1)

        #row 6
        self.lblDob = Label(self.MainFrame, font=('Arial',14,'bold'), text='Date Of Birth', padx=2, pady=2 , bg="white")
        self.lblDob.grid(row=9, column=0, sticky='w')
        self.txtDob = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Dob, width=28 , bg="white")
        self.txtDob.grid(row=9, column=1)

        #row 7
        self.lblNRC = Label(self.MainFrame, font=('Arial',14,'bold'), text='NRC', padx=2, pady=2 , bg="white")
        self.lblNRC.grid(row=10, column=0, sticky='w')
        self.txtNRC = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.NRC, width=28 , bg="white")
        self.txtNRC.grid(row=10, column=1)

        #row 8
        self.lblFatherName = Label(self.MainFrame, font=('Arial',14,'bold'), text="Father's Name", padx=2, pady=2 , bg="white")
        self.lblFatherName.grid(row=11, column=0, sticky='w')
        self.txtFatherName = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.FatherName, width=28 , bg="white")
        self.txtFatherName.grid(row=11, column=1)

        #row 9
        self.lblAddress = Label(self.MainFrame, font=('Arial',14,'bold'), text='Address', padx=2, pady=2 , bg="white")
        self.lblAddress.grid(row=12, column=0, sticky='w')
        self.txtAddress = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Address, width=28 , bg="white")
        self.txtAddress.grid(row=12, column=1)

        #row 10
        self.lblPhone = Label(self.MainFrame, font=('Arial',14,'bold'), text='Phone', padx=2, pady=2 , bg="white")
        self.lblPhone.grid(row=13, column=0, sticky='w')
        self.txtPhone = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.PhoneNo, width=28 , bg="white") 
        self.txtPhone.grid(row=13, column=1)

        ##button
        self.btnSearch = Button(self.MainFrame, text='Search Student', font=('Arial',12,'bold'), height=1, width=16, bd=2 , bg="#FFC107", fg="black", padx=13, command=self.search_student)
        self.btnSearch.grid(row=14, column=0) 

        self.btnUpdate = Button(self.MainFrame, text='Update Student', font=('Arial',12,'bold'), height=1, width=16, bd=2 ,  bg="#4CAF50", fg="white",  padx=13, command=self.update_student)
        self.btnUpdate.grid(row=14, column=1)

        self.btnHome = Button(self.MainFrame, text='Home', font=('Arial',12,'bold'), height=1, width=16 , bg="#2196F3", fg="white", bd=2, padx=13, command=self.Home)
        self.btnHome.grid(row=14, column=2)

        self.btnExit = Button(self.MainFrame, text='Exit', font=('Arial',12,'bold'), height=1 , bg="#F44336", fg="white", width=16, bd=2, padx=13, command=self.Exit)
        self.btnExit.grid(row=14, column=3)

    def search_student(self):
        # Get the roll number entered by the user for searching
        roll_to_search = self.RollSearch.get()

        # Write your SQL query to fetch student details based on the roll number
        query = "SELECT * FROM Student WHERE RollNo = %s"
        self.mycursor.execute(query, (roll_to_search,))
        student = self.mycursor.fetchone()

        # Populate the Entry fields with the fetched student details
        if student:
            # Display the roll number
            self.RollNo.set(student[1])

            # Set the fetched student details to the respective variables or directly to Entry widgets
            self.StudentName.set(student[2])
            self.Gender.set(student[3])
            self.Year.set(student[4])
            self.Grade.set(student[5])
            self.Dob.set(student[6])
            self.NRC.set(student[7])
            self.FatherName.set(student[8])
            self.Address.set(student[9])
            self.PhoneNo.set(student[10])
        else:
            messagebox.showerror("Error", "Student not found")

    def update_student(self):
        # Get the updated values from the entry fields
        roll_no = self.RollNo.get()
        student_name = self.StudentName.get()
        gender = self.Gender.get()
        year = self.Year.get()
        grade = self.Grade.get()
        dob = self.Dob.get()
        nrc = self.NRC.get()
        father_name = self.FatherName.get()
        address = self.Address.get()
        phone_no = self.PhoneNo.get()

        # Write your SQL query to update student details based on the roll number
        query = """
        UPDATE Student 
        SET StudentName = %s, Gender = %s, StudentClass = %s, Grade = %s, Dob = %s, NRC = %s, FatherName = %s, Address = %s, Phone_No = %s 
        WHERE RollNo = %s
        """
        values = (student_name, gender, year, grade, dob, nrc, father_name, address, phone_no, roll_no)

        try:
            self.mycursor.execute(query, values)
            self.mydb.commit()
            messagebox.showinfo("Success", "Student record updated successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error updating student record: {err}")

    def Home(self):
        HomeWindow = Toplevel(self.root)
        Student(HomeWindow)

    def Exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    application = UpdateStudent(root)
    root.mainloop()
