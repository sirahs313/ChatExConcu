import socket
import threading


host = '192.168.56.1'
port = 9999

def receive_messages(client_socket):

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Error al recibir el mensaje")
            client_socket.close()
            break

def start_client():
  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

   
    username = input("Ingresa tu usuario: ")
    password = input("Ingresa tu contraseña: ")
    client_socket.send(username.encode('utf-8'))
    client_socket.send(password.encode('utf-8'))

  
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        
        message = input()
        client_socket.send(message.encode('utf-8'))

#Inicio cliente
start_client()
