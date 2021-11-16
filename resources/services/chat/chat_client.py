import socket
# Создать сокет
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Установить ip и порт
host = socket.gethostname()
port = 3333
# Подключиться к серверу
mySocket.connect((host, port))
#print("Подключиться к серверу")

while True:
    
    msg = mySocket.recv(1024).decode(encoding='UTF-8')
    print("%s" % msg)
    
    if msg == b"EOF":
        break
    if msg == b"quit":
        mySocket.close()
        print("Конец программы \ n")
        exit()
    msg = input("---------------------- Send:")
    mySocket.send(msg.encode(encoding='UTF-8'))
    if msg == "EOF":
        break
    if msg == "quit":
        mySocket.close()
        print("Конец программы \ n")
        exit()
print("Конец программы \ n")
