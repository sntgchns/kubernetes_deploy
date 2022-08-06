from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello from Kubernetes', 'time': time.strftime("%Y-%m-%d %H:%M:%S")})

if __name__ == '__main__':
    app.run(debug=True, port=5000)