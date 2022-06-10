from tkinter import *
import tkinter as tk
from tkinter import ttk,filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.config(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

def open_folder():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs= os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
        # print(songs)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text = music_name)

def play_next():
    next_song = playlist.curselection()
    next_song = next_song[0] + 1
    next_song_name = playlist.get(next_song)
    music.config(text = next_song_name)
    mixer.music.load(next_song_name)
    mixer.music.play()

    playlist.select_clear(0,'end')
    playlist.activate(next_song)
    playlist.select_set(next_song)

def play_previous():
    previous_song = playlist.curselection()
    previous_song = previous_song[0] - 1
    previous_song_name = playlist.get(previous_song)
    music.config(text = previous_song_name)
    mixer.music.load(previous_song_name)
    mixer.music.play()

    playlist.select_clear(0,'end')
    playlist.activate(previous_song)
    playlist.select_set(previous_song)



musicplayericon = PhotoImage(file="clipart326945.png")
root.iconphoto(False,musicplayericon)

headerphoto = PhotoImage(file="top.png")
Label(root,image=headerphoto,bg="#0f1a2b").pack()

mainphoto = PhotoImage(file="inside music.png")
Label(root,image=mainphoto,bg="#0f1a2b",width=200,height=203).place(x=58,y=119)

# playbutton
playbutton = PhotoImage(file="playbutton.png")
Button(root,image=playbutton,bg="#0f1a2b",bd=0,command=play_song).place(x=115,y=330)

# stopbutton
stopbutton = PhotoImage(file="stop.png")
Button(root,image=stopbutton,bg="#0f1a2b",bd=0, command=mixer.music.stop).place(x=15,y=485)

# resumebutton
resumebutton = PhotoImage(file="resume.png")
Button(root,image=resumebutton,bg="#0f1a2b",bd=0,command=mixer.music.unpause).place(x=115,y=510)

# pausebutton
pausebutton = PhotoImage(file="pause.png")
Button(root,image=pausebutton,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=270,y=500)

#play_previous
playprevious = PhotoImage(file="Previous.png")
Button(root,image=playprevious,bg="#0f1a2b",bd=0,command=play_previous).place(x=80,y=580)

#playnext
playnext = PhotoImage(file="Next-Button.png")
Button(root,image=playnext,bg="#0f1a2b",bd=0,command=play_next).place(x=220,y=580)

# musiclist
menu = PhotoImage(file="menu.png")
Label(root,image=menu,bg="#0f1a2b").pack(padx=30,pady=50,side=RIGHT,anchor="w")

#current playing music label
music=Label(root,text="",font="arial 15",fg="white",bg="#0f1a2b")
music.place(x=400,y=250)

#musicframe
musicframe = Frame(root,bd=2,relief=RIDGE)
musicframe.place(x=400,y=350,width=465,height=250)

Button(root,text="Open Folder",width=13,height=2,font="arial 10 bold",fg="white",bg="#21b3de",command=open_folder).place(x=400,y=302)

# scroll bar
scroll = Scrollbar(musicframe)
playlist = Listbox(musicframe,width=100,font="arial 10",bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",
bd=0,yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)



root.mainloop()

