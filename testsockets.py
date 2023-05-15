import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2828))

command = 'rotate_y:3'
sock.sendall(command.encode())

sock.close()
