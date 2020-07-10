# coding: utf8
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from tempfile import TemporaryFile
import numpy as np
import os
from random import randint


def gen():
    if not(os.path.exists('images')):
        os.mkdir('images')
    income = ["A", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П",
              "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
    Shrift = ["arial", "calibri", "times", "tahoma", "corbel", "impact", "verdana", "sylfaen"]
    S = ["SMOOTH", "SMOOTH_MORE"]
    povarot = [-12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12]
    for litters in income:
        for fonts in Shrift:
            for turns in povarot:
                for size in range(8, 18):
                    label = litters
                    font = ImageFont.truetype(fonts, size)
                    fontimage = Image.new('L', (font.getsize(label)[0], sum(font.getmetrics())))
                    ImageDraw.Draw(fontimage).text((0, 0), label, fill=255, font=font)
                    fontimage = fontimage.rotate(turns, resample=Image.BICUBIC, expand=True)
                    img = Image.new('RGBA', (32, 32), 'white')
                    idrow = ImageDraw.Draw(img)
                    img.paste('black', box=(3, 3), mask=fontimage)
                    img.save('images/' + str(randint(1, 5000)) + "_" + str(income.index(label)) + "_" + str(
                        turns) + fonts + str(size) + '.png')
                    for x in S:
                        a = 'img = img.filter(ImageFilter.' + x + ')'
                        exec(a)
                        img.save('images/' + str(randint(1, 5000)) + "_" + str(income.index(label)) + "_" + str(
                            turns) + fonts + str(size) + x + '.png')


def test():
    if not(os.path.exists('test')):
        os.mkdir('test')
    income = ["A", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П",
              "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
    Shrift = ["verdana", "sylfaen", "georgia", "simsun"]
    S = ["SMOOTH", "SMOOTH_MORE"]
    povarot = [-12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12]
    for litters in income:
        for fonts in Shrift:
            for turns in povarot:
                for size in range(8, 18):
                    label = litters
                    font = ImageFont.truetype(fonts, size)
                    fontimage = Image.new('L', (font.getsize(label)[0], sum(font.getmetrics())))
                    ImageDraw.Draw(fontimage).text((0, 0), label, fill=255, font=font)
                    fontimage = fontimage.rotate(turns, resample=Image.BICUBIC, expand=True)
                    img = Image.new('RGBA', (32, 32), 'white')
                    idrow = ImageDraw.Draw(img)
                    img.paste('black', box=(3, 3), mask=fontimage)
                    img.save('test/' + str(randint(1, 5000)) + "_" + str(income.index(label)) + "_" + str(
                        turns) + fonts + str(size) + '.png')
                    for x in S:
                        a = 'img = img.filter(ImageFilter.' + x + ')'
                        exec(a)
                        img.save('test/' + str(randint(1, 5000)) + "_" + str(income.index(label)) + "_" + str(
                            turns) + fonts + str(size) + x + '.png')


if __name__ == "__main__":
    gen()
    test()
