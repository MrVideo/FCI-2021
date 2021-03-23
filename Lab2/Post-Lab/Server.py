from socket import *
from sympy import isprime

serverName = ''
serverPort = 65535
server = (serverName, serverPort)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(server)

print('Listening...')

while True:
    number, client = serverSocket.recvfrom(2048)
    isPrime = isprime(int(number.decode('utf-8')))
    if isPrime:
        reply = 'Il numero è primo'
    else:
        reply = 'Il numero non è primo'
    serverSocket.sendto(reply.encode('utf-8'), client)
