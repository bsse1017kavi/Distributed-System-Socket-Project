import requests, socketio, random
from flask_apscheduler import APScheduler

scheduler = APScheduler()

c = socketio.Client()
c.connect("http://localhost:8000", namespaces=['/communication'])

#function name should be same as event of server
@c.event(namespace='/communication')
def message(data):
    #print(1)
    print(data)


def request_to_server():
    for i in range(10):
        # Rider Client
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)

        data = \
            {
                'x': x,
                'y': y,
            }

        r = requests.post(url="http://localhost:8000/rider", data=data)

        # Driver Client
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)

        data = \
            {
                'x': x,
                'y': y,
            }

        r = requests.post(url="http://localhost:8000/driver", data=data)


scheduler.add_job(id='New Task', func=request_to_server, trigger='interval', seconds=5)
scheduler.start()
