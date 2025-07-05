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

operations_w3_q11 = {
    'question': "A retailer pays $6 for a product, sells it for $12, and can return unsold units for a $2 credit. What is the underage cost (CU)?",
    'options_list': [
        "A. $4",
        "B. $6",
        "C. $8",
        "D. $10"
    ],
    'correct_answer': "B. $6",
    'explanation': "Underage cost $CU = p - c = 12 - 6 = 6$",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q12 = {
    'question': "In the classic newsvendor model, which parameter change lowers the optimal order quantity?",
    'options_list': [
        "A. Higher selling price",
        "B. Higher salvage value",
        "C. Lower unit cost",
        "D. Lower underage cost"
    ],
    'correct_answer': "D. Lower underage cost",
    'explanation': "Lower $CU$ reduces the critical fractile $CF = \\frac{CU}{CU + CO}$, which reduces optimal order quantity $Q^*$.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q13 = {
    'question': "The critical fractile equals 0.80. What is the implied overage-to-underage cost ratio $CO:CU$?",
    'options_list': [
        "A. 1 : 4",
        "B. 1 : 3",
        "C. 1 : 1",
        "D. 4 : 1"
    ],
    'correct_answer': "A. 1 : 4",
    'explanation': "Given $CF = 0.80 = \\frac{CU}{CU + CO} \\Rightarrow CO = 0.25 \\cdot CU$, so $CO:CU = 1:4$.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q14 = {
    'question': "Which action most directly reduces the impact of order batching on the bullwhip effect?",
    'options_list': [
        "A. Volume-based price discounts",
        "B. Smaller, more frequent replenishments",
        "C. Longer lead times",
        "D. Seasonal promotions"
    ],
    'correct_answer': "B. Smaller, more frequent replenishments",
    'explanation': "Frequent, smaller orders reduce demand variability seen by upstream suppliers, lowering bullwhip effect.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q15 = {
    'question': "A supplier shares real-time POS data with downstream partners. Which bullwhip cause is primarily addressed?",
    'options_list': [
        "A. Forecast error",
        "B. Price fluctuation",
        "C. Information delay",
        "D. Shortage gaming"
    ],
    'correct_answer': "C. Information delay",
    'explanation': "Sharing POS data reduces lags and distortions in information, directly addressing information delay.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q16 = {
    'question': "Demand for holiday ornaments is normally distributed with mean 15,000 units and standard deviation 2,500 units. If the optimal service level is 60%, what z-value should be used?",
    'options_list': [
        "A. 0.25",
        "B. 0.52",
        "C. 0.84",
        "D. 1.28"
    ],
    'correct_answer': "A. 0.25",
    'explanation': "From standard normal tables, $z = 0.25$ corresponds to a cumulative probability of 60%.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q17 = {
    'question': "For a grocery chain, dairy products have short shelf lives. Which model characteristic justifies using the newsvendor framework?",
    'options_list': [
        "A. Low margin",
        "B. Single selling period",
        "C. Constant lead time",
        "D. Price elasticity"
    ],
    'correct_answer': "B. Single selling period",
    'explanation': "Newsvendor applies when inventory decisions are made for one short selling window, as with perishables.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q18 = {
    'question': "A wholesaler plans to buy back unsold inventory at 40% of the retailer’s purchase cost. How does this buy-back influence the retailer’s critical fractile?",
    'options_list': [
        "A. Decreases it",
        "B. Increases it",
        "C. Leaves it unchanged",
        "D. Eliminates its use"
    ],
    'correct_answer': "B. Increases it",
    'explanation': "Buy-backs increase salvage value, lowering $CO$ and raising $CF = \\frac{CU}{CU + CO}$.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q19 = {
    'question': "Which metric best quantifies amplification in the bullwhip effect?",
    'options_list': [
        "A. Mean absolute deviation of demand",
        "B. Fill rate differential",
        "C. Variance ratio of orders to sales",
        "D. Lead-time demand"
    ],
    'correct_answer': "C. Variance ratio of orders to sales",
    'explanation': "Bullwhip effect is measured by $\\frac{Var(Orders)}{Var(Sales)}$ — higher values mean greater amplification.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q20 = {
    'question': "When salvage value equals unit cost in a newsvendor problem, the optimal service level is closest to:",
    'options_list': [
        "A. 0%",
        "B. 25%",
        "C. 50%",
        "D. 100%"
    ],
    'correct_answer': "D. 100%",
    'explanation': "If salvage value = cost, then $CO = 0$, so $CF = \\frac{CU}{CU + 0} = 1$, implying 100% service level.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q21 = {
    'question': "BuzzCo sells reusable water bottles. Annual demand is 6,000 units. The ordering cost is $20 per order, and the annual holding cost is $0.80 per unit. What is the optimal order quantity using the EOQ model?",
    'options_list': [
        "A. 387",
        "B. 512",
        "C. 625",
        "D. 710",
        "E. 548"
    ],
    'correct_answer': "E. 548",
    'explanation': r"EOQ = \sqrt{\frac{2DS}{H}} = \sqrt{\frac{2 \cdot 6000 \cdot 20}{0.8}} = \sqrt{300000} \approx 547.7 \Rightarrow 548",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q22 = {
    'question': "A bookstore sells 50 units per day of a popular exam guide. It takes 4 days to receive an order. What is the reorder point?",
    'options_list': [
        "A. 100",
        "B. 200",
        "C. 250",
        "D. 300",
        "E. 400"
    ],
    'correct_answer': "B. 200",
    'explanation': r"ROP = \text{daily demand} \times \text{lead time} = 50 \times 4 = 200",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q23 = {
    'question': "A company can buy a part at $12 per unit or receive a discount to $10 per unit if it orders 2,500 units at once. Ordering cost is $100 per order, and holding cost is 20% of unit price. Annual demand is 5,000 units. What should the company do?",
    'options_list': [
        "A. Use the $12 supplier",
        "B. Use the $10 supplier",
        "C. Use either—cost is the same",
        "D. Use $10 supplier only if EOQ ≥ 2,500",
        "E. Use $10 supplier if total cost is minimized"
    ],
    'correct_answer': "E. Use $10 supplier if total cost is minimized",
    'explanation': "Total cost = purchase + ordering + holding. Compare both options to determine minimum cost.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q24 = {
    'question': "A forecast for week 1 was 850 units. Actual demand in week 1 was 920. Using exponential smoothing with α = 0.3, what is the forecast for week 2?",
    'options_list': [
        "A. 871",
        "B. 880",
        "C. 901",
        "D. 860",
        "E. 883"
    ],
    'correct_answer': "A. 871",
    'explanation': r"F_2 = F_1 + \alpha (A_1 - F_1) = 850 + 0.3(920 - 850) = 850 + 21 = 871",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q25 = {
    'question': "Which of the following is NOT a reason to hold safety stock?",
    'options_list': [
        "A. Lead time uncertainty",
        "B. Demand variability",
        "C. Supplier discounts",
        "D. Protection against stockouts",
        "E. Service level targets"
    ],
    'correct_answer': "C. Supplier discounts",
    'explanation': "Supplier discounts affect cycle stock, not safety stock. Safety stock handles variability and uncertainty.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q26 = {
    'question': "A store buys each T-shirt for $25 and sells it for $40. Unsold shirts are donated (no salvage value). What is the critical fractile?",
    'options_list': [
        "A. 0.30",
        "B. 0.60",
        "C. 0.45",
        "D. 0.75",
        "E. 0.85"
    ],
    'correct_answer': "B. 0.60",
    'explanation': r"CU = 40 - 25 = 15,\ CO = 25 - 10 = 15,\ CF = \frac{CU}{CU + CO} = \frac{15}{15 + 10} = 0.60",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q27 = {
    'question': "Which of the following metrics is best for detecting bias in a forecasting method?",
    'options_list': [
        "A. MAD (Mean Absolute Deviation)",
        "B. MAPE (Mean Absolute Percentage Error)",
        "C. MFE (Mean Forecast Error)",
        "D. TS (Tracking Signal)",
        "E. RMSE (Root Mean Square Error)"
    ],
    'correct_answer': "C. MFE (Mean Forecast Error)",
    'explanation': "MFE retains error signs, revealing if forecasts consistently over- or under-predict.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q28 = {
    'question': "If your forecasts are consistently above actual demand, which of the following is true?",
    'options_list': [
        "A. Forecast error values are positive",
        "B. MAD is negative",
        "C. MFE is negative",
        "D. RSFE is near zero",
        "E. Tracking Signal is zero"
    ],
    'correct_answer': "C. MFE is negative",
    'explanation': "Forecast error = Actual - Forecast. If forecasts are too high, the error is negative, so MFE is negative.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q29 = {
    'question': "Which statement is true about exponential smoothing?",
    'options_list': [
        "A. It equally weights the last 3 periods",
        "B. It weights earlier periods more heavily",
        "C. It weights the most recent period most heavily",
        "D. It does not use actual data",
        "E. It requires standard deviation of demand"
    ],
    'correct_answer': "C. It weights the most recent period most heavily",
    'explanation': "Exponential smoothing assigns the highest weight to the most recent observation via the smoothing constant α.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}

operations_w3_q30 = {
    'question': "Which of the following is not typically included in the total annual inventory cost in EOQ analysis?",
    'options_list': [
        "A. Holding cost",
        "B. Ordering cost",
        "C. Purchase cost",
        "D. Stockout cost",
        "E. Transportation cost"
    ],
    'correct_answer': "E. Transportation cost",
    'explanation': "EOQ typically includes holding, ordering, and sometimes purchasing cost. Transportation is usually treated separately.",
    'chapter_information': 'Operations Module W3 - SA INSPIRED - GPT GENERATED'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M3W3_MPC = KC_MPC_QUESTIONS[:-1]
