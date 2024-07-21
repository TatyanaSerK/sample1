from tkinter import *
from tkinter import ttk
import qrcode

def gen_qr(): #функция для создания QR кода
    e1["text"] = e1.get()
    img = qrcode.make(e1["text"]) #кодируем при помощи библиотеки
    img.save("qr_new.png")  # сохраняем картинку с QR
    my_qr = PhotoImage(file="qr_new.png")
    label = ttk.Label(image=my_qr, text="QR", compound="top") #открываем картинку после нажатия кнопки
    label.pack()


#рабочее окно
root = Tk()
root.title("my_QR")
root.geometry("500x400")
#
t1 = Label(text="Введите текст:", height=3) #
e1 = Entry(width=80) #поле ввода
but = Button(text="СГЕНЕРИРОВАТЬ QR-code", width=70, height=3, command=gen_qr) # кнопка

t1.pack()
e1.pack()
but.pack()

root.mainloop()
