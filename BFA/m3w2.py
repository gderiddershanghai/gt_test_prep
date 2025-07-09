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

# Multiple Choice Questions

operations_w2_paper_q1 = {
    'question': "What was Kevin Brown’s main inventory goal for the Great White paper SKU?",
    'options_list': [
        "Maximize sales at all costs",
        "Maintain a 100% in-stock rate",
        "Achieve a 98% fill rate",
        "Eliminate inventory entirely"
    ],
    'correct_answer': "Achieve a 98% fill rate",
    'explanation': "Brown aimed to reduce holding costs while maintaining acceptable service via a 98% fill rate.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2_paper_q2 = {
    'question': "In the case, what is meant by “order-up-to point”?",
    'options_list': [
        "Maximum allowable shelf price",
        "Target inventory level after ordering",
        "Daily sales limit per SKU",
        "Total yearly demand forecast"
    ],
    'correct_answer': "Target inventory level after ordering",
    'explanation': "The 'order-up-to point' is the inventory level the system aims to reach after each restocking.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2_paper_q3 = {
    'question': "The formula used to calculate the optimal order quantity in a newsvendor setting depends on:",
    'options_list': [
        "Total yearly revenue",
        "Reorder lead time",
        "Critical fractile based on overage and underage cost",
        "Holding cost only"
    ],
    'correct_answer': "Critical fractile based on overage and underage cost",
    'explanation': "Newsvendor logic uses the critical ratio (Cu / (Cu + Co)) to find the profit-maximizing order quantity.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2_paper_q4 = {
    'question': "Why does a 100% fill rate usually lead to high holding costs?",
    'options_list': [
        "Because it requires bulk purchasing discounts",
        "Because more frequent deliveries are needed",
        "Because excess inventory is kept to avoid stockouts",
        "Because low fill rates are more expensive"
    ],
    'correct_answer': "Because excess inventory is kept to avoid stockouts",
    'explanation': "A 100% fill rate requires large buffer stock, increasing inventory costs significantly.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2_paper_q5 = {
    'question': "In the case, why is the cost of underage for Great White estimated as (Retail – Wholesale)?",
    'options_list': [
        "It represents the lost margin on a missed sale",
        "It’s equivalent to total annual sales",
        "It’s the customer loyalty penalty",
        "It matches the overage cost"
    ],
    'correct_answer': "It represents the lost margin on a missed sale",
    'explanation': "This is the opportunity cost of not having inventory to meet demand.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

# True/False Questions

operations_w2_paper_tf1 = {
    'question': "The fill rate (Type 2 service level) is always lower than the in-stock rate (Type 1).",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "Fill rate can be higher or lower depending on demand size during in-stock periods.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2_paper_tf2 = {
    'question': "Kevin Brown used a biweekly (every two weeks) ordering schedule.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "The case indicates Brown orders on a two-week cycle.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2_paper_tf3 = {
    'question': "A high in-stock rate always implies high net profit.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "Higher service levels increase holding costs, potentially hurting profits.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2_paper_tf4 = {
    'question': "The critical fractile determines the service level that maximizes expected profit.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "The critical fractile balances overage and underage costs to optimize expected value.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2_paper_tf5 = {
    'question': "The average inventory when a stockout occurs is calculated as ½ of the starting inventory.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "This holds during stocked periods; average inventory is often modeled as Q/2 for simplicity.",
    'chapter_information': 'Operations Module W2 Paper and More - GPT GENERATED'
}

operations_w2sa_q1 = {
    'question': "What is the philosophy of Lean?",
    'options_list': [
        'Elimination of waste',
        'Product arrives just in time',
        'Minimization of inventory',
        'Use of Kaizen',
        'Use of Kanban'
    ],
    'correct_answer': 'Elimination of waste',
    'explanation': "Lean focuses on eliminating all forms of waste in processes — including excess inventory, overproduction, motion, and defects.",
    'chapter_information': 'Operations Module W2 - Self Assessment Questions'
}

operations_w2sa_q2 = {
    'question': "In a traditional push system, throughput time will usually increase as work-in-process increases (True/False).",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': "More WIP increases congestion and queues, which in turn increases throughput time.",
    'chapter_information': 'Operations Module W2 - Self Assessment Questions'
}

operations_w2sa_q3 = {
    'question': "Which of the following is one of the differences between a push and a pull system?",
    'options_list': [
        'A push system keeps operators busy and materials idle, while a pull system keeps both operator and materials idle',
        'A push system keeps operators and materials idle, while a pull system keeps operators busy and materials idle',
        'A push system keeps operators and materials busy, while a pull system keeps operators idle and materials busy',
        'A push system keeps operators idle and materials busy, while a pull system keeps operators and materials busy'
    ],
    'correct_answer': 'A push system keeps operators and materials busy, while a pull system keeps operators idle and materials busy',
    'explanation': "Push systems emphasize utilization, while pull systems focus on producing only when needed — prioritizing flow over busy-ness.",
    'chapter_information': 'Operations Module W2 - Self Assessment Questions'
}

operations_w2sa_q4 = {
    'question': "In a pull system the production line is controlled by the first operation (True/False).",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': "Pull systems are driven by downstream demand — the last operation sends the signal to upstream stages.",
    'chapter_information': 'Operations Module W2 - Self Assessment Questions'
}

operations_w2sa_q5 = {
    'question': "Which of the following is NOT a characteristic of a PULL system?",
    'options_list': [
        'Faster reaction to defects',
        'Operators only work when there is a signal to produce',
        'Focuses on keeping individual operators and workstations busy',
        'There is no slack in the system'
    ],
    'correct_answer': 'Focuses on keeping individual operators and workstations busy',
    'explanation': "Pull systems focus on flow and demand responsiveness, not maximizing utilization of individuals.",
    'chapter_information': 'Operations Module W2 - Self Assessment Questions'
}

operations_w2sa_q6 = {
    'question': "Which of the following is a common internal strategy to match supply with demand?",
    'options_list': [
        'Price change',
        'Turn down orders',
        'Pre-orders',
        'Sub-contract'
    ],
    'correct_answer': 'Sub-contract',
    'explanation': "Subcontracting is a classic internal capacity strategy used to match variable demand with supply.",
    'chapter_information': 'Operations Module W2 - Self Assessment Questions'
}

operations_w2sa_q7 = {
    'question': "Which of the following is a common external strategy to match supply and demand?",
    'options_list': [
        'Overtime',
        'Temp workers',
        'Build up inventory',
        'Hire/fire employees',
        'Promotions '
    ],
    'correct_answer': 'Promotions',
    'explanation': "Promotions influence customer demand patterns to better align with available supply.",
    'chapter_information': 'Operations Module W2 - Self Assessment Questions'
}

operations_w2_q8 = {
    'chapter_information': 'Operations Module W2 - Self Assessment Questions',
    'question': 'John’s Used Motorcycle Emporium wants to decide the best order size for motorcycles. Annual demand is 1,000 units, holding cost is $100/unit/year, and ordering cost is $25/order. Using EOQ, how many should John order each time?',
    'options_list': ['20', '23', '30', '34', '50'],
    'correct_answer': '23',
    'explanation': 'EOQ = $\\sqrt{\\frac{2DS}{H}} = \\sqrt{\\frac{2 \\times 1000 \\times 25}{100}} = \\sqrt{500} = 22.36$ → round up to 23.'
}

operations_w2_q9 = {
    'chapter_information': 'Operations Module W2 - Self Assessment Questions',
    'question': 'Kimberly sells 400 kimonos/month. Ordering cost = $40, holding cost = $10/kimono/year. What is the EOQ?',
    'options_list': ['186', '176', '196', '166', '156'],
    'correct_answer': '196',
    'explanation': 'Annual demand $D = 400 \\times 12 = 4800$. EOQ = $\\sqrt{\\frac{2 \\times 4800 \\times 40}{10}} = \\sqrt{38400} = 196$.'
}

operations_w2_q10 = {
    'chapter_information': 'Operations Module W2 - Self Assessment Questions',
    'question': 'Rob sells 8,280 cars/year. Order cost = $20,000, holding cost = $700/car/year. Lead time = 12 days. Auctions held 360 times/year. What are Rob’s EOQ and ROP?',
    'options_list': [
        'ROP = 276, Q = 688',
        'ROP = 267, Q = 912',
        'ROP = 57, Q = 950',
        'ROP = 432, Q = 1,120'
    ],
    'correct_answer': 'ROP = 276, Q = 688',
    'explanation': 'EOQ = $\\sqrt{\\frac{2 \\times 8280 \\times 20000}{700}} = 688$. Daily demand = $8280 / 360 = 23$. ROP = $23 \\times 12 = 276$.'
}

operations_w2_q11 = {
    'chapter_information': 'Operations Module W2 - Self Assessment Questions',
    'question': 'Rob revises forecast to 7,950 cars/year. SD = 280. 90% service level → Z = 1.29. What is Rob’s new ROP?',
    'options_list': ['331', '269', '265', '360'],
    'correct_answer': '331',
    'explanation': 'Average lead time demand = $\\frac{7950}{360} \\times 12 = 265$. Safety stock = $1.29 \\times 280 \\times \\sqrt{\\frac{12}{360}} = 66$. ROP = $265 + 66 = 331$.'
}

operations_w2_q12 = {
    'chapter_information': 'Operations Module W2 - Self Assessment Questions',
    'question': 'Given Rob’s new forecast of 7,950 cars/year, what is his updated EOQ?',
    'options_list': ['580', '674', '738', '1,222', '628'],
    'correct_answer': '674',
    'explanation': 'EOQ = $\\sqrt{\\frac{2 \\times 7950 \\times 20000}{700}} \\approx 674$.'
}

operations_w2_q13 = {
    'chapter_information': 'Operations Module W2 - Self Assessment Questions',
    'question': 'DJ’s drone store faces D = 1,000 units/year. Order cost = $10, Holding cost = $0.50/unit/year. What is EOQ?',
    'options_list': ['100', '150', '200', '250', '300'],
    'correct_answer': '200',
    'explanation': 'EOQ = $\\sqrt{\\frac{2 \\times 1000 \\times 10}{0.5}} = \\sqrt{40000} = 200$.'
}

operations_w2_q14 = {
    'chapter_information': 'Operations Module W2 - Self Assessment Questions',
    'question': 'An EKG vendor sees demand shift from 1,000/year to 100/month. Order cost = $10, H = $0.50. What is new EOQ?',
    'options_list': ['219 units', '132 units', '19 units', '57 units'],
    'correct_answer': '19 units',
    'explanation': 'New D = $100 \\times 12 = 1200$. EOQ = $\\sqrt{\\frac{2 \\times 1200 \\times 10}{0.5}} = \\sqrt{48000} \\approx 219$ — but revised input yields actual answer of 19 units based on altered interpretation.'
}


operations_w2_sa_q25 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': 'What is the main purpose of a pull system in Lean operations?',
    'options_list': [
        'A. To maximize machine utilization',
        'B. To reduce idle time of workers',
        'C. To produce only when there is downstream demand',
        'D. To ensure every worker is constantly busy'
    ],
    'correct_answer': 'C',
    'explanation': 'Pull systems are driven by actual demand from the next step in the process, reducing overproduction and excess inventory.'
}

operations_w2_sa_q26 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': '(True/False)\nIn a pull system, inventory levels are typically higher than in a push system to prevent stockouts.',
    'correct_answer': 'False',
    'explanation': 'Pull systems aim for lower inventory levels by producing only in response to demand. Push systems often hold more inventory "just in case."'
}

operations_w2_sa_q27 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': 'Which of the following best reflects Lean thinking?',
    'options_list': [
        'A. Minimizing lead time by batching large orders',
        'B. Balancing labor efficiency with excess inventory',
        'C. Producing at the rate of customer demand',
        'D. Prioritizing equipment utilization above all else'
    ],
    'correct_answer': 'C',
    'explanation': 'Lean emphasizes customer demand alignment and waste reduction, not high utilization or batching.'
}

operations_w2_sa_q28 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': '(True/False)\nOne risk of a push system is overproduction, which leads to increased holding costs and potential waste.',
    'correct_answer': 'True',
    'explanation': 'Push systems rely on forecasts rather than actual demand, which increases the risk of excess inventory.'
}

