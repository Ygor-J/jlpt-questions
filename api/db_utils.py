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
    
    return con.fetchall()

def write_line_to_database_duckdb(con: DuckDBPyConnection, data: dict) -> None:
    '''
    Inserts new data to the duckdb database.
    '''

    question_id_data, question_str_data, question_choices_data, question_answer_data = data.values()

    query = f'''

        INSERT INTO jlpt_questions (question_id, question_str, question_choices, question_answer)
        VALUES
        (
            {question_id_data},
            {question_str_data},
            {question_choices_data},
            {question_answer_data}
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