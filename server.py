import socket
import math
import threading
import random

drivers = []
riders = []


def min(a):
    min = a[0]
    index = 0
    i = 0
    for item in a:
        if item < min:
            min = item
            index = i
        i = i+1

    return index

def minimal(a, b):
    #current_rider = a[0]
    distances = []
    x1 = a[0][0]
    y1 = a[0][1]


    for item in b:
        x2 = item[0]
        y2 = item[1]

        distance =  math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))

        distances.append(distance)

    index = min(distances)

    return index

def scheduler():
    threading.Timer(5.0, scheduler).start()
    if len(riders) > 0 and len(drivers) > 0:
        print(riders)
        print(drivers)

        index = minimal(riders, drivers)

        req_rider = riders[0]
        req_driver = drivers[index]

        print(riders[0])
        print(drivers[index])

        rating = random.randint(0, 100)

        db = open("db.txt", "a")

        string_to_write = str(drivers[index][2]) + "," + str(rating) +  "\n"

        db.write(string_to_write)

        del riders[0]
        del drivers[index]

        #return req_rider, req_driver

s = socket.socket()

s.bind(("localhost", 9999))

s.listen(3)
print('Waiting to be connected')

db = open("db.txt", "w+")

db.write("Driver ID,Rating")

i = 0

# req_rider = ""
# req_driver = ""
#
# if not scheduler() is None:
#     req_rider, req_driver = scheduler()

scheduler()

while True:
    c, addr = s.accept()

    co = c.recv(1024).decode()

    x, y, mode, id = co.split(",")

    x = int(x)
    y = int(y)

    co = []
    co.append(x)
    co.append(y)

    if mode == "rider":
        riders.append(co)
        #print('works')
    else:
        co.append(id)
        drivers.append(co)
        # print('works b')

    #scheduler()

    # if i==19:
    #     print(riders)
    #     print(drivers)
    #
    #     index = minimal(riders, drivers)
    #
    #     print(riders[0])
    #     print(drivers[index])
    #
    #     del riders[0]
    #     del drivers[index]
    #
    #     print(riders)
    #     print(drivers)

    #print('Connected with ', addr)

    #a = [5,2,6]

    #print(a[min(a)])

    # if not scheduler() is None:
    #     send_message = "(" + str(req_rider[0]) + "," + str(req_rider[1]) + ")" + "(" + str(req_driver[0]) + "," + str(
    #         req_driver[1]) + ")"
    #
    #     c.send(bytes(send_message, 'utf-8'))
    #
    #     c.close()

    c.send(bytes('Welcome', 'utf-8'))

    c.close()


    i = i+1