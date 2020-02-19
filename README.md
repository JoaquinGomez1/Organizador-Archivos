# Organizador-Archivos
Programa que organiza los archivos que descargo a diario en mi PC

#Importante: el comportamiento de este programa solo fue testeado en mi máquina, utilizando windows 10 y el navegador chrome para descargar archivos. Si se descarga algo utilizando otro navegador como por ejemplo Firefox el script no funcionará ya que, al descargar los archivos directamente con su nombre y extension original (sin usar una extension .tmp como lo hace chrome), si los archivos descargados son muy grandes se intentarán mover antes de que finalice la descarga. 


El programa funciona utilizando la libreria 'Watchdog', la cual se encarga de monitorear carpetas designadas constantemente esperando cambios. 

Los comandos principales para determinar que accion tomar al crear o modificar un archivo se encuentran en las funciones llamadas 'on_created' y 'on_modified' las cuales dictaminan que hacer en caso de que se cree un archivo o se modifique. 
Todos los cambios que se realizan dentro de la carpeta de descargas quedan registrados en un archivo de texto llamado Creaciones.txt el cual el programa ignora a la hora de buscar modificaciones dentro de la carpeta.

Los nombres de los archivos que ingresan o se modifican en la carpeta de descargas se consiguen utilizando la variable 'event.src_path' que nos retorna el directorio completo (C:/users/bla/bla/bla.ejmplo) del archivo a observar. Esta variable es tomada como hija de la clase 'FileSystemEventHandler' provista por la libreria Watchdog.

Es importante para el programa agregar un tiempo de delay o de retraso entre las lecturas de modificaciones y las ejecuciones del codigo porque de esta forma evitamos mover archivos que todavia no han sido descargados completamente 


