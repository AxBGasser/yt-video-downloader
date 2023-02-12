from colorama import Fore, Style
from datetime import datetime
from pytube import YouTube
from pathlib import Path
import pandas as pd
import os

# URL de ejemplo:
# https://www.youtube.com/watch?v=j5h6ucwQklw
link = input("Ingresa la URL: ")
subdir = input("Ingresa el nombre de la carpeta: ")
yt = YouTube(link)

print("Titulo del video: {} ".format(yt.title))

""" ===================================================== """
""" Get video streams (information) from the video """
""" resolution, 60fps """
video_itag = yt.streams.filter(resolution="1080p")
print(video_itag)
print("")
video_itag = input("Ingresa el itag: ")
video = yt.streams.get_by_itag(video_itag)

print("====================================================")

""" ===================================================== """
""" Get audio streams (information) from the video """
audio_selected = yt.streams.filter(type="audio")
print(audio_selected)
print("")
audio_itag = input("Ingresa el itag: ")
audio = yt.streams.get_by_itag(audio_itag)
""" ===================================================== """

path = 'Videos\YT-Download\{}'.format(subdir)
folder = str(os.path.join(Path.home(), path))
print("====================================================")

try:
    print("Descargando...")
    video.download(folder , None , 'VIDEO-')
    audio.download(folder , None , 'AUDIO-')
    print("====================================================")
    print("Descarga completada!")
except:
    print("Error:")
    print("Itags no encontrados intentar descargar el video y audio.")
    print("Verifica los itag disponibles en el video y seleccionalo a gusto")
    print("=> Documentacion oficial: https://pytube.io/en/latest/user/streams.html#filtering-streams")