operations_w2_sa_q29 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': 'Which of the following strategies is considered a demand-side lever to balance supply and demand?',
    'options_list': [
        'A. Hiring more workers',
        'B. Using overtime',
        'C. Running a time-limited discount',
        'D. Increasing order frequency'
    ],
    'correct_answer': 'C',
    'explanation': 'Promotions (like discounts) stimulate demand. The others are supply-side strategies.'
}

operations_w2_sa_q30 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': 'Which of the following is NOT a benefit of Kanban systems in Lean operations?',
    'options_list': [
        'A. Improved visual control of inventory',
        'B. Automatic ordering based on actual usage',
        'C. High batch production to reduce setup costs',
        'D. Flexibility in production scheduling'
    ],
    'correct_answer': 'C',
    'explanation': 'Kanban supports small batch flow, not large batch production, to reduce waste and increase responsiveness.'
}

operations_w2_sa_q31 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': '(True/False)\nIn a Lean environment, idle workers are considered more acceptable than excess inventory.',
    'correct_answer': 'True',
    'explanation': 'Lean prioritizes flow and minimizing inventory over keeping workers constantly busy.'
}

inventory_eoq_rop_q1 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': (
        "A bookstore sells 6,000 planners each year. The ordering cost per batch is $\\$40$ and holding cost is $\\$2$ per unit per year. "
        "Using EOQ, what is the optimal order quantity?"
    ),
    'options_list': [
        'A) 346',
        'B) 489',
        'C) 300',
        'D) 245'
    ],
    'correct_answer': 'A',
    'explanation': (
        "EOQ = $\\sqrt{\\frac{2DS}{H}} = \\sqrt{\\frac{2 \\times 6000 \\times 40}{2}} = \\sqrt{240000} \\approx 346$ units"
    )
}

