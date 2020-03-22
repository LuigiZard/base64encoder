# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 17:45:27 2020

@author: LuigiZard
"""

from tkinter import filedialog 
from PIL import ImageTk
import PIL.Image
from tkinter import *
import os
import base64

def browseBtn():
   
    filename = filedialog.askopenfilename()
    texto.insert(0, filename)
    img = ImageTk.PhotoImage(PIL.Image.open(filename))
    #panel = Label(ventana, image = img)
    panel.config(image = img)
    panel.image = img
    #panel.pack(side = "bottom", fill = "both", expand = "yes")
    # panel.place(x = 32, y = 128)

    
def convbase64():
    path = str(texto.get())
    imagen = open(path, 'rb')
    leeimg = imagen.read()
    codigo64 = base64.encodebytes(leeimg)
    texto2.insert("1.0", codigo64)

def decode64():
    myFormats = [('JPEG / JFIF','*.jpg'),\
                     ('Portable Network Graphics','*.png'),\
                     ('Windows Bitmap','*.bmp'),('CompuServer GIF','*.gif'),]
    baset = texto2.get("1.0", "end")
    filepath = filedialog.asksaveasfilename(filetypes=myFormats)
    imagen = open(filepath, 'wb')
    imagen.write(base64.decodebytes(baset.encode()))
    imagen.close()

ventana = Tk()
ventana.title("Convertidor imagen a Base64")
ventana.geometry("800x480")
letrero = Label(ventana, text = "Imagen:")
texto = Entry(ventana, width = 100)
limagen = Label(ventana, text = "Vista previa")
panel = Label(ventana, image = "")
buscarImg = Button(ventana, text = "Elegir", command=browseBtn)
letrero2 = Label(ventana, text = "codigo base64:")
texto2 = Text(width = 75, height = 1)
btnconvertir = Button(ventana, text = "Codificar", command=convbase64)
btndecodificar = Button(ventana, text = "decodificar", command=decode64)
btnabrirArchivo = Button(ventana, text = "Abrir archivo", command = abrirar)
btnabrirImg = Button(ventana, text = "Abrir imagen", command = abririmg)
letrero.place(x = 32, y = 32)
letrero2.place(x = 16, y = 64)
limagen.place(x = 32, y = 96)
texto.place(x = 114, y = 35)
texto2.place(x = 114, y = 69)
buscarImg.place(x = 724, y = 32)
btnconvertir.place(x = 724, y = 64)
btndecodificar.place (x = 724, y = 96)
panel.place(x = 32, y = 128)

ventana.mainloop()