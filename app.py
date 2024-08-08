from flask import Flask, request
import json

app: Flask = Flask(__name__)


@app.route("/add/", methods=["POST"])
def add():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = json_data["a"] + json_data["b"]
            return {'result': result}
        except json.JSONDecodeError:
            return 'ERROR::Invalid Input -> input format: {"a":int, "b":int}'

@app.route("/subtract/", methods=["POST"])
def subtract():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = json_data['a'] - json_data['b']
            return {'result': result}
        except json.JSONDecodeError:
            return 'ERROR::Invalid Input -> input format: {"a":int, "b":int}'
        
@app.route("/multiply/", methods=["POST"])
def multiply():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = json_data["a"] * json_data["b"]
            return {'result': result}
        except json.JSONDecodeError:
            return 'ERROR::Invalid Input -> input format: {"a":int, "b":int}'
        
@app.route("/divide/", method=["POST"])
def divide():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = json_data["a"] / json_data["b"]
            return {'result': result}
        except json.JSONDecodeError:
            return 'ERROR::Invalid Input -> input format: {"a":int, "b":int}'


if __name__ == "__main__":
    app.run(debug=True)