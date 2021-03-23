from socket import *

serverName = 'localhost'
serverPort = 65535
serverSocket = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)

number = input('Inserisci il numero da analizzare: ')

clientSocket.sendto(str(number).encode('utf-8'), serverSocket)

try:
    reply, server = clientSocket.recvfrom(2048)
    print(reply.decode('utf-8'))
except:
    print('Exception: timed out')
finally:
    clientSocket.close()