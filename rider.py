import socket
#from random import seed
#from random import randint
import random

def connect_to_server():
    x = random.randint(-180, 180)

    y = random.randint(-180, 180)

    # print(x)
    # print(y)

    co = str(x) + "," + str(y) + ",rider,0";

    # for i in range(10):
    #     v = randint(-180,180)
    #     print(v)

    print(co)

    c = socket.socket()

    c.connect(("localhost", 9999))

    # name = input("Give your name: ")

    c.send(bytes(co, 'utf-8'))

    print(c.recv(1024).decode())

for i in range(10):
    connect_to_server()