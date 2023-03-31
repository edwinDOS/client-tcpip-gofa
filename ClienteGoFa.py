import socket
import time
mi_socket = socket.socket()
mi_socket.connect(("127.0.0.1" , 1025))
respuesta = mi_socket.recv(1024)
print(respuesta)
mi_socket.sendall('Server connected'.encode())

while True:
    print('coordenadas: ')
    datos = input()
    mi_socket.sendall(datos.encode())

    time.sleep(5)