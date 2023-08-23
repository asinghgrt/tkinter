from tkinter import*
root=Tk()
def get():
    label1=Label(root,text="Hello how are you!")
    label1.pack()
mybutton=Button(root,text="Click me!",borderwidth=10,fg="red",bg="navyblue",command=get)
mybutton.pack()
root.mainloop()
