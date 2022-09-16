from tkinter import *
from pytube import YouTube
from tkinter import messagebox
from tkinter import filedialog

#[Corpus; Window settings].
root = Tk()
root.title("Simple Youtube Video Downloader")
root.geometry("500x600")
#root.iconbitmap("icon.ico")

#[Corpus; Download (function)].
def download():
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successfully")
        myVar.set("")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")
        messagebox.showerror("Error",f"Error {e}")

#[Corpus; Choose dir (function)].
def browse_file():
    filename = filedialog.askdirectory()
    if filename:
        path.set(filename)

#[Corpus; Starting].
Label(root, text = "Welcome to Youtube\nDownloader Application", font = "Consolas 15 bold").pack()
myVar = StringVar()
myVar.set("Enter the link below")
Entry(root, textvariable = myVar, width = 40).pack(pady = 10)
link = StringVar()
Entry(root, textvariable = link, width = 40).pack(pady = 10)
Button(root, text = "Download video", command = download).pack()
path = StringVar()
Entry(root, textvariable = path, width = 40).pack(pady = 10)
Button(root, text = "Browse", command = browse_file).pack()
root.mainloop()