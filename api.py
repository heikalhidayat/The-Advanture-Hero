from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/karakter/<id>")
def get_karakter(id):
    return f"Fetching karakter with ID: {id}"

if __name__ == "__main__":
    app.run(debug=True)