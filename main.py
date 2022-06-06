from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter import ttk, font
import time
import threading
from turtle import color
from numpy import False_
import serial

root = tk.Tk()
root.title('Tercera entrega')
root.resizable(height=False, width=False)

data = ''
recibido = ''
led=False

# --------------Configuración Serial----------------


def timer():
    global data
    global recibido
    global led
    while True:
        nucleo = serial.Serial('COM3', 9600)
        rawString = str(nucleo.readline())
        rawString = rawString.strip("b'\.n")  # Ya tengo mi valor @Data# limpio
        # Limpieza y verificación del dato en Serial
        if(rawString.count('@') == 1) and (rawString.count('#') == 1):
             data = rawString.strip("@#")
             recibido  = data
             print(data)
        ##

        register = Text(registerFrame, height=10, width=25, font=font.Font(
            family="Verdana", size=11,
        ))
        register.insert(INSERT, recibido)
        register.grid(
            row=2, column=0, columnspan=2, pady=10, padx=10)

        ##

        

        if led==True:
            nucleo.write(b'@')
            led=False
            print('entre')

        nucleo.close()
        time.sleep(0.1)  # 100ms


t = threading.Thread(target=timer)
t.start()


def test():
    print('me llamaron')


def OnOffLed():
    global led
    led=True
    


# ------------------------Configuracion inicial de frames -------
buttonsFrame = tk.Canvas(root, width=350, height=200, bg='Light gray')
buttonsFrame.grid(row=0, column=0)
registerFrame = tk.Canvas(root, width=350, height=275, bg='Light gray')
registerFrame.grid(row=0, column=1)

# ---------------------Se establace la posicion de los botones----------
botonSaveInfo = Button(buttonsFrame, text='Guardar datos RTC', font=font.Font(
    family="Verdana", size=8
), width=28).grid(
    row=0, column=0, padx=5, pady=15, columnspan=2)
botonReadInfo = Button(buttonsFrame, text='Leer datos de la EEPROM', font=font.Font(
    family="Verdana", size=8
), width=28).grid(
    row=1, column=0, padx=5, pady=10, columnspan=2)
botonReadInfoEspecifico = Button(buttonsFrame, text='Dato especifico', font=font.Font(
    family="Verdana", size=8
), width=12).grid(
    row=2, column=0, padx=10, pady=15)
combo = ttk.Combobox(buttonsFrame, values=[
                     "Bloque 1", "Bloque 2", "Bloque 3", "Bloque 4", "Bloque 5"], width=12)
combo.grid(row=2, column=1)
botonOffLed = Button(buttonsFrame, text='Apagar LED',command=OnOffLed, font=font.Font(
    family="Verdana", size=8
), width=12).grid(
    row=3, column=0, padx=8, pady=15)
botonOnLed = Button(buttonsFrame, text='Encender LED', font=font.Font(
    family="Verdana", size=8
), width=12).grid(
    row=3, column=1, padx=8, pady=15)
botonReadADC = Button(buttonsFrame, text='Leer ADC', font=font.Font(
                      family="Verdana", size=8
                      ), width=28).grid(
    row=4, column=0, padx=5, pady=15, columnspan=2)

# -----------------------Se establese el frame de registros y entrada de comandos

tk.Label(registerFrame, text='Comando:', bg='Light gray').grid(
    row=0, column=0, pady=10, padx=20)

label = Label(registerFrame, text='COMANDO:')
label.grid(row=0, column=0, pady=10, padx=8)
label.config(fg="Black", bg='Light gray', font=("Verdana", 12), justify='left')

entry = ttk.Entry(registerFrame,
                  font=font.Font(
                      family="Verdana",
                      size=11,
                      # weight=font.BOLD,   # Negrita.
                      slant=font.ITALIC,  # Cursiva.
                      overstrike=False,    # Tachado.
                      underline=False      # Subrayado.
                  ), width=11,
                  ).grid(row=0, column=1, padx='5')

botonComand = Button(registerFrame, text='Enviar comando',
                     width=33, font=font.Font(
                         family="Verdana", size=8,
                     )).grid(row=1, column=0, columnspan=2)
# entryComand.bind('<Return>', test())  # ('<Return>',funcionALlamar)

register = Text(registerFrame, height=10, width=25, font=font.Font(
    family="Verdana", size=11,))
register.grid(
    row=2, column=0, columnspan=2, pady=10, padx=10)

# start()
root.mainloop()
