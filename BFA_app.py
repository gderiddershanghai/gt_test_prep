import streamlit as st
from BFA.bfa_mpc_big_review import big_review
from BFA.bfa_mpc_page1 import review_questions

def intro():
    st.write("# MGT 8803/6754 Business Fundamentals for Analytics Review App")
    st.sidebar.success("Select a review category to begin.")

    st.markdown("""
This app helps you prepare for **MGT 8803/6754: Business Fundamentals for Analytics** through multiple-choice questions based on lectures, readings, and practice problems.

### Sections:
- **Weekly Review**: Practice questions by week/module.
- **Exam Practice**: Randomized comprehensive review across topics.

### Additional Resources:
- [Khan Academy: Microeconomics](https://www.khanacademy.org/economics-finance-domain/microeconomics)
- [Harvard Business Review – Analytics](https://hbr.org/topic/analytics)
- [Corporate Finance Institute (CFI) – Business Analysis Resources](https://corporatefinanceinstitute.com/resources/)
- [MIT Sloan Management Review](https://sloanreview.mit.edu/)
- [Coursera: Introduction to Finance and Accounting Specialization (Wharton)](https://www.coursera.org/specializations/finance-accounting)
- [Coursera: Business Analytics Specialization (Wharton)](https://www.coursera.org/specializations/business-analytics)
- [Investopedia – Financial Ratios Guide](https://www.investopedia.com/terms/f/financial-ratio.asp)


Check out other review apps for related courses:
- [ISYE 6501 Introduction to Analytics Modeling](https://isye6501test-prep.streamlit.app/)
- [MGT 6203 Analytics for Business](https://mgt-6203-mt-study-aid.streamlit.app/)
- [ISYE 6740 Computational Data Analytics](https://cda-review-app.streamlit.app/) (not updated)
- [CS 7643 Deep Learning](https://deep-learning-practice.streamlit.app/) 
- [CS 7280 Network Science Review App](https://network-science-review.streamlit.app/) (not updated)
- [ISYE 6644 & 6739 Sim and Prob/Stats Review App](https://gt-sim-prob-prep.streamlit.app/) 
    """)
    
def weekly_review():
    st.markdown("# Weekly Review")
    st.write("Practice questions from specific weeks or modules.")
    review_questions()

def exam_practice():
    st.markdown("# Exam Practice")
    st.write("Comprehensive exam-style question set.")
    big_review()

def reset_or_initialize_state():
    keys_to_delete = ['token', 'chapter_review_state', 'comprehensive_review_state']
    for key in keys_to_delete:
        if key in st.session_state:
            del st.session_state[key]

page_names_to_funcs = {
    "—": intro,
    "Weekly Review": weekly_review,
    "Exam Prep": exam_practice
}

if 'current_demo' not in st.session_state:
    st.session_state['current_demo'] = None

demo_name = st.sidebar.selectbox("Choose Review Type", list(page_names_to_funcs.keys()), index=0)

if st.session_state['current_demo'] != demo_name:
    st.session_state['current_demo'] = demo_name
    reset_or_initialize_state()

if demo_name in page_names_to_funcs:
    page_names_to_funcs[demo_name]()