from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "ESP8266 DHT11 Web Server Đang hoạt động!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
