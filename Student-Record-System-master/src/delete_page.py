from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from add_informatin import Student
class DeleteStudent:

    def __init__(self, root):
        self.root = root
        self.root.title('Delete Student Information')
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
        self.lblTitle = Label(self.MainFrame, font=('Arial', 20, 'bold'), text='Delete Student Details', padx=2, pady=2, bg="white")
        self.lblTitle.grid(row=0, column=0, columnspan=5, pady=(0, 20))
        

        ##########################Widget...........
        self.rollS = Label(self.MainFrame, font=('Arial',14,'bold'), text=' Enter Roll No That You Want To Delete', padx=2, pady=2, bg="white")
        self.rollS.grid(row=2, column=0, sticky='w')
        self.txtSearchroll = Entry(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.RollSearch, width=28 , bg="white")
        self.txtSearchroll.grid(row=2, column=1)

        #row 1
        self.roll = Label(self.MainFrame, font=('Arial',14,'bold'), text='Roll No', padx=2, pady=2, bg="white")
        self.roll.grid(row=4, column=0, sticky='w')
        self.txtroll = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.RollNo, width=28 , bg="white")
        self.txtroll.grid(row=4, column=1)

        #row 2
        self.Name = Label(self.MainFrame, font=('Arial',14,'bold'), text='Student Name', padx=2, pady=2 , bg="white")
        self.Name.grid(row=5, column=0, sticky='w')
        self.txtName = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.StudentName, width=28 , bg="white")
        self.txtName.grid(row=5, column=1)

        #row 3
        self.lblFirstname = Label(self.MainFrame, font=('Arial',14,'bold'), text='Gender', padx=2, pady=2 , bg="white")
        self.lblFirstname.grid(row=6, column=0, sticky='w')
        self.txtFirstname = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Gender, width=28 , bg="white")
        self.txtFirstname.grid(row=6, column=1)

        #row 4
        self.lbYear = Label(self.MainFrame, font=('Arial',14,'bold'), text='Year', padx=2, pady=2 , bg="white")
        self.lbYear.grid(row=7, column=0, sticky='w')
        self.txtYear = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Year, width=28 , bg="white")
        self.txtYear.grid(row=7, column=1)

        #row 5
        self.lblGrade = Label(self.MainFrame, font=('Arial',14,'bold'), text='Grade', padx=2, pady=2 , bg="white")
        self.lblGrade.grid(row=8, column=0, sticky='w')
        self.txtGrade = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Grade, width=28 , bg="white")
        self.txtGrade.grid(row=8, column=1)

        #row 6
        self.lblDob = Label(self.MainFrame, font=('Arial',14,'bold'), text='Date Of Birth', padx=2, pady=2 , bg="white")
        self.lblDob.grid(row=9, column=0, sticky='w')
        self.txtDob = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Dob, width=28 , bg="white")
        self.txtDob.grid(row=9, column=1)

        #row 7
        self.lblNRC = Label(self.MainFrame, font=('Arial',14,'bold'), text='NRC', padx=2, pady=2 , bg="white")
        self.lblNRC.grid(row=10, column=0, sticky='w')
        self.txtNRC = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.NRC, width=28 , bg="white")
        self.txtNRC.grid(row=10, column=1)

        #row 8
        self.lblFatherName = Label(self.MainFrame, font=('Arial',14,'bold'), text="Father's Name", padx=2, pady=2 , bg="white")
        self.lblFatherName.grid(row=11, column=0, sticky='w')
        self.txtFatherName = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.FatherName, width=28 , bg="white")
        self.txtFatherName.grid(row=11, column=1)

        #row 9
        self.lblAddress = Label(self.MainFrame, font=('Arial',14,'bold'), text='Adderss', padx=2, pady=2 , bg="white")
        self.lblAddress.grid(row=12, column=0, sticky='w')
        self.txtAddress = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.Address, width=28 , bg="white")
        self.txtAddress.grid(row=12, column=1)

        #row 10
        self.lblPhone = Label(self.MainFrame, font=('Arial',14,'bold'), text='Phone', padx=2, pady=2 , bg="white")
        self.lblPhone.grid(row=11, column=0, sticky='w')
        self.txtPhone = Label(self.MainFrame, font=('Arial',14,'bold'), textvariable=self.PhoneNo, width=28 , bg="white")
        self.txtPhone.grid(row=11, column=1)

        ##button
        self.btnSearch = Button(self.MainFrame, text='Search Student', font=('Arial',12,'bold'), height=1 , bg="#FFC107", fg="black", width=16,bd=2, padx=13, command=self.search_student)
        self.btnSearch.grid(row=13, column=0)

        self.btnDelete = Button(self.MainFrame, text='Delete Student', font=('Arial',12,'bold'), height=1 ,  bg="#4CAF50", fg="white", width=16,bd=2, padx=13, command=self.delete_student)
        self.btnDelete.grid(row=13, column=1)

        self.btnHome = Button(self.MainFrame, text='Home', font=('Arial',12,'bold'), height=1, width=16 , bg="#2196F3", fg="white", bd=2, padx=13, command=self.Home)
        self.btnHome.grid(row=13, column=2)

        self.btnExit = Button(self.MainFrame, text='Exit', font=('Arial',12,'bold'), height=1 , bg="#F44336", fg="white", width=16, bd=2, padx=13, command=self.Exit)
        self.btnExit.grid(row=13, column=3)

        

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


    def Exit(self):
        # Implement logic to go back to the home page or close the window
        # For example:
        self.root.destroy()

    def Home(self):
        HomeWindow = Toplevel(self.root)
        Student(HomeWindow)
    
    def delete_student(self):
        roll_to_delete = self.RollSearch.get()
        query = "SELECT * FROM Student WHERE RollNo = %s"
        self.mycursor.execute(query, (roll_to_delete,))
        student = self.mycursor.fetchone()

        # Check if the roll number is provided
        if not roll_to_delete:
            messagebox.showerror("Error", "Please enter a Roll Number to delete")
            return

        # Ask for confirmation before deleting the record
        confirmation = messagebox.askyesno("Delete", "Are you sure you want to delete this student?")
        if confirmation:
            if student:
                studentid=student[0]
                try:
                    # Write your SQL query to delete student details based on the roll number
                    query1="DELETE FROM Student_Mark WHERE Student_Id = %s"
                    self.mycursor.execute(query1,(studentid,))
                    self.mydb.commit()
                    query = "DELETE FROM Student WHERE Student_Id = %s"
                    self.mycursor.execute(query, (studentid,))
                    self.mydb.commit()  # Commit the transaction

                    # Clear the fields after deletion
                    self.clear_fields()

                    messagebox.showinfo("Success", "Student record deleted successfully")
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error deleting student: {err}")

    def clear_fields(self):
        self.RollNo.set("")
        self.StudentName.set("")
        self.Gender.set("")
        self.Year.set("")
        self.Grade.set("")
        self.Dob.set("")
        self.NRC.set("")
        self.FatherName.set("")
        self.Address.set("")
        self.PhoneNo.set("")
        self.RollSearch.set("")


if __name__ == '__main__':
    root = Tk()
    application = DeleteStudent(root)
    root.mainloop()

