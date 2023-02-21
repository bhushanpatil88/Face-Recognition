from tkinter import*
from tkinter import ttk
from tkinter import messagebox

from add import Add
from delete import Delete

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        
        # set the window
        self.root.geometry("700x700+0+0")
        self.root.title("Face_Recogonition_System")


        #title section
        title = Label(text="Face Recognition System",font=("verdana",30,"bold"),bg="lightblue",fg="navyblue")
        title.place(x=0,y=0,width=700,height=80)

        button_frame1 = Frame(bd=2,bg="white")
        button_frame1.place(x=0,y=80,width=700,height=620)

        # Add button
        add_btn=Button(button_frame1,command=self.Add_User, text="Add User",width=10,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        add_btn.grid(row=100,column=10,padx=20,pady=200)   

        #update photo button
        detect_face=Button(button_frame1,command=self.Detect_Face,text="Detect Face",width=10,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        detect_face.grid(row=100,column=20,padx=20,pady=200)     

        #delete button
        delete_user=Button(button_frame1,command=self.Delete_User,text="Delete User",width=10,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        delete_user.grid(row=100,column=30,padx=20,pady=200)

        #update photo button
        update_user=Button(button_frame1,command=self.Update_User,text="Update User",width=10,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        update_user.grid(row=100,column=40,padx=20,pady=200)
        
        
    


      
    def Add_User(self):
        self.new_window=Toplevel(self.root)
        self.app= Add(self.new_window)
    
    def Delete_User(self):
        self.new_window=Toplevel(self.root)
        self.app= Delete(self.new_window)
    
    def Update_User(self):
        self.new_window=Toplevel(self.root)
        self.app=Update(self.new_window)
    
    def Detect_Face(self):
        self.new_window=Toplevel(self.root)
        self.app=Detect(self.new_window)

    def Close(self):
        root.destroy()
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()