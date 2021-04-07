from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

message = input('Inserisci una stringa: ')
clientSocket.send(message.encode('utf-8'))

modifiedMessage = clientSocket.recv(1024)
print('Messaggio del server: ', modifiedMessage.decode('utf-8'))

clientSocket.close()