import numpy as np
from .m1w1 import BFA_M1W1_MPC
from .m1w2 import BFA_M1W2_MPC
from .m1w3 import BFA_M1W3_MPC
from .m1_extra import BFA_M1_EXTRA_MPC

from .m2w1 import BFA_M2W1_MPC
from .m2w2 import BFA_M2W2_MPC
from .m2w3 import BFA_M2W3_MPC

from .m3w1 import BFA_M3W1_MPC

from .m2_extra import BFA_M2_EXTRA_MPC

# Questions Dictionary
questions_dictionary = {

    'M1W1': BFA_M1W1_MPC, 
    'M1W2': BFA_M1W2_MPC, 
    'M1W3': BFA_M1W3_MPC, 
    "M1_EXTRA": BFA_M1_EXTRA_MPC,
    'M2_EXTRA':  BFA_M2_EXTRA_MPC,
    'M2W1': BFA_M2W1_MPC, 
    'M2W2': BFA_M2W2_MPC, 
    'M2W3': BFA_M2W3_MPC, 
    'M3W1': BFA_M3W1_MPC, 
}

# Updated Review Sets
REVIEW_SETS = {
    'M1W1': BFA_M1W1_MPC, 
    'M1W2': BFA_M1W2_MPC, 
    'M1W3': BFA_M1W3_MPC, 
    'M1_EXTRA': BFA_M1_EXTRA_MPC,
    "FINANCIAL ACCOUNTING": ['M1W1', 'M1W2', 'M1W3', "M1_EXTRA"],
    'M2_EXTRA':  BFA_M2_EXTRA_MPC,
    'M2W1': BFA_M2W1_MPC, 
    'M2W2': BFA_M2W2_MPC, 
    'M2W3': BFA_M2W3_MPC, 
     "FINANCE": ['M2W1', 'M2W2', 'M2W3'],
      "NON GT FINANCE": ['M2_EXTRA'],
      'M3W1': BFA_M3W1_MPC, 
}



# Token Class
class Token:
    def __init__(self, STATE="1"):
        self.STATE = STATE
        self.mpc_questions = []
        self.num_questions = 15
        self.chapters_to_review = []
        # print('-----------------------------')
        # print('-----', sum([len(questions_dictionary[question_list]) for question_list in REVIEW_SETS["FINANCIAL ACCOUNTING"]]))
        # print('-----------------------------')
        print('-----',len(questions_dictionary['M2W1'])) 
        # print('---self.mpc_questions--',len(self.mpc_questions) )
            #   sum([len(questions_dictionary[question_list]) for question_list in REVIEW_SETS["FINANCIAL ACCOUNTING"]]))

        # print('TOTAL QUESTIONS:', sum([len(v) for k,v in REVIEW_SETS["FINANCIAL ACCOUNTING"]]))
        
    def initialize_mpc_questions(self):
        print(self.__dict__, '------------')

        if self.STATE not in REVIEW_SETS:
            print(f"Error: Invalid STATE '{self.STATE}' passed to Token. Check REVIEW_SETS definition.")
            return

        review_entry = REVIEW_SETS[self.STATE]

        if not review_entry:
            print(f"Error: chapters_to_review not set for STATE: {self.STATE}")
            return

        # Case 1: Direct list of questions (single chapter review)
        if isinstance(review_entry[0], dict):
            self.mpc_questions = list(np.random.choice(
                review_entry,
                size=min(self.num_questions, len(review_entry)),
                replace=False
            ))
            print('---self.mpc_questions CASE 1--',len(self.mpc_questions) )
            return

        # Case 2: List of chapter keys (multi-chapter review)
        self.chapters_to_review = review_entry
        question_pool = []
        for chapter in self.chapters_to_review:
            try:
                question_pool.extend(questions_dictionary[chapter])
            except KeyError:
                print(f"Error: Chapter {chapter} not found in questions dictionary.")

        if not question_pool:
            print(f"Error: No questions found for STATE: {self.STATE}")
            return

        self.mpc_questions = list(np.random.choice(
            question_pool,
            size=min(self.num_questions, len(question_pool)),
            replace=False
        ))
        print('---self.mpc_questions--',len(self.mpc_questions) )


    # def initialize_mpc_questions(self):
        
    #     print(self.__dict__, '------------')
    #     # Validate the STATE
    #     if self.STATE not in REVIEW_SETS:
    #         print(f"Error: Invalid STATE '{self.STATE}' passed to Token. Check REVIEW_SETS definition.")
    #         return

    #     self.chapters_to_review = REVIEW_SETS[self.STATE]

    #     if not self.chapters_to_review:
    #         print(f"Error: chapters_to_review not set for STATE: {self.STATE}")
    #         return

    #     # Generate Questions
    #     self.mpc_questions = []
    #     while len(self.mpc_questions) < self.num_questions:
    #         chapters = np.random.choice(self.chapters_to_review, size=len(self.chapters_to_review), replace=False)
    #         for chapter in chapters:
    #             try:
    #                 review_questions = questions_dictionary[chapter]
    #                 if not review_questions:
    #                     print(f'Warning: Chapter {chapter} is empty.')
    #                     continue

    #                 # Add Random Questions
    #                 mpc_idx = np.random.choice(range(len(review_questions)), size=1, replace=False)
    #                 self.mpc_questions.append(review_questions[int(mpc_idx)])

    #                 if len(self.mpc_questions) >= self.num_questions:
    #                     break
    #             except KeyError:
    #                 print(f"Error: Chapter {chapter} not found in questions dictionary.")

if __name__ == "__main__":
    token = Token('Final')
    token.initialize_mpc_questions()
    print(token.mpc_questions)
