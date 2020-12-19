import time
import socket
import os
from _thread import *

# Create TCP socket
ServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Prevent "address in use" on server restart
ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# variable declaration
host = ''
port = 8887
ThreadCount = 0

# Binding and binding error catch
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

# Clear terminal
os.system('clear')
# Socket listening
print('Waiting for a Connection..')
ServerSocket.listen(5)



welcome = "Welcome to the Server! :D\n**To disconnect press CTRL+C** "
def threaded_client(connection, addr):
    try:
        connection.send(welcome.encode(encoding='UTF-8',errors='strict'))
        while True:
            data = connection.recv(2048)
            reply = 'Server Says: '+ data.decode('UTF-8')
            print("Sent: \""+str(data.decode())+"\" to client: "+str(addr))
            if not data:
                break
            connection.sendall(reply.encode(encoding='UTF-8',errors='strict'))
    except socket.error as e:
        print("Socket error: %s" % str(e))

    connection.close()

# Multithreading code 
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, address ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()

