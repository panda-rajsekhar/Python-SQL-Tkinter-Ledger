import customtkinter
from time import strftime
import datetime as dt

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1380x720+0+0")
#root.resizable(0,0

root.title('CTk-Clock')

def time():
    string = strftime('%H:%M:%S') # remove the :%S to remove the seconds funciton and save more power 
    mark.configure(text = string)
    mark.after(1000, time)


frame = customtkinter.CTkFrame(master = root,height=300)
#designed by rajsekhar panda
frame.pack(pady = 20, padx = 20,fill = "both",expand = True)



mark = customtkinter.CTkLabel(frame,font = ("rockwell nova ", 320,"bold"))
mark.pack()
time()
# Gets date from host computer.
date = dt.datetime.now()
# Takes the date and formats it.
format_date = f"{date:%a, %b %d %Y}"
# Add the date to the tkinter window
w = customtkinter.CTkLabel(frame, text=format_date,font=("rockwell nova", 60,"bold"))
w.pack()
root.mainloop()

