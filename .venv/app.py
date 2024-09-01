from flask import Flask, jsonify

app = Flask(__name__)

@app.route(rule:"/api", methods=['GET'])
def hello_world():
    data = {"status":"success"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)