from tkinter import *

root = Tk()
l1 = Label(text="Машинное обучение", font="Arial 32")
l2 = Label(text="Распознавание образов", font=("Comic Sans MS", 24, "bold"))
l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')
l1.pack()
l2.pack()
root.mainloop()

def take():
    l['text'] = "Выдано"
 
root = Tk()
Label(text="Пункт выдачи").pack()
Button(text="Взять", command=take).pack()
l = Label(width=10, height=1)
l.pack()
root.mainloop()

e1 = Entry(width=50)
def insert():
    e1.insert(0,"Tkinter - GUI ")
b = Button(text="Вставить", command=insert)
e1.pack()
b.pack()
root.mainloop()

b1 = Button(text="Изменить", width=15, height=3)
 
def change():
    b1['text'] = "Изменено"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'
 
b1.config(command=change)
 
b1.pack()
root.mainloop()