from flask import Flask
from flask import jsonify
from utils.database import get_karakter_by_id
from utils.database import get_username_by_id

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/karakter/<id>")
def get_karakter(id):
    data = get_karakter_by_id(id)
    return jsonify(data)

@app.route("/username/<id>")
def get_username(id):
    data = get_username_by_id(id)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)