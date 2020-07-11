# coding: utf8
from __future__ import absolute_import, division, print_function, unicode_literals
import matplotlib.pyplot as plt
import tkinter as tk
import time
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
from tkinter import filedialog as fd
from gen import *
from lib import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        self.B = Button(self, text='генерация обучающей выборки', width=35, command=self.gen)
        self.B.place(x=0, y=0)
        self.B1 = Button(self, text='генерация тестирующей выборки', width=35, command=self.gentest)
        self.B1.place(x=0, y=30)
        self.B2 = Button(self, text='Иницаилзация нейронной сети', width=35, command=self.neur)
        self.B2.place(x=0, y=60)
        self.B3 = Button(self, text='Обучение нейронной сети', width=35, command=self.neural_network)
        self.B3.place(x=0, y=90)
        self.B4 = Button(self, text='Тестировка на заготовленной выборке', width=35, command=self.tests)
        self.B4.place(x=0, y=120)
        self.B5 = Button(self, text='Код генерации выборок', width=35, command=self.gener)
        self.B5.place(x=0, y=150)
        self.B6 = Button(self, text='загрузить изображение для тестировки', width=35, command=self.load)
        self.B6.place(x=0, y=180)
        self.B7 = Button(self, text='протестировать загруженное изображение', width=35, command=self.goTest)
        self.B7.place(x=0, y=210)

        self.T = Text(self, width=80, height=13, bg="black", fg='white', wrap=WORD)
        self.T.place(x=300, y=0)

        self.img = Image.open('title.jpg').resize((200, 200), Image.ANTIALIAS)
        self.tatras = ImageTk.PhotoImage(self.img)

        self.canvas = Canvas(self, width=200, height=200)
        self.canvas.create_image(10, 10, anchor=NW, image=self.tatras)
        self.canvas.place(x=0,y=240)

        self.model = neural()
        self.model.load_weights('model.h5')

        self.file_name = ""

    def goTest(self):
        self.T.delete(1.0, END)
        arr = list()
        arr.append(binar(obrez(self.file_name)))
        pred = self.model.predict(arr)[0]
        income = ["A", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П",
                  "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
        self.T.insert(1.0, 'по мнению нейронной сети это буква ' + income[np.argmax(pred)])

    def load(self):
        self.file_name = fd.askopenfilename()
        self.canvas.delete('all')
        self.img = Image.open(self.file_name).resize((200, 200), Image.ANTIALIAS)
        self.tatras = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(10, 10, anchor=NW, image=self.tatras)

    def gener(self):
        self.T.delete(1.0, END)
        a = open('gen.py', 'r', encoding='utf-8')
        t = list()
        for i in a:
            t.append(i)
        a.close()
        t = reversed(t[7:])
        for i in t:
            self.T.insert(1.0, i)

    def neur(self):
        self.T.delete(1.0, END)
        self.model = neural()
        self.T.insert(1.0, 'Нейронная сеть иницаилизированна')

    def gen(self):
        self.T.delete(1.0, END)
        gen()
        self.T.insert(1.0, 'Обучающая выборка сгенерирована\n')

    def gentest(self):
        self.T.delete(1.0, END)
        test()
        self.T.insert(1.0, 'Тестирующая выборка сгенерирована\n')

    def neural_network(self):
        self.T.delete(1.0, END)
        training('images')
        self.T.insert(1.0, 'Нейронная сеть обученна\n')

    def tests(self):
        self.T.delete(1.0, END)
        acc = testing('test')
        self.T.insert(1.0, 'Точность на проверочных данных: ' + str(acc))


if __name__ == '__main__':
    root = Tk()
    app = Window(root)
    root.wm_title("Маленькие циферки")
    root.geometry("950x500")
    root.mainloop()
