finance_week3_L1_q1 = {
    'question': "Which of the following statements is FALSE with regard to the Weighted Average Cost of Capital (WACC)?",
    'options_list': [
        "A. The WACC accounts for both debt and equity financing",
        "B. Interest on debt is tax-deductible and must be adjusted using the tax rate",
        "C. The WACC is the maximum return a company must earn to satisfy investors",
        "D. The WACC is necessary only for companies using equity financing"
    ],
    'correct_answer': "D. The WACC is necessary only for companies using equity financing",
    'explanation': "WACC applies to firms using both debt and equity. It is not exclusive to equity-financed firms.",
    'chapter_information': 'Finance Module - Week 3 Lecture 1- GPT GENERATED'
}

finance_week3_L1_q2 = {
    'question': "The after-tax cost of debt is calculated using which of the following formulas?",
    'options_list': [
        "A. r_d + T",
        "B. r_d − T",
        "C. r_d ⋅ (1 − T)",
        "D. r_d / (1 + T)"
    ],
    'correct_answer': "C. r_d ⋅ (1 − T)",
    'explanation': "Interest on debt is tax-deductible, so the effective cost of debt is reduced by the tax rate.",
    'chapter_information': 'Finance Module - Week 3 Lecture 1- GPT GENERATED'
}

finance_week3_L1_q3 = {
    'question': "A firm's cost of debt increases when:",
    'options_list': [
        "A. It issues more equity",
        "B. Its WACC declines",
        "C. Its credit rating is downgraded",
        "D. Treasury bond yields decrease"
    ],
    'correct_answer': "C. Its credit rating is downgraded",
    'explanation': "A downgrade implies higher default risk, which increases the spread over Treasury rates, raising the cost of debt.",
    'chapter_information': 'Finance Module - Week 3 Lecture 1- GPT GENERATED'
}

finance_week3_L1_q4 = {
    'question': "Which of the following is TRUE regarding debt financing decisions?",
    'options_list': [
        "A. Firms with fewer tangible assets are more likely to use debt",
        "B. Stable cash flows support higher levels of debt",
        "C. Tax considerations discourage the use of debt",
        "D. High-growth firms prefer to rely more heavily on debt"
    ],
    'correct_answer': "B. Stable cash flows support higher levels of debt",
    'explanation': "Stable cash flows reduce default risk, making debt more accessible. High-growth firms prefer equity for flexibility.",
    'chapter_information': 'Finance Module - Week 3 Lecture 1- GPT GENERATED'
}

finance_week3_L1_q5 = {
    'question': "What is the primary reason a company’s cost of debt is higher than the Treasury bond rate?",
    'options_list': [
        "A. Because the company is publicly traded",
        "B. Because investors demand compensation for default risk",
        "C. Because it includes dividend payments",
        "D. Because it is calculated before taxes"
    ],
    'correct_answer': "B. Because investors demand compensation for default risk",
    'explanation': "Corporate bonds carry default risk, unlike Treasury bonds. The difference is the default spread.",
    'chapter_information': 'Finance Module - Week 3 Lecture 1- GPT GENERATED'
}

finance_week3_L1_q6 = {
    'question': "In estimating a company’s cost of debt, what role do bond ratings from Moody’s or S&P play?",
    'options_list': [
        "A. They determine the firm’s tax rate",
        "B. They dictate the firm's capital structure",
        "C. They help estimate the default risk premium above the Treasury rate",
        "D. They are used to calculate the cost of equity"
    ],
    'correct_answer': "C. They help estimate the default risk premium above the Treasury rate",
    'explanation': "Bond ratings reflect the issuer’s creditworthiness and are used to derive the appropriate default spread over Treasury rates.",
    'chapter_information': 'Finance Module - Week 3 Lecture 1- GPT GENERATED'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M2W3_MPC = KC_MPC_QUESTIONS[:-1]
