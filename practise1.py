from tkinter import*
root=Tk()
root.geometry("800x800")
label=Label(text="Welcome to Tauinfo")
label.pack()
photo=PhotoImage(file="R.png")
label2=Label(image=photo)
label2.pack()



root.mainloop()