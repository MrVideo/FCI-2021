from socket import *

serverName = 'localhost'
serverPort = 65535
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)

message = input('Inserisci una stringa: ')

clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

try:
    consonant, address = clientSocket.recvfrom(2048)
    consonant = consonant.decode('utf-8')
    print(consonant)
except:
    print('Exception: timed out')
finally:
    clientSocket.close()