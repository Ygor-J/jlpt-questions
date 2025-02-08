from flask import Flask, jsonify, request, session
import duckdb
import db_utils
import random
from dotenv import load_dotenv
import os

DUCKDB_URI = 'database_duckdb.db' # The path of duckdb database

load_dotenv('../.env')

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
con = duckdb.connect(DUCKDB_URI)

@app.route('/questions/all', methods=['GET'])
def get_all_questions():
    return jsonify(db_utils.retrieve_database_duckdb(con))

@app.route('/questions/new', methods=['POST'])
def add_question():
    question_data = request.get_json(force=True)
    db_utils.write_line_to_database_duckdb(con, question_data)
    return question_data

@app.route('/questions/del/<question_id>', methods=['DELETE'])
def del_question(question_id):
    db_utils.delete_question_database_duckdb(con, question_id)
    return f'Question {question_id} was deleted. If it doesn\'t exist, nothing was done!'

@app.route('/questions/random', methods=['GET'])
def get_random_question():
    if 'seen_questions' not in session:
        session['seen_questions'] = list()
    
    if session['seen_questions'] == list():
        random_question = db_utils.retrieve_random_row_duckdb(con)[0]
        session['seen_questions'].append(random_question['question_id'])
        session.modified = True
        return jsonify(random_question)
    else:
        unseen_questions = db_utils.retrieve_unseen_questions_duckdb(con, session['seen_questions'])
        if unseen_questions == list():
            random_question = db_utils.retrieve_random_row_duckdb(con)[0]
            session['seen_questions'] = list()
            session['seen_questions'].append(random_question['question_id'])
        else:
            random_question = random.choice(unseen_questions)
            session['seen_questions'].append(random_question['question_id'])

        session.modified = True
        return jsonify(random_question)

if __name__ == '__main__':
    app.run(port=5000)