from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = input('Inserisci una stringa (per uscire, inserisci .): ')

    clientSocket.send(message.encode('utf-8'))
    if message == '.':
        break

    modifiedMessage = clientSocket.recv(1024)
    print('Messaggio del server: ', modifiedMessage.decode('utf-8'))

clientSocket.close()