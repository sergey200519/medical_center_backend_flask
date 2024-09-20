import json

from collections import OrderedDict

from flask import Flask, jsonify, logging, request
from flask_cors import CORS


from models.Reviews import Review
from ORM import ORM

app = Flask(__name__)
app.json.sort_keys = False

CORS(app)

database = ORM()

@app.route("/")
def index():
    return "Hi"

@app.route("/reviews/", methods=["GET"])
def get_reviews():
    return jsonify(database.get_all(Review))

@app.route("/reviews/", methods=["POST"])
def add_reviews():
    try:
        return jsonify(database.insert(Review, request.json))
    except Exception:
        print("Error inserting review")
        return jsonify({
            "status": "error"
        })
    
@app.route("/services/dentistry", methods=["GET"])
def add_dentistry():
    with open("services.json", encoding="utf-8") as json_file:
        data = OrderedDict(json.load(json_file, object_pairs_hook=OrderedDict))
    # print(data)
    # print("-\n-\n-\n")
    # print(dict(reversed(data.items())))
    return jsonify(data)

@app.route("/services/laboratory", methods=["GET"])
def add_dentistry():
    with open("services_lab.json", encoding="utf-8") as json_file:
        data = OrderedDict(json.load(json_file, object_pairs_hook=OrderedDict))
    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)
    logging.getLogger("flask_cors").level = logging.DEBUG
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)
#     logging.getLogger("flask_cors").level = logging.DEBUG