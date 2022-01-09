import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory # filedialog - otevirá a ukládá funkce dialogu, askdirectory - popup s nastavením cesty
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")

directory = askdirectory()
os.chdir(directory) # změní aktuální pracovní adresář na zadanou cestu. Jako cestu k novému adresáři přijímá pouze jediný argument
songlist = os.listdir() # seznam obsahující názvy položek v adresáři zadaném cestou
playlist = tkr.Listbox(musicplayer, font="Arial 12", bg="#C0C0C0", selectmode=tkr.SINGLE) # zobrazení textového seznamu uživateli a vybrání jednoho songu k přehrání

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init() # po inicializaci nahraje a pustí hudbu


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE)) #modlul pro kontrolu audia, nahraje hudbu
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


Button1 = tkr.Button(musicplayer, width=5, height=2, font="Helvetica 13 bold", text="PLAY", command=play, bg="#33cc33",
                     fg="white")
Button2 = tkr.Button(musicplayer, width=5, height=2, font="Helvetica 13 bold", text="STOP", command=stop,
                     bg="#ff6600", fg="white")
Button3 = tkr.Button(musicplayer, width=5, height=2, font="Helvetica 13 bold", text="PAUSE", command=pause, bg="#ffa366",
                     fg="white")
Button4 = tkr.Button(musicplayer, width=5, height=2, font="Helvetica 13 bold", text="UNPAUSE", command=unpause,
                     bg="#85e085", fg="white")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 14 bold", bg="#ffffcc", textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()