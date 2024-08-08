from flask import Flask, request
import json

app: Flask = Flask(__name__)


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        data: bytes = request.get_data()
        json_data: dict = json.loads(data)
        return {'result': sum(json_data.values())}


if __name__ == "__main__":
    app.run(debug=True)