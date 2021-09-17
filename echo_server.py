import socket
import time

host = ""
port = 8001
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#q3
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connect from {address} has been established")
    data = clientsocket.recv(buffer_size)
    clientsocket.send(data)
    clientsocket.close()