from tkinter import*;
root=Tk()
root.geometry("700x500")
def password():
    v=entry3.get()
    if v=="123@anu":
        correct=Label(root,text="Correct password!",borderwidth=5,fg="green")
        correct.grid(row=15,column=2)
        import string
        import random

        if __name__=="__main__":
             s1=string.ascii_lowercase
             s2=string.ascii_uppercase
             s3=string.digits
             s4=string.punctuation
             def hello():
                   ab=enter.get()
                   s=[]
                   s.extend(list(s1))    
                   s.extend(list(s2))    
                   s.extend(list(s3))    
                   s.extend(list(s4))  
                   random.shuffle(s)
                   label23=Label(root,text="".join(s[0:ab]))
                   label23.grid(row=25,column=2)
            # print("Your password :","".join(s[0:len]))
        len=Label(root,text="Enter your desired password length")
        len.grid(row=20,column=2)
        enter=Entry(root,borderwidth=5,width=5)
        enter.grid(row=20,column=3,columnspan=1)
        b2=Button(root,text="submit",borderwidth=10,command=hello)
        b2.grid(row=20,column=4)
        s=[]
        s.extend(list(s1))    
        s.extend(list(s2))    
        s.extend(list(s3))    
        s.extend(list(s4))  
        random.shuffle(s)
        
    else:
        inco=Label(root,text="Incorrect password!!!",borderwidth=3,fg="Red")
        inco.grid(row=15,column=2)
# photo=PhotoImage(file="imagess.png")
# label=Label(image=photo)
# label.grid()
label1=Label(root,text="Welcome to Tauinfo.com \nAdvanced password generator app to generate and save multiapps password\n ",fg="grey",width=70,font="cursive")
label1.grid(row=0,column=2)
label2=Label(root,text="Enter your name",fg="blue",bg="white")
label2.grid(row=1,column=0)
label3=Label(root,text=" : ")
label3.grid(row=1,column=1)
entry1=Entry(root,borderwidth=5,bg="yellow",width=50)
entry1.grid(row=1,column=2)
label2=Label(root,text="Enter your Unique id:",fg="blue",bg="white")
label2.grid(row=3,column=0)
label3=Label(root,text=" : ")
label3.grid(row=3,column=1)
entry2=Entry(root,borderwidth=5,bg="yellow",width=50)
entry2.grid(row=3,column=2)
label2=Label(root,text="Password of Tauinfo",fg="blue",bg="white")
label2.grid(row=6,column=0)
label3=Label(root,text=" : ")
label3.grid(row=6,column=1)
entry3=Entry(root,borderwidth=5,bg="yellow",width=50)
entry3.grid(row=6,column=2)
b1=Button(root,text="Click to generate password",borderwidth=10,command=password)
b1.grid(rows=8,column=2)
root.title("Password Generator")
root.mainloop()