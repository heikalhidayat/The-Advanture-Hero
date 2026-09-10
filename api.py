from flask import (Flask, jsonify, request)

from utils.database import (
    get_username_by_id, get_inventory_by_id, get_pocket_by_id,
    get_karakter_by_id, get_skills_by_id, get_equipment_by_id,
    get_by_id
)

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
    data = get_inventory_by_id(id)
    return jsonify(data)

@app.route("/pocket/<id>")
def get_pocket(id):
    data = get_pocket_by_id(id)
    return jsonify(data)

@app.route("/karakter/<id>")
def get_karakter(id):
    data = get_karakter_by_id(id)
    return jsonify(data)

@app.route("/skills/<id>")
def get_skills(id):
    data = get_skills_by_id(id)
    return jsonify(data)

@app.route("/equipment/<id>")
def get_equipment(id):
    data = get_equipment_by_id(id)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)