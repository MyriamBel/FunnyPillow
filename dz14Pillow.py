#/usr/bin/python3
# -*- coding: utf-8 -*-
#Программа создает картинку с разрешением ФуллашДи и рисует слева направо вертикальные линии
#шириной 1 пх. Цвет первой линии (128,128,128). Цвет каждой последующей имеет случайный сдвиг
# по каждому параметру цвета на +-10.каждый след.цвет определяется относительно предыдущего.
#Если диапазон больше 255, то равен 255,если меньше 0,торавен 0
def createimg():
    from PIL import Image, ImageDraw
    from random import randint, choice
    x = 1920
    y = 1080
    new = Image.new(mode='RGB', size=(x, y), color=(0, 0, 0))
    draw = ImageDraw.Draw(new)
    r = 128
    g = 128
    b = 128
    for i in range(0, y):
        draw.line((0, i) + (x, i), width=1, fill=(r, g, b))
        r = choice((r + randint(0, 10), r - randint(0, 10)))
        if r > 255:
            r = 255
        elif r < 0:
            r = 0
        g = choice((g + randint(0, 10), g - randint(0, 10)))
        if g > 255:
            g = 255
        elif g < 0:
            g = 0
        b = choice((b + randint(0, 10), b - randint(0, 10)))
        if b > 255:
            b = 255
        elif b < 0:
            b = 0
    new.save('testPillow.jpg')
createimg()
