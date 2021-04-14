from socket import *
from time import sleep

serverName = 'localhost'
serverPort = 12000
serverAdd = (serverName, serverPort)

try:
    cSocket = socket(AF_INET, SOCK_STREAM)
    cSocket.connect(serverAdd)

    while True:
        m = input('Inserisci una stringa: ')
        strlen = len(m)
        start = 0
        end = start + 100

        if m == '.':
            cSocket.send(m.encode('utf-8'))
            cSocket.close()
            break
        elif strlen <= 100:
            cSocket.send(m.encode('utf-8'))
        else:
            while strlen > 0:
                mSplit = m[start:end]
                start = end
                end += 100
                cSocket.send(mSplit.encode('utf-8'))
                sleep(2)
                strlen -= 100

except ConnectionRefusedError:
    print('Il server ha rifiutato la connessione')
except BrokenPipeError:
    print('La connessione si è interrotta per motivi sconosciuti')
finally:
    cSocket.close()