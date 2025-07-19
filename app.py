from flask import Flask, request, jsonify

app = Flask(__name__)

# Route chính để kiểm tra server hoạt động
@app.route('/')
def index():
    return '✅ Flask server is running!'

# Route để nhận dữ liệu POST từ ESP8266
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Nhận dữ liệu từ ESP8266:", data)
    return jsonify({"status": "received", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
