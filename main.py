import os.path
import tkinter as tk
from tkinter import messagebox
import pytube
from pytube import Playlist


def clear():
    video_link.set('')


def close_window():
    window.destroy()


def open_folder():
    path1 = os.path.realpath(path)
    os.startfile(path1)


def download_video():
    try:
        link_1 = video_link.get()
        u2be_link = pytube.YouTube(link_1)
        video = u2be_link.streams.get_highest_resolution()
        video.download(output_path=path)
        messagebox.showinfo('DONE!', "Video downloaded")
    except:
        messagebox.showinfo('ERROR', 'URL is not defined')


def download_playlist():
    try:
        playlist_url = playlist_link.get()
        pl = Playlist(playlist_url)

        for video in pl.videos:
            video.streams.get_highest_resolution().download(output_path=path)
        messagebox.showinfo('DONE!', "All videos from playlist downloaded")
    except:
        messagebox.showinfo('ERROR', 'URL is not defined')


if __name__ == '__main__':
    path = 'C:/U2BE Downloader/'

    window = tk.Tk()
    window.geometry('420x250')
    window.resizable(False, False)
    window.title('U2BE DOWNLOADER')
    window.config(bg='#ed9b9b')
    window.iconbitmap('u2be_l.ico')

    lb1 = tk.Label(window, text='YOUTUBE VIDEO DOWNLOADER', font=('Times', '15', 'bold'), fg='#ec1316', bg='#ed9b9b')
    lb1.pack(padx=5, pady=10)

    lb2 = tk.Label(window, text='Link video', font=('Times', '15', 'bold'), fg='#ec1316', bg='#ed9b9b')
    lb2.place(x=10, y=80)

    lb3 = tk.Label(window, text='Link playlist', font=('Times', '15', 'bold'), fg='#ec1316', bg='#ed9b9b')
    lb3.place(x=10, y=130)

    video_link = tk.StringVar()
    link_name = tk.Entry(window, textvariable=video_link, font=('Arial', '10'))
    link_name.place(x=140, y=85)

    playlist_link = tk.StringVar()
    link_name = tk.Entry(window, textvariable=playlist_link, font=('Arial', '10'))
    link_name.place(x=140, y=135)

    btn1 = tk.Button(window, text='Download', font=('Arial', '10', 'bold'), fg='#ec1316', bd=2, command=download_video)
    btn1.place(x=300, y=80)
    btn4 = tk.Button(window, text='Download', font=('Arial', '10', 'bold'), fg='#ec1316', bd=2,
                     command=download_playlist)
    btn4.place(x=300, y=130)
    btn2 = tk.Button(window, text=' Clear ', font=('Arial', '10', 'bold'), bd=2, command=clear)
    btn2.place(x=80, y=190)
    btn4 = tk.Button(window, text='Open folder', font=('Arial', '10', 'bold'), bd=2, command=open_folder)
    btn4.place(x=165, y=190)
    btn3 = tk.Button(window, text='  Exit  ', font=('Arial', '10', 'bold'), bd=2, command=close_window)
    btn3.place(x=280, y=190)

    window.mainloop()
