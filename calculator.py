from tkinter import *
root = Tk()
root.geometry("330x445")
root.title("My Calculator")
textinput = StringVar()
operator = ""

# FRAME
f2=Frame(root,width=300,height=500,bg="powder blue",relief=SUNKEN)
f2.pack()

# Function
def btnclick (number):
	global operator
	operator=operator + str(number)
	textinput.set(operator)
def clrdisplay ():
	global operator
	operator=""
	textinput.set(operator)
def butnequal ():
	global operator
	textinput.set(eval(operator))
	operator=""

# DISPLAY
textdisplay=Entry(f2,font=('arial',20,'bold'),textvariable=textinput,bd=15,insertwidth=4,bg="powder blue",justify='right')
textdisplay.grid(columnspan=4)

# BUTTONS
btn7=Button(f2,text=".",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="powder blue",command=lambda:btnclick(".")).grid(row=6,column=0)
btn7=Button(f2,text="+",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="powder blue",command=lambda:btnclick("+")).grid(row=3,column=3)
btn7=Button(f2,text="*",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="powder blue",command=lambda:btnclick("*")).grid(row=4,column=3)
btn7=Button(f2,text="/",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="powder blue",command=lambda:btnclick("/")).grid(row=5,column=3)
btn7=Button(f2,text="9",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(9)).grid(row=3,column=2)
btn7=Button(f2,text="8",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(8)).grid(row=3,column=1)
btn7=Button(f2,text="7",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(7)).grid(row=3,column=0)
btn7=Button(f2,text="6",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(6)).grid(row=4,column=2)
btn7=Button(f2,text="5",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(5)).grid(row=4,column=1)
btn7=Button(f2,text="4",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(4)).grid(row=4,column=0)
btn7=Button(f2,text="3",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(3)).grid(row=5,column=2)
btn7=Button(f2,text="2",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(2)).grid(row=5,column=1)
btn7=Button(f2,text="1",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(1)).grid(row=5,column=0)
btn7=Button(f2,text="0",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light green",command=lambda:btnclick(0)).grid(row=6,column=1)
btn7=Button(f2,text="-",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="powder blue",command=lambda:btnclick("-")).grid(row=6,column=3)
btneql=Button(f2,text="=",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="powder blue",command=butnequal).grid(row=6,column=2)
btnclr=Button(f2,text="C",padx=16,pady=16,bd=4,fg="black",font=('arial',20,'bold'),bg="light pink",command=clrdisplay).grid(row=2,column=3)



root.mainloop()