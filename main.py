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
        messagebox.showinfo(None, "Видео загружено в папку C:/U2BE Downloader")
    except:
        messagebox.showinfo('Ошибка', 'Видео не найдено')


# def  get_resolution():
#     window2 = tk.Tk()
#     window2.geometry('200x90')
#     window2.title('ВЫБОР РАЗРЕШЕНИЯ')
#     window2.config(bg='#ffffff')
#     res_lb = tk.Label(window2, text='Выберите разрешение', font='Arial,7,bold', bg='#ffffff')
#     res_lb.pack(pady=15)
#     btn480 = tk.Button(window2, text='480p', command=lambda: (foo1(set_text('480p')), foo2(window2.destroy())))
#     btn480.place(x=10, y=50)
#     btn720 = tk.Button(window2, text='720p', command=lambda: (foo1(set_text('720p')), foo2(window2.destroy())))
#     btn720.place(x=60, y=50)
#     btn1080 = tk.Button(window2, text='1080p', command=lambda: (foo1(set_text('1080p')), foo2(window2.destroy())))
#     btn1080.place(x=110, y=50)
#     return foo1()



window = tk.Tk()
window.geometry('450x250')
window.resizable(False, False)
window.title('U2BE DOWNLOADER')
window.config(bg='#ed9b9b')

lb1 = tk.Label(window, text='Скачать видео с Ютуба.\nБесплатно! без регистрации! без смс!', font='Arial,15,bold',
               bg='#ed9b9b')
lb1.pack(pady=15)

lb2 = tk.Label(window, text='Ссылка на видео', font='Arial,15,bold', bg='#ed9b9b')
lb2.place(x=10, y=100)

video_link = tk.StringVar()
link_name = tk.Entry(window, textvariable=video_link, font='Arial,15,bold')
link_name.place(x=150, y=100)

btn1 = tk.Button(window, text='Скачать', font='Impact,8,bold', bd=2, command=download)
btn1.place(x=360, y=100)
btn2 = tk.Button(window, text='Очистить', font='Arial,8,bold', bd=2, command=clear)
btn2.place(x=140, y=160)
btn3 = tk.Button(window, text='Выход', font='Arial,8,bold', bd=2, command=close_window)
btn3.place(x=240, y=160)

window.mainloop()
