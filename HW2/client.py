#!/usr/bin/python3

import socket

MAX_FILE_SIZE = 1024

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "18.217.224.154"

port = 60000

print("Connecting to " + host + ":" + port.__str__())

clientSocket.connect((host, port))

print("Connected!")

f = open("test.txt", 'rb')

l = f.read(MAX_FILE_SIZE)

clientSocket.send(l)

f.close()

clientSocket.shutdown(socket.SHUT_WR)
print("Finished, server responds with")
print(clientSocket.recv(1024).decode('utf-8'))

clientSocket.close()
