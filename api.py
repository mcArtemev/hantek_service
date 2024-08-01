from flask import Flask, request, jsonify
from GPS.gps_reader import GPSReader
from MDNS.mdns_service import MDNSService

app = Flask(__name__)

@app.route('/api/oscilloscope', methods=['GET'])
def get_oscilloscope_data():
    data = {
        'channel1': [0, 1, 2, 3, 4],
        'channel2': [5, 6, 7, 8, 9]
    }
    return jsonify(data)


@app.route('/api/attenuator', methods=['POST'])
def control_attenuator():
    command = request.json.get('command')
    if attenuator_controller:
        attenuator_controller.send_command(command)
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error', 'message': 'Attenuator controller not initialized'}), 500


def start_api(scanner, attenuator_ctrl):
    global attenuator_controller
    attenuator_controller = attenuator_ctrl

    scanner.start()
    gps_reader = GPSReader(scanner)
    gps_reader.start()
    attenuator_controller.start()

    mdns_service = MDNSService()
    mdns_service.register_service()

    app.run(host='0.0.0.0', port=5000)
