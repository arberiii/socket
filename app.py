from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message from user', namespace="/messages")
def receive_message_from_user(message):
    print('USER MESSAGE: {}'.format(message))
    emit('from flask', message.upper(), broadcast=True)

'''
@socketio.on('message')
def receive_message(message):
    print('########: {}'.format(message))
    send('This is a message from Flask.')

@socketio.on('custom event')
def receive_custom_event(message):
    print('THE CUSTOM MESSAGE IS: {}'.format(message['name']))
    emit('from flask', {'extension' : 'Flask-SocketIO'}, json=True)

'''

@app.route('/orginate')
def orginate():
    socketio.emit("server originated", "something you can't relate client")
    return "<h1>Sent!</h1"

if __name__ == '__main__':
    socketio.run(app)