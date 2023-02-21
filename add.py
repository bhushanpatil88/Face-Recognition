from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

import mysql.connector
import cv2

conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()



class Add:
    def __init__(self,root):
        self.root=root

        # set the window
        self.root.geometry("700x700+0+0")
        self.root.title("Face_Recogonition_System")

        self.root.configure(bg='white')

        self.name=StringVar()
        self.email=StringVar()

        #title section
        title = Label(self.root,text="Face Recognition System",font=("verdana",30,"bold"),bg="lightblue",fg="navyblue")
        title.place(x=0,y=0,width=700,height=80)



        #Name of Student        
        label_3 =Label(self.root,text="Enter Name", width=30,height=2,font=("verdana",12,"bold"),fg="lightgreen",bg='white')
        label_3.place(x=168,y=131)
        entry_1=Entry(self.root,textvariable=self.name,width=53)
        entry_1.place(x=168,y=182)

        # E-Mail
        label_3 =Label(self.root,text="Enter E-Mail", width=30,height=2,font=("verdana",12,"bold"),fg="lightgreen",bg="white")
        label_3.place(x=168,y=230)
        entry_1=Entry(self.root,textvariable=self.email,width=53)
        entry_1.place(x=168,y=282)

 

        #take image button
        b1 = Button(self.root, text='Upload File',width=10,command = lambda:upload_file(),font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        b1.place(x=180,y=330) 

        def upload_file():  
            global img
            f_types = [('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img=Image.open(filename)
            img_resized=img.resize((200,200)) 
            img=ImageTk.PhotoImage(img_resized)
            b2 =  Button(self.root,image=img) 
            b2.place(x=250,y=450)
    

        #save button
        save_btn=Button(self.root,text="Save",command = self.add_data,width=7,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        save_btn.place(x=300,y=400)


    def add_data(self):
        if  self.name.get()=="" or self.email.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s)",(
                self.name.get(),
                self.email.get(),

                ))

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 





if __name__ == "__main__":
    root=Tk()
    obj=Add(root)
    root.mainloop()