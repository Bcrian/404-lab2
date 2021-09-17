import socket

host = '127.0.0.1'
port = 8001
buff_size = 2048
payload = "www.google.com"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(host)
s.send(payload.encode())
s.shutdown(socket.SHUT_WR)
print("close socket")
s.close()