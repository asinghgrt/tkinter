from tkinter import*;
root=Tk()

root.title("Currency Convertor")
root.geometry("700x500")
root.iconbitmap("favicon.ico")
root.configure(bg='#87CEEB')
Heading=Label(text="Convert Currency into Rupees or Rupees into any currecy",bg="Dark Gray",borderwidth=5,font=("algerian",15))
Heading.pack()
My_quit=Button(text="Quit",bg="Dark Gray",font=5,command=quit)
My_quit.pack(side="bottom",padx=1)
i=Entry(bg= '#F5F5DC',width=10,borderwidth=2)
i.insert(0,"Rupees")
i.pack()
def r_to_d():
    input=float(i.get())
    a=input/82.70
    label2=Label(text=a,bg="yellow",borderwidth=10,font=("roboto",12))
    label2.pack()
def r_to_e():
    input=float(i.get())
    a=input/89.31
    label2=Label(text=a,bg="yellow",borderwidth=10,font=("roboto",12))
    label2.pack()
def r_to_aed():
    input=float(i.get())
    a=input/22.52
    label2=Label(text=a,bg="yellow",borderwidth=10,font=("roboto",12))
    label2.pack()
def r_to_pound():
    input=float(i.get())
    a=input/144
    label2=Label(text=a,bg="yellow",borderwidth=10,font=("roboto",12))
    label2.pack()
def r_to_riyad():
    input=float(i.get())
    a=input/22.70
    label2=Label(text=a,bg="yellow",borderwidth=10,font=("roboto",12))
    label2.pack()
def r_to_takka():
    input=float(i.get())
    a=input/0.74
    label2=Label(text=a,bg="yellow",borderwidth=10,font=("roboto",12))
    label2.pack()
label=Label(text="",borderwidth=10,bg='#87CEEB')
label.pack()
b1=Button(text="convert into dollar",bg='#FFFFE0',width=20,command=r_to_d)
b1.pack()
b2=Button(text="convert into Euro",bg='#FFFFE0',width=20,command=r_to_e)
b2.pack()
b3=Button(text="convert into AEd",bg='#FFFFE0',width=20,command=r_to_aed)
b3.pack()
b4=Button(text="convert into pound",bg='#FFFFE0',width=20,command=r_to_pound)
b4.pack()
b5=Button(text="convert into Riyad",bg='#FFFFE0',width=20,command=r_to_riyad)
b5.pack()
b6=Button(text="convert into takka",bg='#FFFFE0',width=20,command=r_to_takka)
b6.pack()
root.mainloop()