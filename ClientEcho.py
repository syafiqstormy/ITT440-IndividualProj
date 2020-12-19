import os
import socket
import sys
import signal

# Signal handler
def signal_handler(sig,frame):
    print("\nYou pressed Ctrl+C!\nExiting program...")
    sys.exit(0)

# code for Ctrl+C catch
signal.signal(signal.SIGINT, signal_handler)

ClientSocket = socket.socket()
host = '192.168.0.66'
port = 8887

# Clearing terminal
os.system('clear')
print('Waiting for connection')

# catch error if socket has problem connecting to server
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode('UTF-8'))

while True:
    Input = input('Say Something : ')

# Empty input error checking
    if Input =='':
      print("Input is empty!")
      Input= input('Say Something that is not empty! : ')

    ClientSocket.send(Input.encode(encoding='UTF-8',errors='strict'))
    Response = ClientSocket.recv(1024)
    if len(Response)!= 0:
      print(Response.decode('UTF-8'))
    else:
      print("****Server has unexpectedly closed connection****")
      ClientSocket.close()
      sys.exit(0)

ClientSocket.close()

