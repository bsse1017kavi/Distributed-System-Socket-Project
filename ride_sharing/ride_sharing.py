import flask
from flask import Flask, request
import math, requests
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

drivers = []
riders = []

scheduler = APScheduler()
#scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': '2'})

app = Flask(__name__)

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
    x1 = int(a[0][0])
    y1 = int(a[0][1])


    for item in b:
        x2 = int(item[0])
        y2 = int(item[1])

        distance =  math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))

        distances.append(distance)

    index = min(distances)

    fair = int(distances[index] * 10)

    return index, fair

@app.route('/rider', methods=['POST'])
def rider():
    data = request.form
    #
    #message = str(data['x']) + ',' + str(data['y'])
    #
    # print(message)
    #
    co = []
    co.append(data['x'])
    co.append(data['y'])
    #
    riders.append(co)

    return flask.Response(status=201)

@app.route('/driver', methods=['POST'])
def driver():
    data = request.form

    message = str(data['x']) + ',' + str(data['y'])

    print(message)

    co = []
    co.append(data['x'])
    co.append(data['y'])

    drivers.append(co)

    return {"x":1}

def match_driver_rider():
    print(drivers)
    print(riders)
    #messages = []
    if len(riders) > 0 and len(drivers) > 0:
        for i in range((len(riders))):
            index, fair = minimal(riders, drivers)
            req_rider = riders[0]
            req_driver = drivers[index]

            message = "Rider location " + "(" + str(req_rider[0]) + "," + str(
                req_rider[1]) + ")" + " was matched with Driver location" + "(" + str(req_driver[0]) + "," + str(
                req_driver[1]) + ")" + " Fair: " + str(fair) + " Taka"

            print(message)

            data = {'message': message}

            r = requests.post('http://communication:9000/message', data=data)
            #r = requests.post('http://0.0.0.0:9000/message', data=data)

            del riders[0]
            del drivers[index]

            #messages.append(message)

    else:
        message = 'Not enough rider or driver yet'
        #messages.append(message)

    #return messages

if __name__ == "__main__":
    scheduler.add_job(id='Schedule Task', func=match_driver_rider, trigger='interval', seconds=5)
    scheduler.start()
    app.run(debug=True, host="0.0.0.0", port=8000)