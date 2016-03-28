# -*- coding: utf-8 -*-

from urllib import request
import sys, os, time, webbrowser, re

# utilizar una plicacion de consola para entrar en un navegador de internet como tarea automatizada
url = 'http://www.google.es'
url_opened = request.urlopen(url)
print("Sitio web", str(url_opened.headers.items()))
print("")
print("Longitud: ", len(url_opened.read()))
time.sleep(3)
plataforma = sys.platform
if plataforma.lower().startswith('linux'):
    print("Plataforma: Linux")
elif plataforma.lower().startswith('darwin'):
    print("Plataforma: Macintosh")
elif plataforma.lower().startswith('win32'):
    print("Plataforma: Windows 32 bits")
else:
    print("Plataforma: No reconocida")

webbrowser.open_new("http://marca.com")