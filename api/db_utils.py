import ast
from duckdb import DuckDBPyConnection

# Db utils for duckdb



def retrieve_database_duckdb(con: DuckDBPyConnection) -> str:
    '''
    Retrieves all data in the database.

    '''

    query = '''
        SELECT * FROM jlpt_questions
    '''

    con.execute(query)
    
    return con.pl().to_dicts()

def write_line_to_database_duckdb(con: DuckDBPyConnection, data: dict) -> None:
    '''
    Inserts new data to the duckdb database.
    '''

    query = f'''

        INSERT INTO jlpt_questions (question_id, question_str, question_choices, question_answer, question_level, question_explanation, question_type, question_topics)
        VALUES
        (
            {data['question_id']},
            '{data['question_str']}',
            {data['question_choices']},
            '{data['question_answer']}',
            '{data['question_level']}',
            '{data['question_explanation']}',
            '{data['question_type']}',
            '{data['question_topics']}'

        )

    '''

    con.execute(query)
    


def delete_question_database_duckdb(con: DuckDBPyConnection, question_id_data: int) -> None:
    '''
    Delete a specific line/question from duckdb database.
    '''
    question_id_data = str(question_id_data)

    query = f'''

        DELETE FROM jlpt_questions WHERE question_id = {question_id_data}

    '''

    con.execute(query)

def retrieve_random_row_duckdb(con: DuckDBPyConnection) -> str:
    '''
    Retrieves random line from data in the database.

    '''

    query = '''
        SELECT * FROM jlpt_questions 
        ORDER BY RANDOM()
        LIMIT 1
    '''

    con.execute(query)
    
    return con.pl().to_dicts()


def retrieve_unseen_questions_duckdb(con: DuckDBPyConnection, seen_questions: list) -> str:
    '''
    Retrieves random line from data in the database.

    '''
    query = f'''

        SELECT * FROM jlpt_questions 
        WHERE question_id NOT IN {str(tuple(seen_questions))}
    '''

    con.execute(query)

    return con.pl().to_dicts()


# Db utils for file db
DATABASE_FILE_URI = 'database_file.db' # The path of database file

def retrieve_database() -> str:
    '''
    Retrieves all data in the database.

    '''

    data = list()

    with open(DATABASE_FILE_URI, 'r') as f:
        for line in f:
            data.append(ast.literal_eval(line.strip()))
    
    return data

def write_line_to_database(data: dict) -> None:
    '''
    Append new line to the end of the database file.
    '''

    with open(DATABASE_FILE_URI, 'a') as f:
        f.write('\n')
        f.write(str(data))

def write_to_database(data: list) -> None:
    '''
    Truncate and write to database file.

    IMPORTANT: this function erases all previous data.
    '''

    with open(DATABASE_FILE_URI, 'w+') as f:
        for index, line in enumerate(data):
            f.write(str(line))
            if index != len(data) - 1:
                f.write('\n')


def delete_question_database(question_id: int) -> None:
    '''
    Delete a specific line/question from database file.
    '''
    question_id = str(question_id)

    data = retrieve_database()
    for question in data:
        if question['question_id'] == question_id:
            data.remove(question)

    write_to_database(data)