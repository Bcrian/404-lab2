import socket
import sys
import time 

host = ""
port = 8001
buffer_size = 1024

s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_server.bind((host, port))
s_server.listen(2)

while True:
    clientsocket, address = s_server.accept()
    s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_data = clientsocket.recv(buffer_size)
    client_host = send_data.decode()

    try:
        host_ip = socket.gethostbyname(client_host)
    except socket.gaierror:
        print("There is an error resolving the host")
        sys.exit()

    s_client.connect((host_ip, 80))
    s_client.send(send_data)
    s_client.shutdown(socket.SHUT_WR)

    data = s_client.recv(buffer_size)
    clientsocket.send(data)
    clientsocket.close()