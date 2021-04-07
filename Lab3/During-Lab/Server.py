from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

while True:


    connectionSocket, clientAddress = serverSocket.accept()
    print('Richiesta da: ', clientAddress)

    message = connectionSocket.recv(1024)
    message = message.decode('utf-8')
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode('utf-8'))

    connectionSocket.close()