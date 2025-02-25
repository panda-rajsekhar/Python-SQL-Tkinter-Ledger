from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import random

def main():
    win = Tk()
    app = Customer_Info(win)
    win.mainloop()


class Customer_Info:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Details")
        self.root.geometry("1920x1080+0+0")
        print("CI Stage 1 Working")


        label = Label(root, text="Customer Details",font=("century gothic",43 ),fg  = "black", bg = "white", width = 45)
        label.place(x = 0,y= 0 )


       
        # Making the tableframe 
        Table_frm = LabelFrame(self.root, bd = 10, relief=  RIDGE, text=  " View Details : ",font = ("century gothic",16,"bold"),padx = 2)
        Table_frm.place(x = 2,y =90,height = 700, width  = 1530)


        print(" CIStage 2 Working")


        #---------show table----------------#
        details_table = Frame(Table_frm,bd = 3,relief = RIDGE)
        details_table.place(x = 0, y = 50, height = 610, width = 1510)

        scroll_x  = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y  = ttk.Scrollbar(details_table, orient = VERTICAL)


        self.Cust_Details_Table = ttk.Treeview(details_table,column = ( "ref","name","num","mail","pin","addr","product","price"),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
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

        self.Cust_Details_Table["show"] = "headings"



        self.Cust_Details_Table.column("ref",        width = 200           )
        self.Cust_Details_Table.column("name",       width = 200           )
        self.Cust_Details_Table.column("num",        width = 200           )
        self.Cust_Details_Table.column("mail",       width = 200           )
        self.Cust_Details_Table.column("pin",        width = 200           )
        self.Cust_Details_Table.column("addr",       width = 200           )
        self.Cust_Details_Table.column("product",    width = 200           )
        self.Cust_Details_Table.column("price",      width = 200           )


        self.Cust_Details_Table.pack(fill = BOTH , expand = 1 )
        
        self.fetch_data()

    print("CI Stage 3 Working")

    def add_data(self):
        if self.var_num.get()=="":
            messagebox.showerror("Error", "Mobile Number Is Required")

        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="rspanda",database ="management_01")
                my_cursor = conn.cursor() 
                my_cursor.execute("insert into todays values(%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                 self.var_ref.get(),
                                                 self.var_name.get(),         
                                                 self.var_num.get(),      
                                                 self.var_mail.get(),     
                                                 self.var_pin.get(),      
                                                 self.var_addr.get(),     
                                                 self.var_product.get(), 
                                                 self.var_price.get()   
                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Data has been Successfully inserted",)
            except Exception as es:
                messagebox.showwarning("Warning ", f"Something went wrong : {str(es)}")


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="rspanda",database ="management_01")
        my_cursor = conn.cursor()
        my_cursor.execute("select *  from  todays ")
        rows  = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values = i)
            conn.commit() 
        conn.close() 

    print(" CI Stage 4 Working")




    
if __name__=="__main__":
    main()   