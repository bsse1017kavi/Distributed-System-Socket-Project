import time

import requests, socketio, random
from flask_apscheduler import APScheduler

#scheduler = APScheduler()

c = socketio.Client()
c.connect("http://communication.chittagong.com:9000", namespaces=['/communication'])

#function name should be same as event of server
@c.event(namespace='/communication')
def message(data):
    #print(1)
    print(data)

    rating = random.randint(1,100)

    data = {'rating': rating, 'location': 'chittagong'}

    r = requests.post(url="http://server.chittagong.com:8005/rating", data=data)
    #r = requests.post(url="http://127.0.0.1:8002/rating", data=data)


def request_to_server():
    for i in range(10):
        # print("hello")
        # Rider Client
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)

        data = \
            {
                'x': x,
                'y': y,
            }
        #print(data)

        r = requests.post(url="http://server.chittagong.com:8005/rider", data=data)
        #r = requests.post(url="http://127.0.0.1:8002/rider", data=data)

        # Driver Client
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)

        data = \
            {
                'x': x,
                'y': y,
            }

        #print(data)
    #
        r = requests.post(url="http://server.chittagong.com:8005/driver", data=data)
        #r = requests.post(url="http://127.0.0.1:8002/driver", data=data)

# scheduler.add_job(id='New Task', func=request_to_server, trigger='interval', seconds=5)
# scheduler.start()

while True:
    request_to_server()
    time.sleep(4)
    # print("Hello")
    # time.sleep(4)