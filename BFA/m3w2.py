operations_w2_q1 = {
    'question': (
        "What is the primary philosophy behind Lean manufacturing?"
    ),
    'options_list': [
        "Producing goods just-in-time",
        "Minimizing labor costs",
        "Eliminating waste",
        "Increasing equipment utilization"
    ],
    'correct_answer': "Eliminating waste",
    'explanation': (
        "The core principle of Lean is to eliminate waste in all forms — inventory, defects, motion, etc. "
        "JIT is just one tool used in Lean, not the philosophy itself."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q2 = {
    'question': (
        "Which Lean tool is used to visually map all steps in a process to identify non-value-adding activities?"
    ),
    'options_list': [
        "5S",
        "Kanban",
        "Kaizen",
        "Value Stream Mapping"
    ],
    'correct_answer': "Value Stream Mapping",
    'explanation': (
        "Value Stream Mapping (VSM) helps visualize material and information flows to identify waste (non-value steps). "
        "5S is for workplace organization, Kanban for WIP control, and Kaizen for continuous improvement."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q3 = {
    'question': (
        "In a pull system, what triggers production at an upstream process?"
    ),
    'options_list': [
        "Weekly schedule",
        "Available raw materials",
        "Customer order or downstream demand",
        "Operator availability"
    ],
    'correct_answer': "Customer order or downstream demand",
    'explanation': (
        "In pull systems, downstream demand or consumption triggers production upstream. "
        "It’s demand-driven, unlike scheduled push systems."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q4 = {
    'question': (
        "What happens if there is no Kanban card in a pull system?"
    ),
    'options_list': [
        "Production is accelerated",
        "The system switches to push",
        "No production occurs",
        "A backup inventory is created"
    ],
    'correct_answer': "No production occurs",
    'explanation': (
        "Kanban cards serve as authorization to produce. No card means no production, "
        "which helps limit WIP and prevent overproduction."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

# True/False Questions

operations_w2_tf1 = {
    'question': (
        "Lean manufacturing emphasizes keeping workers busy at all times to maximize output."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        "Lean focuses on keeping materials moving (not workers constantly busy). "
        "Overproduction is considered waste."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf2 = {
    'question': (
        "In a pull system, upstream processes only produce when signaled by downstream demand."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "Pull systems are demand-driven — production occurs only when triggered by a Kanban or similar signal from downstream."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf3 = {
    'question': (
        "Value Stream Mapping is used to optimize workstation layout."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        "VSM is used to map process flows and identify non-value-adding steps, not to design physical layouts. "
        "That’s more aligned with 5S or facility layout planning."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf4 = {
    'question': (
        "Kanban helps limit work-in-process inventory in a pull system."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "Kanban acts as a control mechanism — it limits WIP by only allowing production when a card (signal) is present."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf5 = {
    'question': (
        "5S is a tool used to identify defects in a production system."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        "5S is for workplace organization and cleanliness, not defect detection. "
        "Defect detection is often improved by flow/pull and visual control tools."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf6 = {
    'question': (
        "In Lean, inventory is considered a form of waste."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "Inventory ties up capital, can become obsolete, and hides problems — all of which Lean seeks to avoid."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}


operations_w2_q5 = {
    'question': (
        "Which of the following best describes the purpose of the EOQ model?"
    ),
    'options_list': [
        "Minimize lead time",
        "Maximize customer demand",
        "Minimize total inventory cost",
        "Maximize inventory turnover"
    ],
    'correct_answer': "Minimize total inventory cost",
    'explanation': (
        "EOQ balances ordering and holding costs to minimize total inventory cost."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q6 = {
    'question': (
        "If the annual demand (D) increases, what happens to the EOQ?"
    ),
    'options_list': [
        "Increases",
        "Decreases",
        "Stays the same",
        "Drops to zero"
    ],
    'correct_answer': "Increases",
    'explanation': (
        "EOQ = √(2DS/H), so as D increases, EOQ increases (square root relationship)."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q7 = {
    'question': (
        "In the EOQ model, average inventory is assumed to be:"
    ),
    'options_list': [
        "D × L",
        "Q",
        "Q / 2",
        "S × H"
    ],
    'correct_answer': "Q / 2",
    'explanation': (
        "Because inventory depletes linearly from Q to 0, average inventory is Q/2."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q8 = {
    'question': (
        "What is the correct formula for the Reorder Point (ROP)?"
    ),
    'options_list': [
        "D / Q",
        "H / D",
        "d × L",
        "2DS / H"
    ],
    'correct_answer': "d × L",
    'explanation': (
        "ROP = average daily demand × lead time = d × L"
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

# True/False EOQ-related Questions

operations_w2_tf7 = {
    'question': (
        "Holding costs are usually a fixed cost and do not depend on inventory levels."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': (
        "Holding cost increases with the amount of inventory held."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf8 = {
    'question': (
        "The EOQ model assumes that demand is constant and known."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': (
        "This is a key assumption in the basic EOQ model."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf9 = {
    'question': (
        "Reorder point depends on order size."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': (
        "ROP depends on daily demand and lead time, not order size."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf10 = {
    'question': (
        "In the EOQ model, total cost is minimized when ordering cost equals holding cost."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': (
        "This balance gives the lowest total inventory cost."
    ),
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

# Multiple-Choice Questions

operations_w2_q9 = {
    'question': "Which of the following is *not* a type of inventory?",
    'options_list': [
        "Finished goods",
        "Machine downtime",
        "Work-in-process",
        "Raw materials"
    ],
    'correct_answer': "Machine downtime",
    'explanation': "Downtime isn’t inventory. The rest are legitimate inventory types.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q10 = {
    'question': "A key reason companies hold inventory is to:",
    'options_list': [
        "Eliminate production planning",
        "Increase lead times",
        "Buffer against demand or supply uncertainty",
        "Reduce employee wages"
    ],
    'correct_answer': "Buffer against demand or supply uncertainty",
    'explanation': "Inventory provides a buffer against uncertainty on the demand or supply side.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q11 = {
    'question': "Which of the following is a *cost* of holding inventory?",
    'options_list': [
        "Backorders",
        "Increased market share",
        "Obsolescence",
        "Higher throughput"
    ],
    'correct_answer': "Obsolescence",
    'explanation': "Obsolescence is a direct cost of holding inventory, especially for perishable or fast-moving products.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q12 = {
    'question': "The average inventory level in EOQ is best described as:",
    'options_list': [
        "Q × H",
        "Q × D",
        "Q / 2",
        "D / Q"
    ],
    'correct_answer': "Q / 2",
    'explanation': "Inventory is assumed to decrease linearly from Q to 0, so average = Q / 2.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q13 = {
    'question': "If lead time increases, what happens to the reorder point?",
    'options_list': [
        "Decreases",
        "Increases",
        "Stays the same",
        "Drops to zero"
    ],
    'correct_answer': "Increases",
    'explanation': "ROP = d × L; if L (lead time) increases, the reorder point rises.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q14 = {
    'question': "EOQ is calculated by minimizing which two costs?",
    'options_list': [
        "Setup and shrinkage",
        "Holding and ordering",
        "Spoilage and backorders",
        "Procurement and transportation"
    ],
    'correct_answer': "Holding and ordering",
    'explanation': "EOQ balances ordering and holding costs to find the lowest total inventory cost.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q15 = {
    'question': "In the EOQ formula, what happens if holding cost (H) increases?",
    'options_list': [
        "EOQ increases",
        "EOQ decreases",
        "EOQ stays the same",
        "EOQ drops to zero"
    ],
    'correct_answer': "EOQ decreases",
    'explanation': "EOQ = √(2DS/H); increasing H makes the denominator larger and EOQ smaller.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_q16 = {
    'question': "Which assumption *does not* apply to the basic EOQ model?",
    'options_list': [
        "Demand is constant",
        "Replenishment is instantaneous",
        "Shortages are allowed",
        "Only ordering and holding costs matter"
    ],
    'correct_answer': "Shortages are allowed",
    'explanation': "The basic EOQ model assumes no stockouts or shortages.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

# True/False Questions

operations_w2_tf11 = {
    'question': "Inventory is only considered a cost, never an asset.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "Inventory is recorded as an asset on the balance sheet, though it has associated costs.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf12 = {
    'question': "Shrinkage refers to physical loss of inventory over time.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "Shrinkage includes theft, damage, and loss of physical stock.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf13 = {
    'question': "In the EOQ model, average inventory equals EOQ divided by 2.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "This is a core assumption of the EOQ model under steady demand.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf14 = {
    'question': "The reorder point is affected by both average daily demand and lead time.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "ROP = d × L, where d is daily demand and L is lead time.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf15 = {
    'question': "EOQ is valid even when demand and lead time are highly variable.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "EOQ assumes constant and known demand and lead time.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf16 = {
    'question': "If demand is 5,000 units per year and order quantity is 500, then there will be 10 orders per year.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "Annual orders = D / Q = 5000 / 500 = 10.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf17 = {
    'question': "In the Buzzlot example, the reorder point was based on when the total inventory cost is minimized.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "The ROP is based on when to reorder (lead time × daily demand), not total cost.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}

operations_w2_tf18 = {
    'question': "EOQ minimizes total cost when holding cost = ordering cost.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "That’s the condition for cost minimization in the EOQ framework.",
    'chapter_information': 'Operations Module W2 - GPT GENERATED'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M3W2_MPC = KC_MPC_QUESTIONS[:-1]
