from tkinter import*
root=Tk()
root.geometry("500x500")
myinput=Entry(root,borderwidth=5,fg="blue",bg="violet",width=100)
myinput.pack()
#myinput.insert(0,"Enter name:")
def geto():
    label1=Label(root,text="Hello "+myinput.get()+ " how are you!")
    label1.pack()
mybutton=Button(root,text="Click me!",borderwidth=10,fg="red",bg="navyblue",command=geto)
mybutton.pack()

root.mainloop()