from flask import Flask, jsonify
from flask_cors import CORS
from quiz_data.questions import get_fixed_questions

app = Flask(__name__)
CORS(app)

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    quiz = get_fixed_questions()
    return jsonify(quiz)


if __name__ == '__main__':
    app.run(debug=True)
