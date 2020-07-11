# coding: utf8
from __future__ import absolute_import, division, print_function, unicode_literals
from tkinter import *
import time
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from tempfile import TemporaryFile
import numpy as np
from random import randint
import tensorflow as tf
from tensorflow import keras
import os


def obrez(path):
    img = Image.open(path)
    newArr = np.array(img)
    x1 = 0
    x2 = len(newArr)
    y1 = 0
    y2 = len(newArr[0])
    if len(newArr[0][0]) == 4:
        white = np.array([255, 255, 255, 255])
    else:
        white = np.array([255, 255, 255])
    f = 0
    for i in range(len(newArr)):
        for j in range(len(newArr[0])):
            if np.array_equal(newArr[i][j], white):
                x1 = i
            else:
                f = 1
                break
        if f == 1:
            break
    f = 0
    for i in range(len(newArr) - 1, 0, -1):
        for j in range(len(newArr[0])):
            if np.array_equal((newArr[i][j]), white):
                x2 = i
            else:
                f = 1
                break
        if f == 1:
            break
    f = 0
    for i in range(len(newArr[0])):
        for j in range(len(newArr)):
            if np.array_equal(newArr[j][i], white):
                y1 = i
            else:
                f = 1
                break
        if f == 1: break
    f = 0
    for i in range(len(newArr[0]) - 1, 0, -1):
        for j in range(len(newArr)):
            if np.array_equal(newArr[j][i], white):
                y2 = i
            else:
                f = 1
                break
        if f == 1:
            break
    img = img.crop((y1 - 1, x1 - 1, y2 + 1, x2 + 1)).resize((28, 28), Image.ANTIALIAS)
    return img


def binar(img):
    arr = list()
    newArr = np.array(img)
    for i in newArr:
        f = []
        for j in i:
            t = round(abs(j[0] - 255) / 255, 3)
            f.append(t)
        arr.append(f)
    return arr


def mkDict(dir):
    t = 0
    imgs = os.listdir(dir)
    labels = []
    images = []
    for i in imgs:
        t += 1
        print(t)
        labels.append(int(i.split('_')[1]))
        images.append(binar(obrez(dir + '/' + i)))
    return labels, images


def neural():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(256, activation='sigmoid'),
        keras.layers.Dense(256, activation='sigmoid'),
        keras.layers.Dense(33, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def training(model):
    train_labels, train_images = mkDict('images')
    model.fit(train_images, train_labels, epochs=5)


def testing(model):
    test1_labels, test1_images = mkDict('test')
    test1_loss, test1_acc = model.evaluate(test1_images, test1_labels, verbose=2)
    print('\nТочность на проверочных данных:', test1_acc)
    return test1_acc