#references:https://www.geeksforgeeks.org/socket-programming-python/
#https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
import socket
import sys

host = 'www.google.com'
port = 80
request = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
buffer_size = 4096

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created Successfully")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

try:
    host_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("There is an error resolving the host")
    sys.exit()

s.connect((host_ip, port))
print(f'Socket connected to {host} on {host_ip}')

s.send(request.encode())
s.shutdown(socket.SHUT_WR)

full_data = ""
while True:
    data = s.recv(buffer_size)
    if not data: break
    full_data += data
print(full_data)
s.close()
