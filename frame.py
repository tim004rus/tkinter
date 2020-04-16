from tkinter import *
root = Tk()

frame=Frame(root,width=10,height=10,bg='green',bd=5)
button=Button(frame,text=u'кнопка')
frame.pack()
button.pack()
root.mainloop()