from tkinter import *
from gtts import gTTS
from playsound import playsound
from tkinter import ttk

def text_to_speech():
    global audio
    global e1
    text_inputted = e1.get()

    audio= "speech.mp3"
    sc = gTTS(text = text_inputted , slow= False)
    sc.save(audio)
    playsound(audio)

root = Tk()
root.geometry("300x100")
MainFrame = Tk.frame(root)
Label(root ,text="Enter The Text:").grid(row = 0,column= 0)
e1=Entry(root)
e1.focus_set()
e1.grid(row=0 , column= 1)
Button(root , text="Listen Now!!!",command=text_to_speech).grid(row=1, column=1)
root.mainloop()