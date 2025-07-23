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
    return st.radio(label='Please select the correct answer', options=options, key=question_key)

def big_review():
    apply_custom_css()

    if 'token' not in st.session_state:
        st.session_state.token = Token()
        st.session_state.questions_initialized = False

    st.title("Select a Review Type")

    review_mapping = {
        "Financial Accounting Exam": "FINANCIAL ACCOUNTING",
        "Finance Exam": "FINANCE",
        "Non GT Finance Content": "NON GT FINANCE",
        "Operations (Supply Chain) Exam": "OPERATIONS",
         "Marketing Exam": "MARKETING",

    }

    review_choice = st.radio("Choose a review type", options=list(review_mapping.keys()))
    selected_state = review_mapping[review_choice]

    if st.button('Load Questions'):
        try:
            st.session_state.token = Token(STATE=selected_state)
            st.session_state.token.initialize_mpc_questions()
            st.session_state.questions = st.session_state.token.mpc_questions
            st.session_state.questions_initialized = True
        except ValueError as e:
            st.error(f"Error: {e}")
            return

    if st.session_state.questions_initialized:
        # st.session_state.questions_initialized = False  

        questions = st.session_state.questions

        for i, q in enumerate(st.session_state.questions):
            st.markdown('-------------------------------')

            # ---- Guard against malformed records ----
            opts = q.get('options_list') or q.get('options')
            if not opts:
                st.error(f"Question {i} is missing an options list:\n{q}")
                continue
            correct = q.get('correct_answer')
            if correct is None:
                st.error(f"Question {i} is missing 'correct_answer':\n{q}")
                continue
            # -----------------------------------------

            st.markdown(q['question'])
            chosen = question_generator(q['question'], opts, f"question_{i}")

            if st.button('Submit', key=f"submit_{i}"):
                if chosen == correct:
                    st.success('Great work!')
                else:
                    st.error(f"The correct answer was {correct}")
                st.info(f"Explanation:\n\n{q.get('explanation','')}")
                if 'chapter_information' in q:
                    st.write(f"You can review {q['chapter_information']}")
        # for i, q in enumerate(questions):
        #     st.markdown('-------------------------------')
        #     st.markdown(f"{q['question']}")
        #     options = q['options_list']
        #     correct_answer = q['correct_answer']
        #     explanation = q.get('explanation', " ")
        #     question_key = f"question_{i}"

        #     selected_answer = question_generator(q['question'], options, question_key)

        #     if st.button('Submit', key=f"submit_{i}") and selected_answer:
        #         if selected_answer == correct_answer:
        #             st.success('Great work!')
        #             st.info(f'Explanation: \n\n{explanation}')
        #         else:
        #             st.error(f"The correct answer was {correct_answer}")
        #             st.info(f'Explanation: \n\n{explanation}')
        #         if 'chapter_information' in q:
        #             st.write(f"You can review {q['chapter_information']}")

if __name__ == "__main__":
    big_review()
