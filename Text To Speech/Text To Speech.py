import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to speech")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#305065")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')  # Corrected property name to 'voices'

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    if text:
        if speed == 'Fast':
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

def download():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')  # Corrected property name to 'voices'

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.save_to_file(text, 'output.mp3')
        engine.runAndWait()
    
    if text:
        if speed == 'Fast':
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()
        # Optionally, ask user to choose the save location
        save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if save_path:
            os.rename('output.mp3', save_path)

current_dir = os.path.dirname(os.path.abspath(__file__))

# Icon
speak_image_path = os.path.join(current_dir, "speak.png")
image_icon = PhotoImage(file=speak_image_path)
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

logo_image_path = os.path.join(current_dir, "speaker logo.png")
Logo = PhotoImage(file=logo_image_path)
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg='black').place(x=100, y=30)

# Text Area
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg='#305065', fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg='#305065', fg="white").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font='arial 14', state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

btn = Button(root, text="Speak", compound=LEFT, image=image_icon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

download_image_path = os.path.join(current_dir, "download.png")
image_icon2 = PhotoImage(file=download_image_path)
save = Button(root, text="Save", compound=LEFT, image=image_icon2, width=130, bg='#39c790', font="arial 14 bold", command=download)
save.place(x=730, y=280)

root.mainloop()
