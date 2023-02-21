from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


class Add:
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

        # #Frame with border=2 and bg=white
        # main_frame = Frame(bd=2,bg="white")
        # main_frame.place(x=5,y=80,width=700,height=620)

        #Name of Student        
        label_3 =Label(self.root,text="Enter Name", width=30,height=2,font=("verdana",12,"bold"),fg="lightgreen",bg="white")
        label_3.place(x=168,y=131)
        entry_1=Entry(self.root,textvariable=self.name,width=53)
        entry_1.place(x=168,y=182)

        # E-Mail
        label_3 =Label(self.root,text="Enter E-Mail", width=30,height=2,font=("verdana",12,"bold"),fg="lightgreen",bg="white")
        label_3.place(x=168,y=230)
        entry_1=Entry(self.root,textvariable=self.email,width=53)
        entry_1.place(x=168,y=282)

        button_frame1 = Frame(bd=2,bg="white")
        button_frame1.place(x=170,y=400,width=700,height=620)
       

        #take image button
        take_img=Button(button_frame1,text="Take Picture",width=10,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        take_img.grid(row=0,column=1,padx=5,pady=8)

        #save button
        save_btn=Button(button_frame1,text="Save",command = self.add_data,width=7,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        save_btn.grid(row=1,column=2,padx=5,pady=8)


    def add_data(self):
        if  self.name.get()=="" or self.email.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                

                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=Add(root)
    root.mainloop()