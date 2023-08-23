from tkinter import*
root=Tk()

root.geometry("455x300")
root.title("Calculator")
some=Label(text='''Calculator, machine for automatically performing arithmetical\n
operations and certain mathematical functions. Modern calculators are descendants of a \n
digital arithmetic machine devised by Blaise Pascal in 1642. Later in the 17th century,\n
Gottfried Wilhelm Leibniz created a more-advanced machine, and, especially in the late 19th century,\n
inventors produced calculating machines that were smaller and smaller and less and less laborious to use.\n 
In the early decades of the 20th century, desktop adding machines and other calculating devices were developed. Some were key-driven, others required a rotating drum 
\nto enter sums punched into a keyboard, and later the drum was spun by electric motor.
''',bg="blue",font=(19),padx=100,pady=50,fg="red",relief="groove")
some.pack(padx=10,pady=50,side=BOTTOM,fill=Y)
root.mainloop()