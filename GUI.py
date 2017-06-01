from tkinter import *
a = Tk()
a.title("Football")
a.geometry("500x500+100+100")
b = Label(text='EPL',fg='red',bg='gray')
b.pack()
c = Label(text='Liga BBVA',fg='red',bg='gray').place(x=10,y=10)
d = Label(text='Seria A',fg='red',bg='gray').place(x=450,y=10)
a.mainloop()
