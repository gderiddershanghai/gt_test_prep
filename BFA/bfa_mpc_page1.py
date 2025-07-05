import streamlit as st
from .bfa_states import Token

def apply_custom_css():
    custom_css = """
    <style>
        .question-style {
            font-size: 20px; 
            font-weight: bold; 
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def question_generator(label, options, question_key):
    return st.radio(label='_', options=options, key=question_key)


def review_questions():
    apply_custom_css()

    if 'token' not in st.session_state:
        st.session_state.token = Token()  
        st.session_state.questions_initialized = False

    st.markdown("### Please select a Probability Module to proceed:")

    module_mapping = {
        "Module 1 (Financial Accounting) - Week 1": 'M1W1',
        "Module 1 (Financial Accounting) - Week 2": 'M1W2',
        "Module 1 (Financial Accounting) - Week 3": 'M1W3',
        "Module 2 (Finance) - Week 1": 'M2W1',
        "Module 2 (Finance) - Week 2": 'M2W2',
        "Module 2 (Finance) - Week 3": 'M2W3',
        "Module 2 (Finance) - NON GT CONTENT ":  "M2_EXTRA",
        "Module 3 (Operations) - Week 1": 'M3W1',
        "Module 3 (Operations) - Week 2": 'M3W2',
        "Module 3 (Operations) - Week 3": 'M3W3',
}

    # Module Selection
    selected_module = st.radio(label=' ', options=list(module_mapping.keys()), label_visibility="collapsed")

    if st.button("Load Questions"):
        try:
            st.session_state.STATE = module_mapping[selected_module]
            st.session_state.token = Token(STATE=st.session_state.STATE)
            st.session_state.token.initialize_mpc_questions()
            st.session_state.questions = st.session_state.token.mpc_questions
            st.session_state.questions_initialized = True
        except ValueError as e:
            st.error(f"Error: {e}")
            return


    if st.session_state.questions_initialized:
        # st.session_state.questions_initialized = False  

        questions = st.session_state.questions

        for i, q in enumerate(questions):
            st.markdown('-------------------------------')
            st.markdown(f"{q['question']}")
            options = q['options_list']
            correct_answer = q['correct_answer']
            explanation = q.get('explanation', " ")
            question_key = f"question_{i}"


            selected_answer = question_generator(q['question'], options, question_key)


            if st.button('Submit', key=f"submit_{i}"):
                if selected_answer == correct_answer:
                    st.success('Great work!')
                    st.info(f'Explanation: \n\n{explanation}')
                else:
                    st.error(f"The correct answer was {correct_answer}")
                    st.info(f'Explanation: \n\n{explanation}')
                if 'chapter_information' in q:
                    st.write(f"You can review {q['chapter_information']}")

if __name__ == "__main__":
    review_questions()
