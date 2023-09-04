from tkinter import*;
from tkinter import font;
import datetime;


root=Tk()
def age():
    date=datetime.datetime.now()
    current=Label(root,text=date,borderwidth=5,font=('algerian',15),fg="red")
    current.grid(row=4,column=2)
    
root.title("Current date and time")
root.iconbitmap('favicon.ico')
root.geometry("500x300")


root.minsize(500,300)
photo=PhotoImage(file="imagess.png")
label=Label(image=photo)
label.grid()
# head=Label(root,text="Age Finder!!!",font=('algerian', 20),anchor="center")

# head.grid(row=0)
# my_dob=Label(root,text="Enter your Date of Birth :",font=('hobo bd',15))
# my_dob.grid(row=1,column=0)
# enter=Entry(root,borderwidth=7)
# enter.grid(row=1,column=5)
mybutton=Button(root,text="Find Date and Time!",borderwidth=10,fg="blue",command=age,width=20)
mybutton.grid(row=3,column=5)
my_quit=Button(root,text="Quit",command=quit,borderwidth=10)
my_quit.grid(row=7,column=5)
root.mainloop()