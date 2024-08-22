import json
from flask import Flask, jsonify, logging, request
from flask_cors import CORS


from models.Reviews import Review
from ORM import ORM

app = Flask(__name__)
CORS(app)

database = ORM()

@app.route("/")
def index():
    return "Hi"

@app.route('/reviews/', methods=['GET'])
def get_reviews():
    return jsonify(database.get_all(Review))

@app.route('/reviews/', methods=['POST'])
def add_reviews():
    try:
        return jsonify(database.insert(Review, request.json))
    except Exception:
        print("Error inserting review")
        return jsonify({
            "status": "error"
        })


if __name__ == '__main__':
    app.run(debug=True)
    logging.getLogger('flask_cors').level = logging.DEBUG