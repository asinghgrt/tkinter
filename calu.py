from tkinter import*;
root=Tk()
root.geometry("500x500")
#adding title to our ui
root.title("% calcualtor")
#addind background image
photo=PhotoImage(file="imagess.png")

label=Label(root,image=photo,width=100,height=100)
label.pack()
root.mainloop()