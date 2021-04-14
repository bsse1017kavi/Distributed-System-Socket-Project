from flask import Flask,request
from flask_socketio import SocketIO
from flask_apscheduler import APScheduler
import math, random, sqlite3, requests
from flask_sqlalchemy import SQLAlchemy

riders = []
drivers = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
scheduler = APScheduler()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
db = SQLAlchemy(app)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Rating %r>' % self.id

def insert_to_table(id, rating):

    conn = sqlite3.connect('./ratings.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE ratings (id TEXT  NOT NULL, rating TEXT NOT NULL); ''')
    cursor.execute('''INSERT INTO ratings(id, rating) VALUES (?, ?)''', (str(id),str(rating)))

    conn.commit()
    print("Record inserted")
    cursor.execute('select * from ratings')

    conn.close()

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

@app.route('/rating', methods=['POST'])
def rating():
    data = request.form
    rating = int(data['rating'])
    print(rating)

    #rating = random.randint(1,100)
    #insert_to_table(id,rating)

    new_rating = Rating(rating=rating)
    db.session.add(new_rating)
    db.session.commit()

    return ''

@app.route('/rider', methods=['POST','GET'])
def rider():
    data = request.form

    message = str(data['x']) + ',' + str(data['y'])

    print(message)

    co = []
    co.append(data['x'])
    co.append(data['y'])

    riders.append(co)

    #communicate()

    return ''

@app.route('/driver', methods=['POST','GET'])
def driver():
    data = request.form
    # print(data['x'])
    # print(data['y'])

    message = str(data['x']) + ',' + str(data['y'])

    print(message)

    co = []
    co.append(data['x'])
    co.append(data['y'])

    drivers.append(co)

    #communicate()

    return ''


def match_driver_rider():
    messages = []
    if len(riders) > 0 and len(drivers) > 0:
        for i in range((len(riders))):
            index, fair = minimal(riders, drivers)
            req_rider = riders[0]
            req_driver = drivers[index]

            message = "Rider location " + "(" + str(req_rider[0]) + "," + str(
                req_rider[1]) + ")" + " was matched with Driver location" + "(" + str(req_driver[0]) + "," + str(
                req_driver[1]) + ")" + " Fair: " + str(fair) + " Taka"


            #r = requests.post('http://localhost:8000/rating', data=rating_data)

            #rating()

            del riders[0]
            del drivers[index]

            messages.append(message)

    else:
        message = 'Not enough rider or driver yet'
        messages.append(message)

    return messages

@socketio.on('message')
def communicate():
    messages = match_driver_rider()

    for message in messages:
        socketio.emit('message', message, namespace='/communication')

    #socketio.emit('message', 'Not enough rider or driver yet', namespace='/communication')


if __name__ == "__main__":
    #communicate("hello")
    scheduler.add_job(id='Schedule Task', func=communicate, trigger='interval', seconds= 5)
    scheduler.start()
    socketio.run(app, port=8000)

    #app.run(debug=True)
