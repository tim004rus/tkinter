from tkinter import *
root = Tk()

var=IntVar()
check=Checkbutton(root, text=u'1 пункт', variable='var1', onvalue=1, offvalue=0)
check.pack()
root.mainloop()