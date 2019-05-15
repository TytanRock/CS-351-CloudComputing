#!/usr/bin/python3

import socket

MAX_FILE_SIZE = 1024

serverSocket = socket.socket()

host = socket.gethostname()

port = 60000

print("Binding to: " + host + ":" + port.__str__())

serverSocket.bind((host, port))

print("Configuring Listen")

serverSocket.listen(10)

s, addr = serverSocket.accept()

print("Connection from " + addr.__str__())

rec = s.recv(MAX_FILE_SIZE).decode('utf-8')

print("Client sent: " + rec)

charCount = 0
wordCount = 0
lineCount = 0

lastWasWhitespace = True
for char in rec:
    charCount += 1
    if(char == ' ' or char == '\t' or char == '\n') and not lastWasWhitespace:
        wordCount += 1
        lastWasWhitespace = True
    else:
        lastWasWhitespace = False
    if(char == '\n'):
        lineCount += 1

print("Found " + charCount.__str__() + " chars, "
	+ wordCount.__str__() + " words, and " + lineCount.__str__() +
	" lines")

s.send(bytes("Chars are: " + charCount.__str__() + 
	"\nWords are: " + wordCount.__str__() + 
	"\nLines are: " + lineCount.__str__(), 'utf-8'))

