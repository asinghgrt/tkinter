from tkinter import*
root=Tk()

root.geometry("700x450")
#root.maxsize(700,450)
root.minsize(700,450)
label1=Label(text="Welcome to pyecharm!")
label1.pack()
photo=PhotoImage(file="imagess.png")
label2=Label(image=photo)
label2.pack()
root.mainloop()