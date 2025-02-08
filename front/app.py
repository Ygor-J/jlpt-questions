import streamlit as st

st.header(('JLPT Questions'))

st.divider()


with st.form("Question"):
    st.write('ケネディ殺害の容疑者は __ に謎を残したままマフィアに撃たれて死亡した。') # Question
    answer = st.radio(
        'Answer:',
        options=["'1': '動機'", "'2': '本音'", "'3': '動力'", "'4': '下心'"],
        index=None
    )

    submitted = st.form_submit_button('Check')
    if submitted:
        if answer == "'1': '動機'":
            st.write('You got it right!')
        else:
            st.write('You got it wrong! :(')

