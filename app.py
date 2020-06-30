from flask import Flask, jsonify, request

app = Flask(__name__)
client = app.test_client()

tutorials = [
    {
        'id': 1,
        'title': 'video #1. Intro',
        'description': 'GET, POST routes'
    },
    {
        'id': 2,
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


@app.route('/tutorials/<int:tutorial_id>', methods=["PUT"])
def update_tutorial(tutorial_id):
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    params = request.json
    if not item:
        return {'message': 'No tutorials found'}, 400
    item.update(params)
    return item


@app.route('/tutorials/<int:tutorial_id>', methods=["DELETE"])
def delete_tutorial(tutorial_id):
    idx, _ = next((x for x in enumerate(tutorials)
                  if x[1]['id'] == tutorial_id), (None, None))
    tutorials.pop(idx)
    return '', 204


if __name__ == "__main__":
    app.run()
