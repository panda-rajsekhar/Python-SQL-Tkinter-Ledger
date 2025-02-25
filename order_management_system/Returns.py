from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
def main():
    win = Tk()
    app = Returns(win)
    win.mainloop()



class Returns:
    print(" R stage 1 Working")
    def __init__(self,root):
        self.root=root
        self.root.title("Returns")# giving title
        self.root.geometry("1920x1080+0+0")

        # DEclaring the variables  

        self.var_ref = StringVar()
        self.var_name    =  StringVar()      
        self.var_num=  StringVar()
        self.var_mail=  StringVar()
        self.var_pin=  StringVar()
        self.var_addr=  StringVar()
        self.var_product=  StringVar()
        self.var_price  =  StringVar()
        self.var_rsn=  StringVar()



        label = Label(root, text="Returned Orders",font=("century gothic",40 ), fg  = "Black")
        label.place(x = 550,y= 0 )


        ##Costomer info ##
        labelframeleft = LabelFrame(self.root,bd = 5, relief  =  RIDGE, text = " Customer Details : ",font = ("century gothic",18,"bold"))
        labelframeleft.place(x = 2,y = 5,width = 420 ,height = 800)

        # Label and entry
        #reference Id: 
        lbl_Cust_Ref = Label(labelframeleft, text = "Date(yyyy.mm.dd)",font =("century gothic",18),padx = 2,pady = 6)
        lbl_Cust_Ref.grid(row = 0, column = 0, sticky = W)

        entry_ref = ttk.Entry(labelframeleft,textvariable = self.var_ref,width = 29,font = ("Consolas",18))
        entry_ref.grid(row = 1, column = 0)

        # name 
        cname = Label(labelframeleft, text = "Full Name:",font =("century gothic",18),padx = 2,pady = 6)
        cname.grid(row = 2, column = 0, sticky = W)

        txtcname = ttk.Entry(labelframeleft,textvariable = self.var_name,width = 29,font = ("Consolas",18))
        txtcname.grid(row = 3, column = 0)

        # number
        cnum = Label(labelframeleft, text = "Mobile Number:",font =("century gothic",18),padx = 2,pady = 6)
        cnum.grid(row = 4, column = 0, sticky = W)

        txtcnum = ttk.Entry(labelframeleft,textvariable = self.var_num,width = 29,font = ("Consolas",18))
        txtcnum.grid(row = 5, column = 0)

        #mail 
        cmail = Label(labelframeleft, text = " Mail Id:",font =("century gothic",18),padx = 2,pady = 6)
        cmail.grid(row = 6, column = 0, sticky = W)

        txtcmail = ttk.Entry(labelframeleft,textvariable = self.var_mail,width = 29,font = ("Consolas",18))
        txtcmail.grid(row = 7, column = 0)

        #Pincode
        cpin = Label(labelframeleft, text = "Pincode :",font =("century gothic",18),padx = 2,pady = 6)
        cpin.grid(row = 8, column = 0, sticky = W)

        txtcpin = ttk.Entry(labelframeleft,textvariable = self.var_pin,width = 29,font = ("Consolas",18))
        txtcpin.grid(row = 9, column = 0)

        #Full Add

        caddr = Label(labelframeleft, text = "Address:",font =("century gothic",18),padx = 2,pady = 6)
        caddr.grid(row = 10, column = 0, sticky = W)

        txtcaddr = ttk.Entry(labelframeleft,textvariable = self.var_addr,width = 29,font = ("Consolas",18))
        txtcaddr.grid(row = 11, column = 0)

        #Order 
        cproduct = Label(labelframeleft, text = "Product :",font =("century gothic",18),padx = 2,pady = 6)
        cproduct.grid(row = 12, column = 0, sticky = W)

        txtcproduct = ttk.Entry(labelframeleft,textvariable  = self.var_product,width = 29,font = ("Consolas",18))
        txtcproduct.grid(row = 13, column =0)

        #Price
        cprice = Label(labelframeleft, text = "Price:",font =("century gothic",18),padx = 2,pady = 6)
        cprice.grid(row = 14, column = 0, sticky = W)

        txtcprice = ttk.Entry(labelframeleft,textvariable = self.var_price,width = 29,font = ("Consolas",18))
        txtcprice.grid(row = 15, column = 0)

        #reason
        crsn  = Label(labelframeleft, text = "Reason:",font =("century gothic",18),padx = 2,pady = 6)
        crsn.grid(row = 16, column = 0, sticky = W)

        txtcprice = ttk.Entry(labelframeleft,textvariable = self.var_rsn,width = 29,font = ("Consolas",18))
        txtcprice.grid(row = 17, column = 0)


        print("R stage 2 Working")
       
        #-------Buttons----------# 

        btnADD = Button(labelframeleft,command = self.add_data,  text = "Add",font = ("Arial",11,"bold"),bg = "black",fg = "gold", width = 10)
        btnADD.place(x = 50, y = 725)
        btnADD = Button(labelframeleft,command = self.reset,  text = "Reset",font = ("Arial",11,"bold"),bg = "black",fg = "gold", width = 10)
        btnADD.place(x = 180, y = 725)

        
        # Making the tableframe 
        Table_frm = LabelFrame(self.root, bd = 2, relief=  RIDGE, text=  "View Details and Search System:",font = ("century gothic",16,"bold"),padx = 2)
        Table_frm.place(x = 455,y =90,height = 700, width  = 1050)       



        #======================================Show table ================================================#
        details_table = Frame(Table_frm,bd = 2,relief = RIDGE)
        details_table.place(x = 0, y = 60, height = 570, width = 1040)

        scroll_x  = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y  = ttk.Scrollbar(details_table, orient = VERTICAL)


        self.Cust_Details_Table = ttk.Treeview(details_table,column = ( "ref","name","num","mail","pin","addr","product","price","rsn"),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config( command = self.Cust_Details_Table.xview)
        scroll_y.config( command = self.Cust_Details_Table.yview)



        self.Cust_Details_Table.heading("ref", text = "Order Id")
        self.Cust_Details_Table.heading("name", text = "Name")
        self.Cust_Details_Table.heading("num", text ="Mobile Number")
        self.Cust_Details_Table.heading("mail", text ="Mail Id")
        self.Cust_Details_Table.heading("pin", text ="Pincode")
        self.Cust_Details_Table.heading("addr", text ="Address")
        self.Cust_Details_Table.heading("product", text ="Product")
        self.Cust_Details_Table.heading("price", text ="Price")
        self.Cust_Details_Table.heading("rsn", text = "Reason")

        self.Cust_Details_Table["show"] = "headings"



        self.Cust_Details_Table.column("ref",        width = 200           )
        self.Cust_Details_Table.column("name",       width = 200           )
        self.Cust_Details_Table.column("num",        width = 200           )
        self.Cust_Details_Table.column("mail",       width = 200           )
        self.Cust_Details_Table.column("pin",        width = 200           )
        self.Cust_Details_Table.column("addr",       width = 200           )
        self.Cust_Details_Table.column("product",    width = 200           )
        self.Cust_Details_Table.column("price",      width = 200           )
        self.Cust_Details_Table.column("rsn",        width = 200           )

        self.Cust_Details_Table.pack(fill = BOTH , expand = 1 )
        self.fetch_data()
        print("R stage 3 Working")

    def add_data(self):
        if self.var_num.get()=="":
            messagebox.showerror("Error", "Mobile Number Is Required")

        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="rspanda",database ="management_01")
                my_cursor = conn.cursor() 
                my_cursor.execute("insert into returns values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                 self.var_ref.get(),
                                                 self.var_name.get(),         
                                                 self.var_num.get(),      
                                                 self.var_mail.get(),     
                                                 self.var_pin.get(),      
                                                 self.var_addr.get(),     
                                                 self.var_product.get(), 
                                                 self.var_price.get(),
                                                 self.var_rsn.get()   
                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Data has been Successfully inserted",parent = self.root)
            except Exception as es:
                messagebox.showwarning("Warning ", f"Something went wrong : {str(es)}")


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="rspanda",database ="management_01")
        my_cursor = conn.cursor()
        my_cursor.execute("select *  from  returns ")
        rows  = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values = i)
            conn.commit() 
        conn.close() 

    def reset(self):
        self.var_ref = StringVar()
        self.var_name.set(" ")
        self.var_num.set(" ")
        self.var_mail.set(" ")
        self.var_addr.set(" ")
        self.var_product.set(" ")
        self.var_price.set(" ")

print ("R stage 4 Working")


if __name__=="__main__":
    main()   