import watchdog
from tkinter import *
from tkinter import Tk
from watchdog.observers import Observer


#Unico proposito de la GUI es dar feedback al usuario de que el programa se inicia correctamente

def Start(MyHandler, DownloadDir):
    Observar = Observer()
    Observar.schedule(MyHandler, DownloadDir, recursive=False)  # ACA DETERMINAMOS LA CARPETA A OBSERVAR
    print("Programa inciado...")

    Observar.start()

    Boton_Start = Button(text="Programa iniciado", width=15, height=2, background="darkblue",
                         foreground="white") \
        .place(x=85, y=125)


def GUI(Handler, DireccionDescargas):
    root = Tk()
    root.geometry("250x300")
    root.title("Organizador Automatico")

    Bievenido = Label(text="Bienvenido").place(x=100, y=100)
    Boton_Start = Button(root, text="Comenzar", command=lambda: Start(Handler, DireccionDescargas), width=10, height=2, background="darkgreen",
                         foreground="white") \
        .place(x=85, y=125)

    Boton_Stop = Boton_Start = Button(root, text="Esconder", command=root.withdraw, width=7, height=2,
                                      background="darkred",
                                      foreground="white") \
        .place(x=85, y=195)

    root.mainloop()