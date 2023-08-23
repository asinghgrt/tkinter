from tkinter import*
#from PIL import Image,_ImageTk
root=Tk()

root.geometry("1000x900")
photo=PhotoImage(file="imagess.png")
label=Label(image=photo)
label.pack()





root.mainloop()