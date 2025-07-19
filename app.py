from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "EPS-DHT11-WEB Flask Server is running!"

@app.route('/push', methods=['POST'])
def push_data():
    data = request.get_json()
    print("Dữ liệu nhận:", data)
    return "OK", 200
