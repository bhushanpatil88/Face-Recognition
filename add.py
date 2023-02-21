from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from mongo_connect import get_database

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
            img = ImageTk.PhotoImage(file=filename)
            # img = cv2.resize(img, (200, 200))
            b2 =  Button(self.root,image=img) # using Button 
            b2.place(x=300,y=450)
    

        #save button
        save_btn=Button(self.root,text="Save",command = self.add_data,width=7,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        save_btn.place(x=300,y=400)


    def add_data(self):
        if  self.name.get()=="" or self.email.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                dbname = get_database()
                collection_name = dbname["user_faces"]  

                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=Add(root)
    root.mainloop()