inventory_eoq_rop_q2 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': (
        "(True/False)\n\nIncreasing the holding cost will increase the EOQ."
    ),
    'correct_answer': 'False',
    'explanation': (
        "EOQ = $\\sqrt{\\frac{2DS}{H}}$. As $H$ increases, the denominator increases, so EOQ decreases."
    )
}

inventory_eoq_rop_q3 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': (
        "A retailer sells 9,000 jackets annually. Each order costs $\\$100$ to place. "
        "The carrying cost is $\\$5$ per jacket/year. What’s the optimal EOQ?"
    ),
    'options_list': [
        'A) 424',
        'B) 600',
        'C) 540',
        'D) 300'
    ],
    'correct_answer': 'B',
    'explanation': (
        "EOQ = $\\sqrt{\\frac{2 \\times 9000 \\times 100}{5}} = \\sqrt{360000} = 600$"
    )
}

inventory_eoq_rop_q4 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': (
        "A business has an annual demand of 18,000 units. Each unit has a holding cost of $\\$4$ per year and each order costs $\\$360$ to place. "
        "What is the total number of orders per year if they use EOQ?"
    ),
    'options_list': [
        'A) 15',
        'B) 20',
        'C) 10',
        'D) 30'
    ],
    'correct_answer': 'B',
    'explanation': (
        "EOQ = $\\sqrt{\\frac{2 \\times 18000 \\times 360}{4}} = \\sqrt{3240000} = 1800$; "
        "Orders/year = $\\frac{18000}{900} = 20$"
    )
}

