from flask import Flask, request
import math, requests
from flask_apscheduler import APScheduler

drivers = []
riders = []

scheduler = APScheduler()

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

@app.route('/rider', methods=['POST','GET'])
def rider():
    data = request.form

    message = str(data['x']) + ',' + str(data['y'])

    print(message)

    co = []
    co.append(data['x'])
    co.append(data['y'])

    riders.append(co)

    return ''

@app.route('/driver', methods=['POST','GET'])
def driver():
    data = request.form

    message = str(data['x']) + ',' + str(data['y'])

    print(message)

    co = []
    co.append(data['x'])
    co.append(data['y'])

    drivers.append(co)

    return ''

def match_driver_rider():
    #messages = []
    if len(riders) > 0 and len(drivers) > 0:
        for i in range((len(riders))):
            index, fair = minimal(riders, drivers)
            req_rider = riders[0]
            req_driver = drivers[index]

            message = "Rider location " + "(" + str(req_rider[0]) + "," + str(
                req_rider[1]) + ")" + " was matched with Driver location" + "(" + str(req_driver[0]) + "," + str(
                req_driver[1]) + ")" + " Fair: " + str(fair) + " Taka"

            #print(message)

            data = {'message': message}

            r = requests.post('http://localhost:9000/message', data=data)

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
    app.run(debug=True, host="localhost", port=8000)