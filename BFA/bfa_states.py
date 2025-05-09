import numpy as np
from m1w1 import BFA_M1W1_MPC
from m1w2 import BFA_M1W2_MPC


# Questions Dictionary
questions_dictionary = {

    'M1W1': BFA_M1W1_MPC, 
    'M1W2': BFA_M1W2_MPC, 
}

# Updated Review Sets
REVIEW_SETS = {

    "FINANCIAL ACCOUNTING": ['M1W1', 'M1W2', 'M1W3'],


}

# Token Class
class Token:
    def __init__(self, STATE="1"):
        self.STATE = STATE
        self.mpc_questions = []
        self.num_questions = 10
        self.chapters_to_review = []

    def initialize_mpc_questions(self):
        # Validate the STATE
        if self.STATE not in REVIEW_SETS:
            print(f"Error: Invalid STATE '{self.STATE}' passed to Token. Check REVIEW_SETS definition.")
            return

        self.chapters_to_review = REVIEW_SETS[self.STATE]

        if not self.chapters_to_review:
            print(f"Error: chapters_to_review not set for STATE: {self.STATE}")
            return

        # Generate Questions
        self.mpc_questions = []
        while len(self.mpc_questions) < self.num_questions:
            chapters = np.random.choice(self.chapters_to_review, size=len(self.chapters_to_review), replace=False)
            for chapter in chapters:
                try:
                    review_questions = questions_dictionary[chapter]
                    if not review_questions:
                        print(f'Warning: Chapter {chapter} is empty.')
                        continue

                    # Add Random Questions
                    mpc_idx = np.random.choice(range(len(review_questions)), size=1, replace=False)
                    self.mpc_questions.append(review_questions[int(mpc_idx)])

                    if len(self.mpc_questions) >= self.num_questions:
                        break
                except KeyError:
                    print(f"Error: Chapter {chapter} not found in questions dictionary.")

if __name__ == "__main__":
    token = Token('Final')
    token.initialize_mpc_questions()
    print(token.mpc_questions)
