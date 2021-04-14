from socket import *

serverPort = 12000
serverAdd = ('', serverPort)

sSocket = socket(AF_INET, SOCK_STREAM)
sSocket.bind(serverAdd)
sSocket.listen(1)

print('Server ready')

while True:
    conSocket, cAdd = sSocket.accept()
    print('Connection to ', cAdd, ' established')
    num = 0

    while True:
        m = conSocket.recv(2048)
        m = m.decode('utf-8')
        if m == '.':
            conSocket.close()
            print(cAdd, ' disconnected from server')
            break
        else:
            strlen = len(m)
            print('Segment ', str(num), ': ', strlen, ' characters')
            num += 1