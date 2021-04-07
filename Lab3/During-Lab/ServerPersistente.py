from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    print('Connection request from ', str(clientAddress))

    while True:
        string = connectionSocket.recv(1024)
        string = string.decode('utf-8')
        if string == '.':
            connectionSocket.close()
            break
        else:
            upStr = string.upper()
            connectionSocket.send(upStr.encode('utf-8'))