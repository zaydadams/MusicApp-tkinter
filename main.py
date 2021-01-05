from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title("MusicPlayer")
root.geometry("1000x400")

pygame.mixer.init()


def add_song():
    song = filedialog.askopenfilename(initialdir="songs", filetypes=(("wav Files", "*.wav"),))
    song = song.replace("/home/user/Documents/MusicApp/", "")
    song = song.replace(".wav", "")
    listbx.insert(END, song)


def play():
    song = listbx.get(ACTIVE)
    song1 = f'/home/user/Documents/MusicApp/{song}.wav'

    pygame.mixer.music.load(song1)
    pygame.mixer.music.play()
    display['text']=song


playbtn = Button(root, text="Play Song", bg="green", command=play)
playbtn.place(x=500, y=300)

def pause():
    pygame.mixer.music.pause()


pausebtn = Button(root, text="Pause Song", bg="green", command=pause)
pausebtn.place(x=590, y=300)


def unpause():
    pygame.mixer.music.unpause()


unpausebtn = Button(root, text="Unpause Song", bg="green", command=unpause)
unpausebtn.place(x=690, y=300)


def stop():
    pygame.mixer.music.stop()


stopbtn = Button(root, text="Stop", bg="green", command=stop)
stopbtn.place(x=800, y=300)

display = Label(root, text="", relief="groove", bg="green", fg="white")
display.place(x=10, y=10)
display.config(width=60, height=4)

lblframe1 = LabelFrame(root, text="Playlist")
lblframe1.pack(fill="both")
lblframe1.config(bg="white")
lblframe1.place(x=510, y=10)
listbx = Listbox(lblframe1, bg="grey", fg="white", width="60")
listbx.pack()

menu1 = Menu(root)
root.config(menu=menu1)

add_song_menu = Menu(menu1)
menu1.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add Song To Playlist", command=add_song)

root.mainloop()

# songs are too big to be exported
