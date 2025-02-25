from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from Order_Management import Order_Management
from PIL import Image, ImageTk

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

#making the widget of the loginn Window

class Login_Window:#widget for login window
    print("LW Stage 1 Working")

    def __init__(self,root):
        self.root=root
        self.root.title("Login")#displays title
        self.root.geometry("2400x1850+0+0")#specifies the width and height of the window
        
        #Adding the background in the window

        self.bg=ImageTk.PhotoImage(file= "jacques-dillies-jcav1COVvOc-unsplash.jpg")
        lbl_bg= Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)#place is used to shove the conten ton screen of window

        #maing the login window frame:

        frame = Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=500)

        # providing the user image icon

        img1 = Image.open(r"user.png")# r is to read
        img1 = img1.resize((100,100),Image.ANTIALIAS)#Anti-aliasing is the smoothing of jagged edges in digital images by averaging the colors of the pixels at a boundary
        self.photoimage =ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage,bg="White",borderwidth=0)
        lblimg1.place(x =730,y=180,width=100,height=100)
        Usr_lin= Label(frame,text="USER LOGIN",font=("century gothic",30),fg="black",bg="white")
        Usr_lin.place(x= 50,y=120)      

        # Lable for the user name  and password
        username =  lbl= Label(frame,text="Seller-Id:",font=("century gothic",17,"bold"),fg="black",bg="white")
        username.place(x=40,y=195 )

        self.txtuser=ttk.Entry(frame,font=("consolas",17,))
        self.txtuser.place(x=40,y = 225,width=270 )

        password =  lbl= Label(frame,text="Password:",font=("century gothic",17,"bold"),fg="black",bg="white")
        password.place(x=40,y=265 )
        
        self.txtpass=ttk.Entry(frame,font=("consolas",17,))
        self.txtpass.place(x=40,y = 300,width=270 )

        #---------LOGIN BUTTON---------------#
        loginbtn = Button(frame,command=self.login,text="LOGIN",font=("century gothic",16,"bold"),bd=3,relief= RIDGE,fg="white",bg="#F70D1A")
        loginbtn.place(x=110,y=360,width=120,height=50 )

        print("LW Stage 2 Working")

        #---------SIGN-IN|REGISTER BUTTON---------------#
        """

        loginbtn = Button(frame,text="REGISTER",command=self.register_window,font=("century gothic",16,"bold"),bd=3,relief= RIDGE,fg="white",bg="#F70D1A")
        loginbtn.place(x= 190,y=360,width=120,height=50 ) 


        # remenber : If usng the register and the forget password button then i have to realign it  

        #---------------FORGET PASSWORD BUTTON-------------------#"""

        """"forgetpaswd = Button(frame,text="Forgot Password?",font=("century gothic",10,"bold"),borderwidth=0,relief= RIDGE,fg="blue",bg="white")
        forgetpaswd.place(x=110,y=420 )"""


 #---------------Function for Login Button----------------#

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            if self.txtuser.get()== "order_management" and self.txtpass.get()=="0987654321" :
                self.new_window = Toplevel(self.root)
                self.app = Order_Management(self.new_window)
            else:
                messagebox.showerror("Error ","Use Correct Seller-Id and Password")



    """ the user id : order_management 
        the password : 0987654321
    """
 

if __name__=="__main__":
    main() 




