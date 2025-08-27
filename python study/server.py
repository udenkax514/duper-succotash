from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import index   # this imports your chatbot backend (index.py)

app = Flask(__name__)
CORS(app)

# ---- API routes ----
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_question = data.get("question", "")
    answer = index.get_answer(user_question)   # call your backend logic
    return jsonify({"answer": answer})

@app.route("/teach", methods=["POST"])
def teach():
    data = request.get_json()
    question = data.get("question")
    answer = data.get("answer")
    index.add_knowledge(question, answer)      # update JSON memory
    return jsonify({"message": "Learned new response!"})

# ---- Serve frontend ----
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(debug=True)


