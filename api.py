from flask import (Flask, jsonify, request)

from utils.database import get_by_id

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running"

@app.route("/username/<id>")
def get_user(id):
    data = get_by_id("username", "id_player", id)
    return jsonify(data)

@app.route("/inventory/<id>")
def get_inventory(id):
    data = get_by_id("invetory", "id_item", id)
    return jsonify(data)

@app.route("/pocket/<id>")
def get_pocket(id):
    data = get_by_id("pocket", "id_pocket", id)
    return jsonify(data)

@app.route("/karakter/<id>")
def get_karakter(id):
    data = get_by_id("karakter", "id_karakter", id)
    return jsonify(data)

@app.route("/skills/<id>")
def get_skills(id):
    data = get_by_id("skills", "id_skills", id)
    return jsonify(data)

@app.route("/equipment/<id>")
def get_equipment(id):
    data = get_by_id("equipment", "id_equipment", id)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)