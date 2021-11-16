import socket
 # Создать сокет
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # Установить IP и порт
host = socket.gethostname()
port = 3333
 # bind привязать порт
mySocket.bind((host, port))
 # Монитор
mySocket.listen(10)
 
while True:
    # Получить клиентское соединение
    print ("Ожидание подключения ....")
    client, address = mySocket.accept()
    #print ('«Новое соединение»')
    print("IP is %s" % address[0])
    print("port is %d\n" % address[1])
 
    while True:
        #   Послать сообщение 
        msg = input ("---------------------- Send:")
        client.send(msg.encode(encoding='UTF-8'))
        #print ("Отправка завершена")
        if msg == "EOF":
            break
        if msg == "quit":
            client.close()
            mySocket.close()
            print ("Конец программы \ n")
            exit()
        # Прочитать сообщение
        msg = client.recv(1024).decode(encoding='UTF-8')
        print ("---------------------- Read:", msg)
        #print ('«Чтение завершено»')
        if msg == b"EOF":
            break
        if msg == b"quit":
            client.close()
            mySocket.close()
            print ("Конец программы \ n")
            exit()