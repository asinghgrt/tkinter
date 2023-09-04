from tkinter import*;

root=Tk()
root.title("Linear")
root.iconbitmap('favicon.ico')
my_image=PhotoImage(file="R.png",width="200")
mu=Label(image=my_image)
mu.grid(row=10)
#exitbutton
my_quit=Button(root,text="Exit",command=quit)
my_quit.grid(row=0,column=3)
root.mainloop()