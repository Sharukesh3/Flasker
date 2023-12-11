from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sensor_data = []

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if 'sensor_data' in data:
        sensor_value = data['sensor_data']
        sensor_data.append(sensor_value)
        return "Data received and stored: {}".format(sensor_value), 200
    else:
        return "Invalid data format", 400

@app.route('/sensor_values', methods=['GET'])
def get_sensor_values():
    return {"sensor_data": sensor_data}

@app.route('/button')
def button():
    return render_template('button.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
