import hashlib
from tkinter import *
from array import *

znaki = array("u")
formated = array("u")
indx = 0
cindx = 0

strs = ["" for x in range(11)]

def fastH(string, hash):
    if(hash == "sha256"):
        h = hashlib.sha256(string.encode()).hexdigest()
        return h
    if(hash == "md5"):
        h = hashlib.md5(string.encode()).hexdigest()
        return h


h = fastH("Pain", "sha256")

for i in range(len(h)):
    znaki.append(h[i])

for y in range(11):
    for x in range(6):
        if(indx >= 0 and indx <= 63):
            strs[y] += znaki[indx]
            indx+=1
        else:
            strs[y] += "0"

size = 100
window = Tk()
content = Canvas(window, width=size*11, height= size*6)
content.pack()

for i in range(11):
    c = "#" + strs[cindx]
    content.create_rectangle(i*size, 0, i*size + size, size*11, fill=c)
    cindx+=1

mainloop()

