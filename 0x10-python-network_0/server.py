from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def data():
    if request.is_json:
        content = request.get_json()
        return jsonify({"message": "Valid JSON", "data": content}), 200
    return jsonify({"message": "Not a valid JSON"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
