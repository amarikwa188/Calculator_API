from flask import Flask, request
import json

app: Flask = Flask(__name__)


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = json_data["a"] + json_data["b"]
            return {'result': result}
        except json.JSONDecodeError:
            return {'error': 'invalid input: input format -> '\
                    '{"a":int, "b":int}'}

@app.route("/subtract", methods=["POST"])
def subtract():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = json_data['a'] - json_data['b']
            return {'result': result}
        except json.JSONDecodeError:
            return {'error': 'invalid input: input format -> '\
                    '{"a":int, "b":int}'}
        
@app.route("/multiply", methods=["POST"])
def multiply():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = json_data["a"] * json_data["b"]
            return {'result': result}
        except json.JSONDecodeError:
            return {'error': 'invalid input: input format -> '\
                    '{"a":int, "b":int}'}
        
@app.route("/divide", methods=["POST"])
def divide():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)

            result: int = round(json_data["a"] / json_data["b"], 3)
            return {'result': result}
        except json.JSONDecodeError:
            return {'error': 'invalid input: input format -> '\
                    '{"a":int, "b":int}'}
        except ZeroDivisionError:
            return {'error': 'divisor cannot be zero'}
        
@app.route("/sum", methods=["POST"])
def sum_array():
    if request.method == "POST":
        try:
            data: bytes = request.get_data()
            json_data: dict = json.loads(data)
            result: int = sum(json_data["nums"])
            return {'result': result}
        except json.JSONDecodeError:
            return 'ERROR::Invalid Input -> input format: '\
                   '{"nums": [a: int, b: int, c: int...]}'


if __name__ == "__main__":
    app.run(debug=True)