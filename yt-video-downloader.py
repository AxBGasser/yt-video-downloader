from pytube import YouTube
from pathlib import Path
from datetime import datetime
from colorama import Fore, Style
import os

# URL de ejemplo:
# https://www.youtube.com/watch?v=j5h6ucwQklw
link = input("Ingresa la URL: ")
subdir = input("Ingresa el nombre del subdirectorio: ")

yt = YouTube(link)
print(Fore.GREEN + "Descargando...")
title = yt.title

print("")
print("Detalles del video")
print("Titulo: {} ".format(title))

###
#
video = yt.streams.get_by_itag(itag=299)
# video = yt.streams.get_highest_resolution()

###
#
# audio = yt.streams.get_by_itag(itag=251)
audio = yt.streams.get_audio_only()

###
# HomePath = Videos
# Subdirectories = /YT-Download/{subdir}
path = 'Videos\YT-Download\{}'.format(subdir)

###
# Folder
folder = str(os.path.join(Path.home(), path))

###
#
try:
    video.download(folder,None, 'Video-')
    audio.download(folder,None, 'Audio-')
    print("Descarga completada!")
    print(Style.RESET_ALL)    
except:
    print(Fore.RED + "Error:")
    print(Fore.RED + "+ itags no encontrados intentar descargar el video y audio.")
    print(Fore.RED + "+ Verifica los itag disponibles en cada video y acomodalo a gusto")
    print(Fore.GREEN + "-> Documentacion oficial:  https://pytube.io/en/latest/user/streams.html#filtering-streams")
    print(Style.RESET_ALL)
