from flask import Flask, request, jsonify, render_template_string
import csv
import datetime
import os

app = Flask(__name__)

# 🔴 Biến toàn cục lưu dữ liệu mới nhất
latest_data = {'temperature': None, 'humidity': None, 'timestamp': None}

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    data = request.get_json()
    print("Received data:", data)

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Cập nhật dữ liệu mới nhất
    latest_data = {
        'temperature': data.get('temperature'),
        'humidity': data.get('humidity'),
        'timestamp': now
    }

    # Lưu vào file CSV
    with open('data_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([now, latest_data['temperature'], latest_data['humidity']])

    return jsonify({'message': 'Data received successfully'}), 200

# 🔍 Route để xem dữ liệu
@app.route('/')
def show_data():
    return render_template_string("""
        <h2>THÔNG TIN NHIỆT ĐỘ & ĐỘ ẨM TỪ CĂN HỘ GIA ĐÌNH</h2>
        <p><strong>Nhiệt độ:</strong> {{ temp }} °C</p>
        <p><strong>Độ ẩm:</strong> {{ hum }} %</p>
        <p><strong>Cập nhật lúc:</strong> {{ time }}</p>
        <hr>
        <p>📡 Tự động cập nhật mỗi 10s</p>
        <script>
            setTimeout(() => location.reload(), 10000); // Tự reload sau 10s
        </script>
    """, temp=latest_data['temperature'], hum=latest_data['humidity'], time=latest_data['timestamp'])

# ✅ Cần thêm đoạn này để Render chạy được
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
