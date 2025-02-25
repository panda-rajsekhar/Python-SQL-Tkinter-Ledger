from tkinter import*
from PIL import Image, ImageTk
from Todays import Todays_Ord
from Returns import Returns
from Customer_Info import Customer_Info
def main():
    win = Tk()
    app = Order_Management(win)
    win.mainloop()


class Order_Management:#widget for the window
    print("OM Stage 1 Working")
    def __init__(self,root):
        
        self.root=root
        self.root.title("Order Management System")# giving title
        self.root.geometry("2400x1850+0+0")#giving the window height and width 

        #----Heading of the System-------#

        label = Label(root, text="Order Management Sytem",font=("century gothic",43 ), fg  = "gold", bg = "black", width = 45)
        label.place(x = 0,y= 0 )


        self.bg=ImageTk.PhotoImage(file= "undraw_empty_cart_co35_n.png")#backgroundimage 
        lbl_bg= Label(self.root,image=self.bg)
        lbl_bg.place(x=190,y=80,relwidth=1,relheight=1,height = -10)#

        frame = Frame(self.root,bg="White")
        frame.place(x=0,y=80,width=350,height=800)


        #-----------Making the label frame----------------#
        label_frame_left = LabelFrame(self.root,bd = 10, relief  =  RIDGE, font = ("century gothic",18,"bold"))
        label_frame_left.place(x = 0,y = 79,width = 425 ,height = 750)

        lbl0 = Label(label_frame_left, text = "नमस्ते!",font=("Arial",35))
        lbl0.place(x = 110, y = 35)     

        lbl1 = Label(label_frame_left, text = "Welcome to Order Management System",font=("century gothic",15),)
        lbl1.place(x = 1, y = 105)
        
        #Todays Sales
        label1 = Button(label_frame_left, text = " Sold/ Delivered",command = self.Todays_order,font=("century gothic",22),bd=3,relief= RIDGE,fg="white",bg="#F70D1A")
        label1.place(x = 40, y = 150)
        #returned Orders
        label4 = Button(label_frame_left, text = "Returns",command = self.Returns,font=("century gothic",22),bd=3,relief= RIDGE,fg="white",bg="#F70D1A")
        label4.place(x = 40, y = 300)

        #Customer Detalils \
        label69 = Button(label_frame_left, text = "Customer Details", command = self.Customer_Details,font=("century gothic",22),bd=3,relief= RIDGE,fg="white",bg="#F70D1A")
        label69.place(x = 40, y = 450)

    print("OM Stage 2 Working")

    #----------Defining Functions for the Buttons --------#
    def Todays_order(self):
        self.new_window  = Toplevel(self.root)
        self.app = Todays_Ord(self.new_window)
    
    def Returns(self):
        self.new_window = Toplevel(self.root)
        self.app = Returns(self.new_window)

    def Customer_Details(self):
         self.new_window = Toplevel(self.root)
         self.app = Customer_Info(self.new_window)



print("OM Stage 3 Working")



if __name__=="__main__":
    main()    
