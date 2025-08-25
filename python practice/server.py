from flask import Flask, request, jsonify, send_from_directory
import tictac

app = Flask(__name__, static_folder=".")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    pos = data["position"]
    result = tictac.make_move(pos)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


