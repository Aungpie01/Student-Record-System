from tkinter import *
from tkinter import messagebox,ttk
import mysql.connector
from add_informatin import Student

class AddMark:

    def __init__(self, root):
        self.root = root
        self.root.title('Add Mark Student')
        self.root.geometry('1760x480+0+0')
        
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
        self.MainFrame = Frame(self.root, bg='cadet blue')
        self.MainFrame.grid()

        

        DataFrame2=Frame(self.MainFrame,bd=1,width=1300,height=400,padx=20,pady=20, bg='cadet blue')
        DataFrame2.pack(side='bottom')

        # ListFrame=Frame(DataFrame2,bd=2,width=1350,height=180,padx=18,pady=10,relief=RIDGE, bg='powder blue')
        # ListFrame.pack(side='top')

        ButtonFrame=Frame(DataFrame2,bd=2,width=1350,height=40,padx=18,pady=10, bg='cadet blue')
        ButtonFrame.pack(side='bottom')

        DataFrame=Frame(self.MainFrame,bd=1,width=1500,height=900,padx=20,pady=20, bg='cadet blue')
        DataFrame.pack(side='top')

        DataFrameLeft=LabelFrame(DataFrame,bd=1,width=500,height=500,padx=2, bg='cadet blue',font=('Arial',20,'bold'),text='Student Add Mark\n')
        DataFrameLeft.pack(side='left')

        self.DataFrameRight=LabelFrame(DataFrame,bd=1,width=900,height=400,padx=31,pady=8, bg='powder blue',font=('Arial',20,'bold'),text='All Students Mark\n')
        self.DataFrameRight.pack(side='right')

        # # Title
        # # Title
        # self.lblTitle = Label(self.MainFrame, font=('Arial', 20, 'bold'), text='Student Add Mark Form', padx=2, pady=2, bg="white")
        # self.lblTitle.grid(row=0, column=0, columnspan=5, pady=(0, 20))


        sql="select RollNo,Name,Myanmar,English,Math,Physics,Chemistry,Biology from Student_Mark"
        self.mycursor.execute(sql)
        r_set=self.mycursor.fetchall()
        trv=ttk.Treeview(self.DataFrameRight,selectmode='browse')
        trv.grid(row=1,column=1,padx=20,pady=20)
        trv['columns']=('1','2','3','4','5','6','7','8')
        trv['show']='headings'
        trv.column('1',width=80,anchor='c')
        trv.column('2',width=130,anchor='c')
        trv.column('3',width=100,anchor='c')
        trv.column('4',width=100,anchor='c')
        trv.column('5',width=130,anchor='c')
        trv.column('6',width=130,anchor='c')
        trv.column('7',width=130,anchor='c')
        trv.column('8',width=130,anchor='c')
        trv.heading('1',text='Roll No')
        trv.heading('2',text='Name')
        trv.heading('3',text='Myanmar')
        trv.heading('4',text='English')
        trv.heading('5',text='Math')
        trv.heading('6',text='Physics')
        trv.heading('7',text='Chemistry')
        trv.heading('8',text='Biology')
        for dt in r_set:
            trv.insert('','end',values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
        
        ##########################Widget...........
        self.rollS = Label(DataFrameLeft, font=('Arial', 14, 'bold'), text=' Enter Roll No That You Want To Add Mark', padx=5, pady=3 , bg="cadet blue")
        self.rollS.grid(row=2, column=0, sticky='w')
        self.txtSearchroll = Entry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.RollNo, width=30)
        self.txtSearchroll.grid(row=2, column=1)

        self.lbName = Label(DataFrameLeft, font=('Arial', 14, 'bold'), text='Name', padx=5, pady=3 , bg="cadet blue")
        self.lbName.grid(row=3, column=0, sticky='w')
        self.txtName = Entry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.Name, width=30)
        self.txtName.grid(row=3, column=1)

        #row 1
        self.lbMyanmar = Label(DataFrameLeft, font=('Arial', 14, 'bold'), text='Myanmar', padx=5, pady=3 , bg="cadet blue")
        self.lbMyanmar.grid(row=4, column=0, sticky='w')
        self.txtMyanmar = Entry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.Myanmar, width=30)
        self.txtMyanmar.grid(row=4, column=1)

        #row 2
        self.lbEnglish = Label(DataFrameLeft, font=('Arial', 14, 'bold'), text='English', padx=5, pady=3 , bg="cadet blue")
        self.lbEnglish.grid(row=5, column=0, sticky='w')
        self.txtEnglish = Entry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.English, width=30)
        self.txtEnglish.grid(row=5, column=1)

        #row 3
        self.lbMath = Label(DataFrameLeft, font=('Arial', 14, 'bold'), text='Math ', padx=5, pady=3 , bg="cadet blue")
        self.lbMath.grid(row=6, column=0, sticky='w')
        self.txtMath = Entry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.Math, width=30)
        self.txtMath.grid(row=6, column=1)

        #row 4
        self.lbPhysics = Label(DataFrameLeft, font=('Arial', 14, 'bold'), text='Physics', padx=5, pady=3 , bg="cadet blue")
        self.lbPhysics.grid(row=7, column=0, sticky='w')
        self.txtPhysics = Entry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.Physics, width=30)
        self.txtPhysics.grid(row=7, column=1)

        #row 5
        self.lblChemistry = Label(DataFrameLeft, font=('Arial', 14, 'bold'), text='Chemistry', padx=5, pady=3 , bg="cadet blue")
        self.lblChemistry.grid(row=8, column=0, sticky='w')
        self.txtChemistry = Entry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.Chemistry, width=30)
        self.txtChemistry.grid(row=8, column=1)

        #row 6
        self.lblBiology = Label(DataFrameLeft, font=('Arial', 14, 'bold'), text='Biology', padx=5, pady=3 , bg="cadet blue")
        self.lblBiology.grid(row=9, column=0, sticky='w')
        self.txtBiology = Entry(DataFrameLeft, font=('Arial', 14, 'bold'), textvariable=self.Biology, width=30)
        self.txtBiology.grid(row=9, column=1)

        ##button
        self.btnInsert = Button(ButtonFrame, text='Add Mark', font=('Arial', 12, 'bold'), height=1, width=16, bd=2, bg="#4CAF50", padx=20,fg="white", command=self.insert_student)
        self.btnInsert.grid(row=12, column=0)

        self.btnSearch = Button(ButtonFrame, text='Search Student Mark', font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=20, bg="#2196F3", fg="white", command=self.search_student)
        self.btnSearch.grid(row=12, column=1)

        self.btnUpdate = Button(ButtonFrame, text='Update Student Mark', font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=20, bg="#FFC107", fg="black", command=self.update_student)
        self.btnUpdate.grid(row=12, column=2)

        self.btnDelete = Button(ButtonFrame, text='Delete Student Mark', font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=20, bg="#F44336", fg="white", command=self.delete_student)
        self.btnDelete.grid(row=12, column=3)

        self.btnGPA = Button(ButtonFrame, text='Calculate GPA', font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=20, bg="#9C27B0", fg="white", command=self.gpa)
        self.btnGPA.grid(row=12, column=4)

        self.btnHome = Button(ButtonFrame, text='Home', font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=20, bg="#607D8B", fg="white", command=self.Home)
        self.btnHome.grid(row=12, column=5)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('Arial', 12, 'bold'), height=1, width=16, bd=2, padx=13, bg="#795548", fg="white", command=self.Exit)
        self.btnExit.grid(row=12, column=6)

    def insert_student(self):
        try:
            # First, find the StudentId based on RollNo and Name
            query = "SELECT Student_Id FROM Student WHERE RollNo = %s AND StudentName = %s"
            self.mycursor.execute(query, (self.RollNo.get(), self.Name.get()))
            result = self.mycursor.fetchone()
            if result:
                student_id = result[0]
                print(student_id)
                # SQL insert query
                query = "INSERT INTO Student_Mark (RollNo,Name, Myanmar, English, Math, Physics, Chemistry, Biology,Student_Id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                # Execute the query with parameters
                self.mycursor.execute(query, (self.RollNo.get(),self.Name.get(), self.Myanmar.get(), self.English.get(), self.Math.get(), self.Physics.get(), self.Chemistry.get(), self.Biology.get(),student_id))
                # Commit the transaction
                self.mydb.commit()

                sql="select RollNo,Name,Myanmar,English,Math,Physics,Chemistry,Biology from Student_Mark"
                self.mycursor.execute(sql)
                r_set=self.mycursor.fetchall()
                trv=ttk.Treeview(self.DataFrameRight,selectmode='browse')
                trv.grid(row=1,column=1,padx=20,pady=20)
                trv['columns']=('1','2','3','4','5','6','7','8')
                trv['show']='headings'
                trv.column('1',width=80,anchor='c')
                trv.column('2',width=130,anchor='c')
                trv.column('3',width=100,anchor='c')
                trv.column('4',width=100,anchor='c')
                trv.column('5',width=130,anchor='c')
                trv.column('6',width=130,anchor='c')
                trv.column('7',width=130,anchor='c')
                trv.column('8',width=130,anchor='c')
                trv.heading('1',text='Roll No')
                trv.heading('2',text='Name')
                trv.heading('3',text='Myanmar')
                trv.heading('4',text='English')
                trv.heading('5',text='Math')
                trv.heading('6',text='Physics')
                trv.heading('7',text='Chemistry')
                trv.heading('8',text='Biology')
                for dt in r_set:
                    trv.insert('','end',values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
                # Show success messagebox
                messagebox.showinfo("Success", "Student record added successfully!")
            else:
                messagebox.showerror("Error", "Student not found!")
        except mysql.connector.Error as err:
            # Handle any potential MySQL errors
            messagebox.showerror("Error", f"Error: {err}")

    def search_student(self):
        from Search_Mark import SearchMark
        HomeWindow = Toplevel(self.root)
        SearchMark(HomeWindow)

    def Home(self):
        HomeWindow = Toplevel(self.root)
        Student(HomeWindow)

    def update_student(self):
        from Update_Mark_page import UpdateMark
        HomeWindow = Toplevel(self.root)
        UpdateMark(HomeWindow)

    def delete_student(self):
        from delete_Student_Mark import DeleteStudentMark
        HomeWindow = Toplevel(self.root)
        DeleteStudentMark(HomeWindow)

    def Exit(self):
        self.root.destroy()
    
    def gpa(self):
        from GPA_Student import GPA
        HomeWindow = Toplevel(self.root)
        GPA(HomeWindow)

    

if __name__ == "__main__":
    root = Tk()
    application = AddMark(root)
    root.mainloop()