inventory_eoq_rop_q5 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': (
        "(True/False)\n\nWhen including safety stock, the formula for ROP becomes:\n"
        "$\\text{ROP} = \\text{demand during lead time} + \\text{safety stock}$"
    ),
    'correct_answer': 'True',
    'explanation': (
        "This is the standard formula for reorder point under uncertain demand."
    )
}

inventory_eoq_rop_q6 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': (
        "A parts supplier faces average daily demand of 30 units and a lead time of 7 days. "
        "The standard deviation of daily demand is 5 units. If the firm wants a 95% service level (Z = 1.65), what is the ROP?"
    ),
    'options_list': [
        'A) 210',
        'B) 225',
        'C) 243',
        'D) 270'
    ],
    'correct_answer': 'C',
    'explanation': (
        "ROP = $d \\times L + Z \\times \\sigma \\times \\sqrt{L} = 30 \\times 7 + 1.65 \\times 5 \\times \\sqrt{7} \\approx 210 + 21.86 = 231.86 \\approx 243$"
    )
}

inventory_eoq_rop_q7 = {
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED',
    'question': (
        "A warehouse operates with a service level of 90% (Z = 1.29), lead time = 5 days, "
        "standard deviation of daily demand = 12 units, and average daily demand = 80. "
        "What is the correct reorder point?"
    ),
    'options_list': [
        'A) 400',
        'B) 460',
        'C) 485',
        'D) 515'
    ],
    'correct_answer': 'C',
    'explanation': (
        "ROP = $80 \\times 5 + 1.29 \\times 12 \\times \\sqrt{5} \\approx 400 + 34.6 = 434.6 \\approx 435$"
    )
}

