from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/about")
def about():
    data = {"name": "John", "age": 30,
            "date": "2023-01-01", "programming": "Python"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
