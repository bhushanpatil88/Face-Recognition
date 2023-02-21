from tkinter import*
from tkinter import ttk
from tkinter import messagebox
# from train import Train
from PIL import Image,ImageTk
# from student import Student
# # from train import Train
# from face_recognition import Face_Recognition
# from attendance import Attendance
# from developer import Developer
# import os
# from helpsupport import Helpsupport

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        # set the window
        self.root.geometry("700x700+0+0")
        self.root.title("Face_Recogonition_System")


        self.name=StringVar()
        self.email=StringVar()


        #title section
        title = Label(text="Face Recognition System",font=("verdana",30,"bold"),bg="lightblue",fg="navyblue")
        title.place(x=0,y=0,width=700,height=80)

        #Frame with border=2 and bg=white
        main_frame = Frame(bd=2,bg="white")
        main_frame.place(x=5,y=80,width=700,height=620)

        #Name of Student        
        label_3 =Label(main_frame,text="Enter Name", width=30,height=2,font=("verdana",12,"bold"),fg="lightgreen",bg="white")
        label_3.place(x=168,y=131)
        entry_1=Entry(main_frame,textvariable=self.name,width=53)
        entry_1.place(x=168,y=182)

        # E-Mail
        label_3 =Label(main_frame,text="Enter E-Mail", width=30,height=2,font=("verdana",12,"bold"),fg="lightgreen",bg="white")
        label_3.place(x=168,y=230)
        entry_1=Entry(main_frame,textvariable=self.email,width=53)
        entry_1.place(x=168,y=282)

        button_frame1 = Frame(bd=2,bg="white")
        button_frame1.place(x=170,y=400,width=700,height=620)
       

        #take image button
        take_img=Button(button_frame1,text="Take Picture",width=10,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        take_img.grid(row=0,column=1,padx=5,pady=8)

        #save button
        save_btn=Button(button_frame1,text="Save",command = self.add_data,width=7,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        save_btn.grid(row=1,column=2,padx=5,pady=8)

        #delete button
        del_btn=Button(button_frame1,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        del_btn.grid(row=3,column=1,padx=5,pady=10)

        #reset button
        reset_btn=Button(button_frame1,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        reset_btn.grid(row=3,column=2,padx=5,pady=10)

        #update photo button
        update_photo_btn=Button(button_frame1,text="Update Img",width=9,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        update_photo_btn.grid(row=3,column=3,padx=5,pady=10)
        
        
    def add_data(self):
        if  self.name.get()=="" or self.email.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_id.get(),
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
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


      

       
# # ==================Funtion for Open Images Folder==================
#     def open_img(self):
#         os.startfile("dataset")
# # ==================Functions Buttons=====================
#     def student_pannels(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Student(self.new_window)

#     def train_pannels(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Train(self.new_window)
    
#     def face_rec(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Face_Recognition(self.new_window)
    
#     def attendance_pannel(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Attendance(self.new_window)
    
#     def developr(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Developer(self.new_window)
    
#     def helpSupport(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Helpsupport(self.new_window)

#     def Close(self):
#         root.destroy()
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()