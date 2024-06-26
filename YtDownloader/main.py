import tkinter as tk
from pytube import YouTube

def download_video():
    url = link.get()
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x200")

link = tk.StringVar()

label = tk.Label(root, text="Unesite YouTube URL:")
label.pack()

entry = tk.Entry(root, textvariable=link)
entry.pack()

button = tk.Button(root, text="Preuzmi video", command=download_video, bg="blue", fg="white")
button.pack()

root.mainloop()
