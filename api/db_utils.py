import ast

DATABASE_URI = 'data.db' # The path of database file

def retrieve_database() -> str:
    '''
    Retrieves all data in the database.

    '''

    data = list()

    with open(DATABASE_URI, 'r') as f:
        for line in f:
            data.append(ast.literal_eval(line.strip()))
    
    return data

def write_line_to_database(data: dict) -> None:
    '''
    Append new line to the end of the database file.
    '''

    with open(DATABASE_URI, 'a') as f:
        f.write('\n')
        f.write(str(data))

def write_to_database(data: list) -> None:
    '''
    Truncate and write to database file.

    IMPORTANT: this function erases all previous data.
    '''

    with open(DATABASE_URI, 'w+') as f:
        for index, line in enumerate(data):
            f.write(str(line))
            if index != len(data) - 1:
                f.write('\n')


def delete_question_database(question_id: int) -> None:
    '''
    Delete a specific line/question from database file.
    '''

    data = retrieve_database()
    for question in data:
        if question['question_id'] == question_id:
            data.remove(question)

    write_to_database(data)