import socket

server_ip = 'localhost'
server_port = 4000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

while True:
    pesan = input("Client : ")
    client_socket.send(pesan.encode())

    pesan = client_socket.recv(1024).decode()
    print(f"Server: {pesan}")

client_socket.close()