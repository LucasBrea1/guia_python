import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("192.2.6.109", 12345))

s.send("Hola, servidor".encode())

response = s.recv(1024).decode()

print(response)