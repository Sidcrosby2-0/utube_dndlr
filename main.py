from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import pytube


def clear():
    video_link.set('')


def close_window():
    window.destroy()


def download():
    try:
        link_1 = video_link.get()
        u2be_link = pytube.YouTube(link_1)
        video = u2be_link.streams.get_highest_resolution()
        video.download(output_path='C:/U2BE Downloader/')
        messagebox.showinfo(None, "Video downloaded in  C:/U2BE Downloader")
    except:
        messagebox.showinfo('ERROR', 'URL is not definded')


if __name__ == '__main__':

    window = tk.Tk()
    window.geometry('450x250')
    window.resizable(False, False)
    window.title('U2BE DOWNLOADER')
    window.config(bg='#ed9b9b')

    lb1 = tk.Label(window, text='YOUTUBE VIDEO DOWNLOADER', font='Arial,15,bold',
                   bg='#ed9b9b')
    lb1.pack(padx=5, pady=10)

    lb2 = tk.Label(window, text='Link video', font='Arial,15,bold', bg='#ed9b9b')
    lb2.place(x=10, y=100)

    video_link = tk.StringVar()
    link_name = tk.Entry(window, textvariable=video_link, font='Arial,15,bold')
    link_name.place(x=150, y=100)

    btn1 = tk.Button(window, text='Download', font='Impact,8,bold', bd=2, command=download)
    btn1.place(x=360, y=100)
    btn2 = tk.Button(window, text='Clear', font='Arial,8,bold', bd=2, command=clear)
    btn2.place(x=140, y=160)
    btn3 = tk.Button(window, text='Exit', font='Arial,8,bold', bd=2, command=close_window)
    btn3.place(x=240, y=160)

    window.mainloop()
