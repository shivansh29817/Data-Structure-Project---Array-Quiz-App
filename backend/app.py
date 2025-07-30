from flask import Flask, jsonify, request
from flask_cors import CORS
from quiz_data.questions import get_fixed_questions, add_question, get_all_questions

app = Flask(__name__)
CORS(app)

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    return jsonify(get_all_questions())

@app.route('/api/quiz', methods=['POST'])
def post_question():
    data = request.get_json()
    if not data or not all(k in data for k in ("question", "options", "answer")):
        return jsonify({"error": "Missing fields"}), 400

    added = add_question(data["question"], data["options"], data["answer"])
    return jsonify({"message": "Question added successfully", "question": added}), 201

if __name__ == '__main__':
    app.run(debug=True)
