import os.path
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import pytube


def clear():
    video_link.set('')


def close_window():
    window.destroy()


def open_folder():
    path1 = os.path.realpath(path)
    os.startfile(path1)


def download():
    try:
        link_1 = video_link.get()
        u2be_link = pytube.YouTube(link_1)
        video = u2be_link.streams.get_highest_resolution()
        video.download(output_path=path)
        messagebox.showinfo(None, "Video downloaded")
    except:
        messagebox.showinfo('ERROR', 'URL is not defined')


if __name__ == '__main__':
    path = 'C:/U2BE Downloader/'

    window = tk.Tk()
    window.geometry('400x200')
    window.resizable(False, False)
    window.title('U2BE DOWNLOADER')
    window.config(bg='#ed9b9b')
    window.iconbitmap('u2be_l.ico')

    lb1 = tk.Label(window, text='YOUTUBE VIDEO DOWNLOADER', font=('Times', '15', 'bold'), fg='#ec1316', bg='#ed9b9b')
    lb1.pack(padx=5, pady=10)

    lb2 = tk.Label(window, text='Link video', font=('Times', '15', 'bold'), fg='#ec1316', bg='#ed9b9b')
    lb2.place(x=10, y=80)

    video_link = tk.StringVar()
    link_name = tk.Entry(window, textvariable=video_link, font=('Arial', '10'))
    link_name.place(x=120, y=85)

    btn1 = tk.Button(window, text='Download', font=('Arial', '10', 'bold'), fg='#ec1316', bd=2, command=download)
    btn1.place(x=280, y=80)
    btn2 = tk.Button(window, text=' Clear ', font=('Arial', '10', 'bold'), bd=2, command=clear)
    btn2.place(x=80, y=150)
    btn4 = tk.Button(window, text='Open folder', font=('Arial', '10', 'bold'), bd=2, command=open_folder)
    btn4.place(x=165, y=150)
    btn3 = tk.Button(window, text='  Exit  ', font=('Arial', '10', 'bold'), bd=2, command=close_window)
    btn3.place(x=280, y=150)

    window.mainloop()
