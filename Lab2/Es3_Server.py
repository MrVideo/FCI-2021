from socket import *

serverPort = 65535

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')

print('Listening...')

while True:
    message, address = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    print('Receiving from: ', address)
    strlen = len(message)
    vow = 0
    for element in vowels:
        strlen = strlen - message.count(element)
    reply = 'La stringa contiene ' + str(strlen) + ' consonanti'
    serverSocket.sendto(reply.encode('utf-8'), address)