from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sensor_data = []
relay_state = False  # Initial relay state

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

@app.route('/control_relay', methods=['POST'])
# def control_relay():
#     global relay_state
#     data = request.get_json()
#     if 'action' in data:
#         action = data['action']
#         if action == 'on':
#             relay_state = True
#         elif action == 'off':
#             relay_state = False
#         return f"Relay turned {action}", 200
#     else:
#         return "Invalid request", 400
def control_relay(request):
    if request.method == "POST":
        print(request.form)

@app.route('/current_relay_state', methods=['GET'])
def get_relay_state():
    return {"relay_state": relay_state}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
