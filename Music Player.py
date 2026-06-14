#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    import tkinter as tk
    from tkinter import filedialog
    import pygame
    import os

    root = tk.Tk()
    root.title("Music Player")
    root.geometry("500x350")

    pygame.mixer.init()


    def play():
        pygame.mixer.music.load(listbox.get(tk.ACTIVE))
        var.set(listbox.get(tk.ACTIVE))
        pygame.mixer.music.play()


    def stop():
        pygame.mixer.music.stop()


    def pause():
        pygame.mixer.music.pause()


    def resume():
        pygame.mixer.music.unpause()


    def directorychooser():
        directory = filedialog.askdirectory()
        os.chdir(directory)

        for files in os.listdir(directory):
            if files.endswith(".mp3"):
                listbox.insert(tk.END, files)


    var = tk.StringVar()
    songtitle = tk.Label(root, textvariable=var)

    listbox = tk.Listbox(root)
    listbox.pack()

    play_button = tk.Button(root, text="Play", command=play)
    play_button.pack()

    stop_button = tk.Button(root, text="Stop", command=stop)
    stop_button.pack()

    pause_button = tk.Button(root, text="Pause", command=pause)
    pause_button.pack()

    resume_button = tk.Button(root, text="Resume", command=resume)
    resume_button.pack()

    directory_chooser_button = tk.Button(
        root, text="Choose Directory", command=directorychooser)
    directory_chooser_button.pack()

    songtitle.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
