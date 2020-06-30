from flask import Flask, jsonify, request

app = Flask(__name__)
client = app.test_client()

tutorials = [
    {
        'title': 'video #1. Intro',
        'description': 'GET, POST routes'
    },
    {
        'title': 'video #2. More features',
        'description': 'GET, POST routes'
    }
]


@app.route('/tutorials', methods=["GET"])
def get_list():
    return jsonify(tutorials)


@app.route('/tutorials', methods=["POST"])
def update_list():
    data = request.json
    tutorials.append(data)
    return jsonify(tutorials)


if __name__ == "__main__":
    app.run()
