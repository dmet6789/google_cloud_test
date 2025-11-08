# requirements.txt
# Flask==3.0.0

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/hora', methods=['GET'])
def obtener_hora():
    """
    Endpoint que devuelve la hora actual en formato JSON
    """
    hora_actual = datetime.now()
    
    respuesta = {
        'hora': hora_actual.strftime('%H:%M:%S'),
        'fecha': hora_actual.strftime('%Y-%m-%d'),
        'timestamp': hora_actual.isoformat(),
        'unix_timestamp': int(hora_actual.timestamp())
    }
    
    return jsonify(respuesta)

@app.route('/', methods=['GET'])
def inicio():
    """
    Endpoint principal con información de uso
    """
    return jsonify({
        'mensaje': 'Servicio REST de hora actual',
        'endpoints': {
            '/hora': 'Devuelve la hora actual en formato JSON'
        }
    })

if __name__ == '__main__':
    print("Servidor iniciado en http://localhost:5000")
    print("Prueba el endpoint: http://localhost:5000/hora")
    app.run(debug=True, host='0.0.0.0', port=5000)