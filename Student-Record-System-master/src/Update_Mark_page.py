from tkinter import *
from tkinter import messagebox
import mysql.connector
from add_informatin import Student

class UpdateMark:

    def __init__(self, root):
        self.root = root
        self.root.title('Update Student Mark')
        self.root.geometry('1350x750+0+0')
        
        self.Myanmar = StringVar()
        self.English = StringVar()
        self.Math = StringVar()
        self.Physics = StringVar()
        self.Chemistry = StringVar()
        self.Biology = StringVar()
        self.RollNo = StringVar()
        self.Name = StringVar()

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="project"
        )

        self.mycursor = self.mydb.cursor()

        ##########################Frame...........
        self.MainFrame = Frame(self.root, bg="white")
        self.MainFrame.pack(fill=BOTH, expand=1, padx=20, pady=20)
        

        # Title
        self.lblTitle = Label(self.MainFrame, font=('Arial', 20, 'bold'), text='Update Student mark', padx=2, pady=2, bg="white")
        self.lblTitle.grid(row=0, column=0, columnspan=5, pady=(0, 20))
        
        ##########################Widget...........
        self.rollS = Label(self.MainFrame, font=('Arial', 14, 'bold'), text=' Enter Roll No That You Want To Add Mark', padx=2, pady=2, bg="white")
        self.rollS.grid(row=2, column=0, sticky='w')
        self.txtSearchroll = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.RollNo, width=28 , bg="white")
        self.txtSearchroll.grid(row=2, column=1)

        self.lbName = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Name', padx=2, pady=2 , bg="white")
        self.lbName.grid(row=3, column=0, sticky='w')
        self.txtName = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Name, width=28 , bg="white")
        self.txtName.grid(row=3, column=1)

        #row 1
        self.lbMyanmar = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Myanmar', padx=2, pady=2 , bg="white")
        self.lbMyanmar.grid(row=4, column=0, sticky='w')
        self.txtMyanmar = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Myanmar, width=28 , bg="white")
        self.txtMyanmar.grid(row=4, column=1)

        #row 2
        self.lbEnglish = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='English', padx=2, pady=2 , bg="white")
        self.lbEnglish.grid(row=5, column=0, sticky='w')
        self.txtEnglish = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.English, width=28 , bg="white")
        self.txtEnglish.grid(row=5, column=1)

        #row 3
        self.lbMath = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Math ', padx=2, pady=2 , bg="white")
        self.lbMath.grid(row=6, column=0, sticky='w')
        self.txtMath = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Math, width=28 , bg="white")
        self.txtMath.grid(row=6, column=1)

        #row 4
        self.lbPhysics = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Physics', padx=2, pady=2 , bg="white")
        self.lbPhysics.grid(row=7, column=0, sticky='w')
        self.txtPhysics = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Physics, width=28 , bg="white") 
        self.txtPhysics.grid(row=7, column=1)

        #row 5
        self.lblChemistry = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Chemistry', padx=2, pady=2 , bg="white")
        self.lblChemistry.grid(row=8, column=0, sticky='w')
        self.txtChemistry = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Chemistry, width=28 , bg="white")
        self.txtChemistry.grid(row=8, column=1)

        #row 6
        self.lblBiology = Label(self.MainFrame, font=('Arial', 14, 'bold'), text='Biology', padx=2, pady=2 , bg="white")
        self.lblBiology.grid(row=9, column=0, sticky='w')
        self.txtBiology = Entry(self.MainFrame, font=('Arial', 14, 'bold'), textvariable=self.Biology, width=28 , bg="white")
        self.txtBiology.grid(row=9, column=1)

        ##button
        

        self.btnUpdate = Button(self.MainFrame, text='Update Student Mark', font=('Arial', 12, 'bold'), height=1, width=16,  bg="#4CAF50", fg="white", bd=2, padx=13, command=self.update_student)
        self.btnUpdate.grid(row=14, column=0)

        self.btnUpdate = Button(self.MainFrame, text='Search Student Mark', font=('Arial', 12, 'bold'), height=1, width=16, bg="#2196F3", fg="white", bd=2, padx=13, command=self.search_student)
        self.btnUpdate.grid(row=14, column=1)

        self.btnHome = Button(self.MainFrame, text='Home', font=('Arial', 12, 'bold'), height=1, width=16, bg="#FFC107", fg="black", bd=2, padx=23, command=self.Home)
        self.btnHome.grid(row=14, column=2)

        self.btnExit = Button(self.MainFrame, text='Exit', font=('Arial', 12, 'bold'), height=1, bg="#F44336", fg="white", width=16, bd=2, padx=13, command=self.Exit)
        self.btnExit.grid(row=14, column=3,sticky='w')

    def update_student(self):
        try:
            # First, find the StudentId based on RollNo and Name
            query = "SELECT Student_Id FROM Student WHERE RollNo = %s AND StudentName = %s"
            self.mycursor.execute(query, (self.RollNo.get(), self.Name.get()))
            result = self.mycursor.fetchone()
            if result:
                student_id = result[0]
                print(student_id)
                # SQL update query
                query = """
                UPDATE Student_Mark 
                SET RollNo= %s , Name= %s, Myanmar = %s, English = %s, Math = %s, Physics = %s, Chemistry = %s, Biology = %s
                WHERE Student_Id = %s
                """
                # Execute the query with parameters
                self.mycursor.execute(query, (self.RollNo.get(),self.Name.get(),self.Myanmar.get(), self.English.get(), self.Math.get(), self.Physics.get(), self.Chemistry.get(), self.Biology.get(), student_id))
                # Commit the transaction
                self.mydb.commit()
                messagebox.showinfo("Success", "Student record updated successfully!")
            else:
                messagebox.showerror("Error", "Student not found!")
        except mysql.connector.Error as err:
            # Handle any potential MySQL errors
            messagebox.showerror("Error", f"Error updating student record: {err}")

    def search_student(self):
         # Get the roll number entered by the user for searching
        roll_to_search = self.RollNo.get()
        name_to_search=self.Name.get()
        # Write your SQL query to fetch student details based on the roll number
        query = "SELECT * FROM Student_Mark WHERE RollNo = %s and Name= %s"
        self.mycursor.execute(query, (roll_to_search,name_to_search))
        studentMark = self.mycursor.fetchone()

        # Populate the Entry fields with the fetched student details
        if studentMark:
            # Display the roll number
            self.RollNo.set(studentMark[0])
            self.Name.set(studentMark[1])
            # Set the fetched student details to the respective variables or directly to Entry widgets
            self.Myanmar.set(studentMark[2])
            self.English.set(studentMark[3])
            self.Math.set(studentMark[4])
            self.Physics.set(studentMark[5])
            self.Chemistry.set(studentMark[6])
            self.Biology.set(studentMark[7])
            
        else:
            messagebox.showerror("Error", "Student not found")

    def Home(self):
        from AddMark_Student_page import AddMark
        AddWindow = Toplevel(self.root)
        AddMark(AddWindow)

    def Exit(self):
        self.root.destroy()

    

if __name__ == "__main__":
    root = Tk()
    application = UpdateMark(root)
    root.mainloop()
