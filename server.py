import socket
server_ip = 'localhost'
server_port = 4000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((server_ip, server_port))

server_socket.listen(5)

print(f"Server mendengarkan di {server_ip} : {server_port}")

client_socket, client_address = server_socket.accept()

while True:
   pesan = client_socket.recv(1024).decode()
   if not pesan:
      break
   
   print(f"klien: {pesan}")

   balasan = input("server: ")
   client_socket.send(balasan.encode())

client_socket.close()