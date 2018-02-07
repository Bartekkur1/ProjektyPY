import threading
import socket
from time import sleep

succ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
succ.bind(('127.0.0.1', 10000))
succ.listen(1)

connections = []
nicks = []

def getNick(a):
    for i in range(len(nicks)):
        if a[1] == nicks[i]:
            return str(nicks[i-1])

def kek(c, a):
    global connections
    global nicks

    c.send(bytes("write your nickname : ", "utf-8"))
    nicks.append(str(c.recv(1024), "utf-8"))
    nicks.append(a[1])

    while True:
        data = c.recv(1024)
        for connection in connections:
            if connection != c:
                kek = bytes(getNick(a) + " > ", "utf-8") + data
                connection.send(kek)

        if not data:
            break

while True:
    c, a = succ.accept()
    kekThread = threading.Thread(target=kek, args=(c, a))
    kekThread.daemon = True
    kekThread.start()
    connections.append(c)
    print(c)