from tkinter import*
root=Tk()
#gui logic here



#widthxheight
root.geometry("600x400")
#width,height

root.minsize(300,300)
#width,height

root.maxsize(1000,1000)
label=Label(text="This is Anurag's GUI")
label.pack()

root.mainloop()