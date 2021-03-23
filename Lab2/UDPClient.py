from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM) #AF_INET indica IPV4, AF_INET6 indica IPV6
clientSocket.settimeout(5)

message = input('Inserisci lettere: ')

clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

try:
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    modifiedMessage = modifiedMessage.decode('utf-8')
    print(modifiedMessage)
except:
    print('Exception: timed out')
finally:
    clientSocket.close()