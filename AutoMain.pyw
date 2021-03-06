import time
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import os.path
import shutil
import GUI


# Clase que controla los eventos.
# Actualmente solo monitorea correctamente archivos descargados en chrome
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        nombre = os.path.basename(event.src_path)
        ListaConNombre = os.path.splitext(nombre)
        ExtensionDelArchivo = ListaConNombre[1]
        timeToWait = 3
        time.sleep(timeToWait)
        print(f'Se agregó un archivo en: {DownloadDir}')  # 1

        if ExtensionDelArchivo == ".tmp" or ExtensionDelArchivo == ".crdownload":
            MyHandler.on_modified(event)  # Si el archivo todavia no se descargo completamente todavia, se lo envia a
            #la funcion on_modified para que se la continue monitoreando hasta que finalice la descarga

        else:
            for i in range(len(DirArr)):
                if (ExtensionDelArchivo in TypeArr[i]):
                    ActualizarRegistros(event, "Creaciones")
                    MoverArchivo(event, DirArr[i])
                    time.sleep(timeToWait)
                    BorrarSiExiste(event.src_path, DirArr[i] + "/" + nombre)
                    break  # Quiero que esto se realice una sola vez

    def on_modified(self, event):
        Modify = True
        nombre = os.path.basename(event.src_path)
        soporte = os.path.splitext(nombre)
        extension = soporte[1]
        timeToWait = 5  # Tiempo de espera de control en segundos
        Delay = 3  # Tiempo estandar para que el archivo descargado se agregue correctamente al directorio

        time.sleep(Delay)

        if event.src_path == "C:/Users/Joaquin/Downloads/Creaciones.txt":
            Modify = False  # Controlo si modifico o no el archivo

        for i in range(len(DirArr)):
            if (extension in TypeArr[i]) and Modify:
                ActualizarRegistros(event, "Creaciones")
                MoverArchivo(event, DirArr[i])
                time.sleep(timeToWait)
                BorrarSiExiste(event.src_path, DirArr[i] + "/" + nombre)
                break


# Crea un .txt con los datos del archivo que ingresó en la carpeta de descargas
def ActualizarRegistros(event,
                        ArchName):  # 'event' no tocar para que funcione el observer  /// 'ArchName' = nombre de archivo
    ArchivoDeTexto = open(f"C:/Users/Joaquin/Downloads/{ArchName}.txt", "a")
    hora = datetime.now()
    nombre = os.path.basename(event.src_path)
    datos = ["Nombre Archivo: " + "'" + nombre + "'  ", "Modificado el: ", time.strftime("%d/%m/%y"), "  A la hora: ",
             hora.strftime("%H:%M:%S")]

    for i in range(len(datos)):
        ArchivoDeTexto.write(str(datos[i]))

    ArchivoDeTexto.write("\n")
    ArchivoDeTexto.close()


def MoverArchivo(event, path):
    if os.path.basename(event.src_path) != "Creaciones.txt":
        if os.path.exists(event.src_path):
            try:
                shutil.move(event.src_path, path)
            except shutil.Error:
                pass


# Esta función esta para no tener archivos repetidos en la carpeta de descargas y en descargas temporal
def BorrarSiExiste(path, dirMovido):  # path = direccion de descargas    ///     dirMovido = donde se movió
    if os.path.basename(path) != "Creaciones.txt":
        if os.path.exists(path) and os.path.exists(dirMovido):
            if os.path.basename(path) == os.path.basename(dirMovido):  # Comparar si tienen mismo nombre
                tamPath = os.path.getsize(path)
                tamDir = os.path.getsize(dirMovido)

                if tamPath >= tamDir:
                    os.remove(dirMovido)  # reemplazamos por el archivo mas grande
                else:
                    os.remove(path)


# ----------------------------------------------------PRINCIPAL---------------------------------------------------------


if __name__ == "__main__":
    # Destinos comunes
    DownloadDir = "C:/Users/Joaquin/Documents/Descargas Temp"  #  <---| Este es el destino de la carpeta a observar
    ProgramDir  = "C:/Users/Joaquin/Downloads/Programas"
    RarDir      = "C:/Users/Joaquin/Downloads/.Rar"
    PdfDir      = "C:/Users/Joaquin/Downloads/PDF"
    PyDir       = "C:/Users/Joaquin/Downloads/Python"
    ImgDir      = "C:/Users/Joaquin/Pictures"
    TorrentDir  = "C:/Users/Joaquin/Downloads/Torrents"

    # Definimos los tipos de archivos segun como terminan.
    rarType     = ".rar", ".zip", ".7-zip"
    imgType     = ".jpg", ".jpeg", ".png", ".psd", ".gif", ".webm", ".mp4", ".mp3", ".mpeg", ".wmv", ".webp", ".jepg", ".jfif"
    programType = ".exe", ".jar", ".tar", ".msi", ".iso"
    pyType      = ".py", "pyw"
    pdfType     = ".pdf", ".txt", ".ppt", ".doc", ".docx", ".docs", ".xml", "xlsx", "csv"
    torrentType = ".torrent"

    # Arreglos con los tipos de archivo y direcciones para facil acceso.
    DirArr = [RarDir, ImgDir, ProgramDir, PyDir, PdfDir, TorrentDir]
    TypeArr = [rarType, imgType, programType, pyType, pdfType, torrentType]

    # Estructura general del programa. T0do esto de abajo es requerimiento para que 'Watchdog' funcione correctamente
    MyHandler = MyHandler()
    gui = GUI.GUI(MyHandler, DownloadDir)
