operations_w3_q01 = {
    'question': "Which of the following best describes the critical fractile in the newsvendor model?",
    'options_list': [
        "A. The average number of units sold",
        "B. The ratio of underage cost to total marginal cost",
        "C. The expected demand",
        "D. The maximum inventory level allowed"
    ],
    'correct_answer': "B. The ratio of underage cost to total marginal cost",
    'explanation': "The critical fractile is calculated as CU / (CU + CO), where CU is underage cost and CO is overage cost.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q02 = {
    'question': "If the unit cost is $5, selling price is $9, and salvage value is $2, what is the overage cost (CO)?",
    'options_list': [
        "$7", "$2", "$4", "$3"
    ],
    'correct_answer': "$3",
    'explanation': "Overage cost CO = unit cost − salvage value = 5 − 2 = 3.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q03 = {
    'question': "Which function in Excel gives the z-score from a given cumulative probability?",
    'options_list': [
        "NORM.S.DIST", "NORM.INV", "NORM.S.INV", "Z.TEST"
    ],
    'correct_answer': "NORM.S.INV",
    'explanation': "NORM.S.INV returns the z-value for a given probability in the standard normal distribution.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q04 = {
    'question': "In the newsvendor model, which situation increases the optimal order quantity?",
    'options_list': [
        "A. Higher salvage value",
        "B. Higher cost per unit",
        "C. Higher underage cost",
        "D. Lower mean demand"
    ],
    'correct_answer': "C. Higher underage cost",
    'explanation': "As CU increases, the critical fractile increases, leading to a higher optimal order quantity.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q05 = {
    'question': "Given: CU = 3, CO = 1.5, mean = 1000, std dev = 200. What is the critical fractile?",
    'options_list': [
        "0.33", "0.50", "0.67", "0.75"
    ],
    'correct_answer': "0.67",
    'explanation': "CF = CU / (CU + CO) = 3 / (3 + 1.5) = 0.67",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q06 = {
    'question': "The newsvendor model assumes demand is deterministic.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "The newsvendor model is based on stochastic (random) demand with known distribution.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q07 = {
    'question': "A higher underage cost leads to a lower optimal order quantity.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "Higher CU increases the critical fractile, resulting in a higher order quantity.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q08 = {
    'question': "The critical fractile determines the optimal service level in the newsvendor model.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "The optimal service level equals the critical fractile and dictates the inventory level to balance CU and CO.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q09 = {
    'question': "The z-score is negative if the critical fractile is less than 0.5.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "A CF < 0.5 implies the optimal quantity lies to the left of the mean; thus, the corresponding z is negative.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}

operations_w3_q10 = {
    'question': "Expected profit is maximized when the probability that demand is less than or equal to Q equals the critical fractile.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "This is the newsvendor optimality condition: set Q such that P(D ≤ Q) = CF.",
    'chapter_information': 'Operations Module W3 - GPT GENERATED'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M3W3_MPC = KC_MPC_QUESTIONS[:-1]
