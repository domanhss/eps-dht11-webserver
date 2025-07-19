from flask import Flask, request, jsonify, render_template_string
import csv
import datetime

app = Flask(__name__)

# 🔴 Biến toàn cục lưu dữ liệu mới nhất
latest_data = {'temperature': None, 'humidity': None}

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    data = request.get_json()
    print("Received data:", data)

    # Cập nhật dữ liệu mới nhất
    latest_data = {
        'temperature': data.get('temperature'),
        'humidity': data.get('humidity')
    }

    # Lưu vào file CSV
    with open('data_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([now, latest_data['temperature'], latest_data['humidity']])

    return jsonify({'message': 'Data received successfully'}), 200

# 🔍 Route để xem dữ liệu
@app.route('/')
def show_data():
    return render_template_string("""
        <h2>Nhiệt độ & Độ ẩm từ ESP8266</h2>
        <p><strong>Nhiệt độ:</strong> {{ temp }} °C</p>
        <p><strong>Độ ẩm:</strong> {{ hum }} %</p>
        <hr>
        <p>📡 Tự động cập nhật mỗi 10s</p>
        <script>
            setTimeout(() => location.reload(), 10000); // Tự reload sau 10s
        </script>
    """, temp=latest_data['temperature'], hum=latest_data['humidity'])
