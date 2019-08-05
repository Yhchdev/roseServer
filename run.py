from flask import Flask
from flask_cors import CORS
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

from app.user import user
from app.rose import rose


app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": "*"}})   # 允许所有域名跨域
CORS(app, supports_credentials=True)


app.config['SECRET'] = 'yhchdev'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = '193.112.77.165'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
mqtt = Mqtt(app)
socketio = SocketIO(app)

app.register_blueprint(user, url_prefix = '/user')
app.register_blueprint(rose, url_prefix = '/rose')



@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))



@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    print(message.topic + " " + str(message.payload))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=True, debug=True)