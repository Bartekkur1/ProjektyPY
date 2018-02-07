import socket
import threading

succ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
succ.connect(("127.0.0.1", 10000))
#succ.send(bytes(input(), "utf-8"))

def _input():
    while True:
        succ.send(bytes(input(), "utf-8"))

def _output():
    while True:
        data = succ.recv(1024)
        if data != None:
            print(str(data, "utf-8"))

inputThread = threading.Thread(target=_input)
outputThread = threading.Thread(target=_output)

inputThread.start()
outputThread.start()