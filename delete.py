
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk

class Delete:
    def __init__(self,root):
        self.root=root
        # set the window
        self.root.geometry("700x700+0+0")
        self.root.title("Face_Recogonition_System")

        
        #take image button
        b1 = Button(self.root, text='Delete Record',width=10,font=("verdana",12,"bold"),fg="white",bg="lightgreen")
        b1.place(x=180,y=330) 

        




if __name__ == "__main__":
    root=Tk()
    obj=Delete(root)
    root.mainloop()