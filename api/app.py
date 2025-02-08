from flask import Flask, jsonify, request
import db_utils

app = Flask(__name__)


@app.route('/questions/all', methods=['GET'])
def get_all_questions():
    return jsonify(db_utils.retrieve_database())

@app.route('/questions/new', methods=['POST'])
def add_question():
    question_data = request.get_json(force=True)
    db_utils.write_line_to_database(question_data)
    return question_data

@app.route('/questions/del/<question_id>', methods=['POST'])
def del_question(question_id):
    db_utils.delete_question_database(int(question_id))
    return f'Question {question_id} was deleted. If it doesn\'t exist, nothing was done!'

if __name__ == '__main__':
    app.run(port=5000)