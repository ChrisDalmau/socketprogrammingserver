#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple, single threaded http web server

import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Prepare a sever socket

# Fill in start
serverPort = 8000

serverSocket.bind(("10.0.0.255",serverPort))
serverSocket.listen(1)
# Fill in end



while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    print("\nReceived a request from: {}".format(addr))

    try:
        message = connectionSocket.recv(1024).decode()

        filename = message.split()[1].decode()
        filename = "index.html" if filename == "/" else filename[1:]
        print("filename: {}".format(filename))

        #read the file and put the content in variable outputdata
        with open(filename, 'r') as file:
            outputdata = file.readlines()

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK".encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found".encode())
        connectionSocket.send("Not Found".encode())
        # Fill in end
        
        # Close client socket

        # Fill in start
        connectionSocket.close()
        #Fill in close
        

serverSocket.close()
sys.exit(0)  # Terminate the program after sending the corresponding data
