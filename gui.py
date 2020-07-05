import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageDraw ,  ImageFilter
import PIL
import os
import pickle
import numpy as np
from numpy import asarray

window = tk.Tk()
window.title('Digit recogniser')
window.resizable('FALSE','FALSE')
window.geometry("400x400")

empty2=Label(window,text=" ")
empty2.grid(row=0,column=0)

l1 = Label(window,text="Use mouse to draw a digit for prediction",font=('Times New Roman',14))
l1.grid(row=1,column=0,columnspan=2)

c = Canvas(window,width=200,height=200,bg='white')


def paint(event):
    
    x1,y1 = (event.x-1) , (event.y-1)
    x2,y2 = (event.x+1) , (event.y+1)
    c.create_oval(x1,y1,x2,y2,fill='black',outline='black',width=5)
    draw.line([x1, y1, x2, y2],fill="black",width=5)
    filename = "image.png"
    image1.save(filename)

def act():
    c.delete('all')
    os.remove('image.png')
    os.remove('testflatten.png')
    draw.rectangle([0,0,200,200],fill='white')
    l2.config(text="")
    return



def imageprepare(argv):
    """
    This function returns the pixel values.
    The imput is a png file location.
    """
    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (28, 28), (255))  # creates white canvas of 28x28 pixels

    if width > height:  # check which dimension is bigger
        # Width is bigger. Width becomes 20 pixels.
        nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
        if (nheight == 0):  # rare case but minimum is 1 pixel
            nheight = 1
            # resize and sharpen
        img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
        newImage.paste(img, (4, wtop))  # paste resized image on white canvas
    else:
        # Height is bigger. Heigth becomes 20 pixels.
        nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
        if (nwidth == 0):  # rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
        newImage.paste(img, (wleft, 4))  # paste resized image on white canvas

    # newImage.save("sample.png

    tv = list(newImage.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    print(tva)
    return tva





def predict_it():
    img = Image.open("image.png")
    img = img.resize((28,28), Image.ANTIALIAS)
    filename = 'testflatten.png'
    img.save(filename)
    x=[imageprepare('./testflatten.png')]
    a = model.predict(x)
    l2.config(text="We predict the number is" + str(a),font=('Times New Roman',14))
    l2.grid(row=6,column=0)
    return

image1 = PIL.Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(image1)


c.grid(row=2,column=0,columnspan=2)
c.bind('<B1-Motion>',paint)

file = open('model.pkl', 'rb')
model=pickle.load(file)
file.close()

b1=Button(window,text="clear",command=act,padx=8,pady=8)
b2=Button(window,text='predict the digit',command=predict_it,padx=8,pady=8)

b2.grid(row=4,column=0)
b1.grid(row=4,column=1)

empty=Label(window,text=" ")
empty.grid(row=3,column=0)

l2 = Label(window)

b3=Button(window,text='exit',command=window.quit)
b3.grid(row=5,column=0,columnspan=2,padx=10,pady=10)


window.mainloop()