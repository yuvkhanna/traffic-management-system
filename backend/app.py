from flask import Flask, request, jsonify
from traffic_control import control_traffic_signal
from congestion_prediction import predict_congestion
from route_optimization import get_optimized_route

app = Flask(__name__)

# Endpoint to control traffic signals
@app.route('/control_signal', methods=['POST'])
def control_signal():
    signal_id = request.json['signal_id']
    action = request.json['action']
    response = control_traffic_signal(signal_id, action)
    return jsonify({"status": "success", "response": response})

# Endpoint to predict congestion
@app.route('/predict_congestion', methods=['POST'])
def congestion():
    location = request.json['location']
    time = request.json['time']
    prediction = predict_congestion(location, time)
    return jsonify({"congestion_level": prediction})

# Endpoint to get an optimized route
@app.route('/optimized_route', methods=['POST'])
def optimized_route():
    start = request.json['start']
    destination = request.json['destination']
    route = get_optimized_route(start, destination)
    return jsonify({"route": route})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