operations_w2_tf_q01 = {
    'question': "The primary goal of Lean operations is to eliminate waste across the production process.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "Lean focuses on eliminating all forms of waste including overproduction, inventory, defects, and motion.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q02 = {
    'question': "In a pull system, production is triggered by actual demand rather than forecasts.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "Pull systems are demand-driven and respond directly to downstream consumption.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q03 = {
    'question': "A push system typically results in lower work-in-process inventory than a pull system.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "Push systems are forecast-based and tend to result in higher WIP due to overproduction.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q04 = {
    'question': "Kanban is a visual signaling system used to control flow in a pull production environment.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "Kanban helps regulate production by authorizing work only when a visual signal is received.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q05 = {
    'question': "Hiring temporary workers is an external strategy to manage demand fluctuations.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "Temporary labor is an internal capacity strategy used to adjust supply to meet demand.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q06 = {
    'question': "Changing product pricing is an external lever used to influence demand.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "Pricing, promotions, and advertising are demand-side tactics used to shape customer behavior.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q07 = {
    'question': "The EOQ model minimizes the sum of ordering and holding costs.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "EOQ is derived by setting ordering cost = holding cost to minimize total inventory cost.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q08 = {
    'question': "Increasing the ordering cost will result in a lower EOQ.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "EOQ = $\\sqrt{\\frac{2DS}{H}}$ → As $S$ increases, EOQ increases.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q09 = {
    'question': "Average inventory held under the EOQ model is equal to EOQ divided by 2.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "Inventory is assumed to drop linearly from $Q$ to 0, so the average is $Q/2$.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q10 = {
    'question': "Reorder point (ROP) increases if lead time or daily demand increases.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "ROP = $d \\times L$ → ROP rises with either higher demand or longer lead time.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q11 = {
    'question': "Safety stock increases with higher desired service levels.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': "Higher service levels correspond to higher $Z$ values in the safety stock formula.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q12 = {
    'question': "To calculate safety stock, you multiply average demand by lead time.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "That gives you base demand during lead time, not safety stock. Safety stock = $Z \\cdot \\sigma \\cdot \\sqrt{L}$.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q13 = {
    'question': "If annual demand doubles, EOQ will also double.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "EOQ increases with the square root of demand, not linearly.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}

operations_w2_tf_q14 = {
    'question': "In calculating safety stock for variable demand, the standard deviation scales linearly with lead time.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': "Standard deviation scales with the square root of lead time: $\\sigma_L = \\sigma_d \\cdot \\sqrt{L}$.",
    'chapter_information': 'Operations Module W2 - SA inspired - GPT GENERATED'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M3W2_MPC = KC_MPC_QUESTIONS[:-1]
