from flask import Flask, request
import json

app: Flask = Flask(__name__)


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = sum(json_data.values())
            return {'result': result}
        except json.JSONDecodeError:
            return 'ERROR::Invalid Input -> input format: {"a":int, "b":int}'

@app.route("/subtract", methods=["POST"])
def subtract():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = json_data['a'] - json_data['b']
            return {'result': result}
        except json.JSONDecodeError:
            return 'ERROR::Invalid Input -> input format: {"a":int, "b":int}'

if __name__ == "__main__":
    app.run(debug=True)