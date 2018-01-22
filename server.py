import tkinter
import random
import pyautogui
import math
from tkinter import *

def textInput(inputFrame, message):
    inputFrame.insert('1.0', str(message))
    # command= lambda: textInput(inputBox, "kek"+"\n")

def sendText(message):
    textInput(inputBox, message)

window = Tk()
window.geometry('300x400')
window.title("pyChat")

messageFrame = Frame(window)
sendButton = Button(messageFrame,text="Send", padx='50', pady=5) #command= lambda: sendText())
messageBox = Text(messageFrame, width=20, height=2)

inputBox = Text(window,width=36, height=22,) #state=DISABLED)

inputBox.pack(side=TOP)
messageFrame.pack(side=BOTTOM)
messageBox.pack(side=LEFT)
sendButton.pack(side=RIGHT)
window.mainloop()
