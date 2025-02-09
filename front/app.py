import requests
import streamlit as st
import ast

API_URL = 'http://localhost:5000/'

st.header('JLPT Questions')

st.divider()

class APIUtils:
    
    @staticmethod
    def get_random_question():
        if 'random_question' not in st.session_state:
            st.session_state['random_question'] = requests.get(API_URL + 'questions/random').json()
            return st.session_state['random_question']
    
        return st.session_state['random_question'] 
    
    @staticmethod
    def get_choices(possible_choices_str):
        possible_choices_str = ast.literal_eval(question.get('question_choices'))
        possible_choices = list()
        for key, value in possible_choices_str.items():
            possible_choices.append(f'{key}: {value}')
        return possible_choices


with st.form("question_form"):
    
    question = APIUtils.get_random_question()

    st.write(question.get('question_str'))

    possible_choices_str = ast.literal_eval(question.get('question_choices'))
    choice = st.radio('Choices:', options=APIUtils.get_choices(possible_choices_str), index=None)

    column1, *_, column2 = st.columns(4)

    with column1:
        submmit_button = st.form_submit_button('Submit')
        if 'correct_answer' not in st.session_state:
            st.session_state['correct_answer'] = False
    with column2:
        next_button = st.form_submit_button('Next Question')

    if submmit_button:
        if choice[0] == question.get('question_answer'):
            st.write(':green[You got it right!]')
            st.session_state['correct_answer'] = True
        else:
            st.write(':red[You got it wrong!]!')
            st.write('The correct answer was: :green[{}. {}]'.format(question.get('question_answer'), possible_choices_str.get(question.get('question_answer'))))
            st.session_state['correct_answer'] = False
    if next_button:
        if st.session_state['correct_answer'] == True:
            del st.session_state['random_question']
            st.rerun()
        else:
            st.write(':rainbow[Get the answer right first! Don\'t forget to submit it!]')
       



