import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("localhost",12345))

data, addr = s.recvfrom(1024)

s.sendto("Message for client".encode(), addr)

print(data)