# BFA/m3w1.py

operations_week1_q1 = {
    'question': (
        "What is the \"golden equation\" in operations and supply chain management?"
    ),
    'options_list': [
        'Cost = Price × Quantity',
        'Revenue = Profit + Cost',
        'Profit = Revenue − Cost',
        'Revenue = Assets − Liabilities'
    ],
    'correct_answer': 'Profit = Revenue − Cost',
    'explanation': (
        "SCM is about increasing revenue and reducing costs to improve profit. The profit formula is:\n"
        "Profit = Revenue − Cost"
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}

operations_week1_q2 = {
    'question': (
        "Which of the following is NOT one of the six primary processes defined by the Supply Chain Council?"
    ),
    'options_list': [
        'Source',
        'Make',
        'Optimize',
        'Deliver'
    ],
    'correct_answer': 'Optimize',
    'explanation': (
        "The six are: Plan, Source, Make, Deliver, Return, Engage. 'Optimize' is not one of them explicitly."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}

operations_week1_q3 = {
    'question': (
        "Which of the following best characterizes a strategic (long-term) supply chain decision?"
    ),
    'options_list': [
        'Daily production scheduling',
        'Inventory reordering',
        'Choosing a plant location',
        'Allocating workers for a shift'
    ],
    'correct_answer': 'Choosing a plant location',
    'explanation': (
        "Strategic decisions are long-term, high-impact choices such as facility location, infrastructure investment, and supply chain network design."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}

operations_week1_q7 = {
    'question': (
        "Which of the following is a tactical (medium-term) supply chain decision?"
    ),
    'options_list': [
        'Introducing a new product line',
        'Hiring a new CEO',
        'Planning warehouse staffing levels for the quarter',
        'Determining shipping routes for a customer order'
    ],
    'correct_answer': 'Planning warehouse staffing levels for the quarter',
    'explanation': (
        "Tactical (medium-term) decisions focus on optimizing operations over months, such as capacity planning, workforce allocation, or production forecasting."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}


operations_week1_q4 = {
    'question': (
        "What is the role of a component manufacturer in a supply chain?"
    ),
    'options_list': [
        'Extract raw materials',
        'Transform raw materials into parts',
        'Assemble the final product',
        'Distribute to retailers'
    ],
    'correct_answer': 'Transform raw materials into parts',
    'explanation': (
        "Component manufacturers take processed materials (like metal) and fabricate parts used in final assemblies."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}

operations_week1_q5 = {
    'question': (
        "A disruption in a single component can halt an entire production line. This highlights which key SCM concept?"
    ),
    'options_list': [
        'Economies of scale',
        'Supply chain flexibility',
        'Bottleneck dependency',
        'Just-in-time delivery'
    ],
    'correct_answer': 'Bottleneck dependency',
    'explanation': (
        "A single component (e.g., steering wheel at Toyota) missing can cause a total stoppage—this reflects bottleneck dependency."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}

operations_week1_q6 = {
    'question': (
        "Why did KFC in the UK temporarily shut down stores?"
    ),
    'options_list': [
        'Employee strike',
        'Lack of customer demand',
        'Poor marketing strategy',
        'Delivery supply chain failure'
    ],
    'correct_answer': 'Delivery supply chain failure',
    'explanation': (
        "KFC changed delivery partners, which disrupted the chicken supply chain and led to store closures."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}



operations_week1_q8 = {
    'question': (
        "The “Engage” process in the Supply Chain Council model primarily involves:"
    ),
    'options_list': [
        'Marketing to customers',
        'Financial auditing',
        'Innovation and improvement',
        'Hiring supply chain personnel'
    ],
    'correct_answer': 'Innovation and improvement',
    'explanation': (
        "“Engage” refers to continuous improvement across planning, sourcing, making, delivering, and returning."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}

operations_week1_q9 = {
    'question': (
        "A key motivation for managing supply chains well is to:"
    ),
    'options_list': [
        'Replace accounting systems',
        'Increase stockholder taxes',
        'Drive profitability through cost reduction and revenue growth',
        'Outsource all company functions'
    ],
    'correct_answer': 'Drive profitability through cost reduction and revenue growth',
    'explanation': (
        "Effective SCM contributes to profit by optimizing revenue (e.g., faster product delivery) and minimizing costs (e.g., efficient sourcing)."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}

operations_week1_q10 = {
    'question': (
        "Which of the following best describes the structure of a real-world supply chain?"
    ),
    'options_list': [
        'Circular and closed',
        'Single linear line with one supplier and one customer',
        'A complex network with multiple suppliers at each stage',
        'Government controlled and vertically integrated'
    ],
    'correct_answer': 'A complex network with multiple suppliers at each stage',
    'explanation': (
        "Real-world supply chains are complex networks. For example, Boeing’s 787 involves 20+ global component suppliers, each with their own upstream suppliers."
    ),
    'chapter_information': 'Operations Module W1 GPT GENERATED'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M3W1_MPC = KC_MPC_QUESTIONS[:-1]
