from flask import Flask, request
from flask_socketio import SocketIO
from flask_apscheduler import APScheduler

messages = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

scheduler = APScheduler()

@app.route('/message', methods=['POST'])
def recieve_message():
    message = request.form['message']
    print(message)
    messages.append(message)
    return ''

@socketio.on('message')
def communicate():

    if len(messages)>0:
        for message in messages:
            socketio.emit('message', message, namespace='/communication')

        del messages[:]

    else:
        # socketio.emit('message', 'Not enough rider or driver yet', namespace='/communication')
        socketio.emit('message', 'Not enough rider or driver yet from communication', namespace='/communication')

if __name__ == "__main__":
    scheduler.add_job(id='Schedule Task', func=communicate, trigger='interval', seconds=5)
    scheduler.start()
    socketio.run(app, host="0.0.0.0", port=9000)