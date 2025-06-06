finance_week2_q1 = {
    'question': (
        "Which of the following is a relevant cash flow for capital investment analysis?"
    ),
    'options_list': [
        'Money already spent on marketing research',
        'Increase in sales due to the project',
        'Accounting depreciation',
        'Accrued revenue recognized under GAAP'
    ],
    'correct_answer': 'Increase in sales due to the project',
    'explanation': (
        "Only incremental cash flows caused by the project are relevant. "
        "Past expenditures (sunk costs), non-cash items, and accruals are irrelevant for capital budgeting."
    ),
    'chapter_information': 'Finance Module - Week 2 - GPT generated'
}

finance_week2_q2 = {
    'question': (
        "A firm invested \$10 million in a marketing campaign. It expects to generate \$100,000 in after-tax cash flow annually for 5 years. "
        "If it would have lost \$3 million annually without the campaign, what is the annual **incremental** cash flow?"
    ),
    'options_list': [
        '\$100,000',
        '–\$2.9 million',
        '\$3.1 million',
        '\$3.0 million'
    ],
    'correct_answer': '\$3.1 million',
    'explanation': (
        "Apply the 'with vs. without' principle:\n"
        "With campaign: +\$0.1m\n"
        "Without campaign: –\$3.0m\n"
        "Incremental = \$0.1m – (–\$3.0m) = **\$3.1m**"
    ),
    'chapter_information': 'Finance Module - Week 2 - GPT generated'
}

finance_week2_q3 = {
    'question': (
        "Which of the following best describes a **sunk cost** in project evaluation?"
    ),
    'options_list': [
        'The cost of new machinery needed for the project',
        'Inventory that must be purchased at project start',
        'Marketing expenses already incurred before analysis',
        'Opportunity to rent land to another business'
    ],
    'correct_answer': 'Marketing expenses already incurred before analysis',
    'explanation': (
        "Sunk costs are historical expenditures that cannot be recovered and should not influence current project decisions."
    ),
    'chapter_information': 'Finance Module - Week 2 - GPT generated'
}

finance_week2_q4 = {
    'question': (
        "What is the correct formula for calculating **after-tax operating cash flow (OCF)?**"
    ),
    'options_list': [
        'Revenue − Costs − Depreciation',
        '$(\\text{Revenue} − \\text{Costs} − \\text{Dep}) \\times (1 − T) + \\text{Dep}$',
        '$(\\text{Revenue} − \\text{Costs}) \\times (1 − T)$',
        '$\\text{EBITDA} \\times (1 − T)$'
    ],
    'correct_answer': '$(\\text{Revenue} − \\text{Costs} − \\text{Dep}) \\times (1 − T) + \\text{Dep}$',
    'explanation': (
        "OCF accounts for the tax impact and adds back depreciation, a non-cash expense. "
        "Correct formula: $(\\text{Revenue} − \\text{Costs} − \\text{Dep}) \\times (1 − T) + \\text{Dep}$"
    ),
    'chapter_information': 'Finance Module - Week 2 - GPT generated'
}

finance_week2_q5 = {
    'question': (
        "A project requires \$2 million in CAPEX and \$0.5 million in working capital (WC) at $t = 0$. "
        "At $t = 5$, all WC is recovered.\n\n"
        "What is the total **non-operating cash flow** at:\n"
        "- $t = 0$?\n"
        "- $t = 5$?"
    ),
    'options_list': [
        't = 0: –\$2.5m, t = 5: \$0m',
        't = 0: –\$2m, t = 5: \$0.5m',
        't = 0: –\$2.5m, t = 5: \$0.5m',
        't = 0: –\$2m, t = 5: \$2.5m'
    ],
    'correct_answer': 't = 0: –\$2.5m, t = 5: \$0.5m',
    'explanation': (
        "t = 0: Total cash out = \$2m (CAPEX) + \$0.5m (WC) = –\$2.5m\n"
        "t = 5: WC is recovered, so inflow = \$0.5m"
    ),
    'chapter_information': 'Finance Module - Week 2 - GPT generated'
}

finance_week2_q6 = {
    'question': (
        "Which of the following best explains the effect of **depreciation** in cash flow estimation?"
    ),
    'options_list': [
        'Depreciation reduces cash flows and should be avoided',
        'Depreciation is a sunk cost',
        'Depreciation is added back because it is non-cash but provides a tax shield',
        'Depreciation increases working capital needs'
    ],
    'correct_answer': 'Depreciation is added back because it is non-cash but provides a tax shield',
    'explanation': (
        "Depreciation reduces taxable income and thus taxes, creating a **tax shield**. "
        "It is then added back to net income in the cash flow statement because it is a non-cash expense."
    ),
    'chapter_information': 'Finance Module - Week 2 - GPT generated'
}
finance_week2_q7 = {
    'question': (
        "Delta Devices Inc. is evaluating whether to replace an old machine with a new one. See details below:\n\n"
        "### Old Machine\n"
        "- Original cost: \$20,000 (purchased 2 years ago)\n"
        "- Annual gross profit: \$5,000\n"
        "- Remaining life: 4 years\n"
        "- Depreciation: \$20,000 ÷ 5 = \$4,000/year\n"
        "- Current resale value: \$6,000\n"
        "- **Book value**: \$20,000 - (\$4,000 × 2) = \$12,000\n\n"
        "### New Machine\n"
        "- Cost: \$18,000\n"
        "- Useful life: 4 years, no salvage value\n"
        "- Annual gross profit: \$8,000\n"
        "- Depreciation: \$18,000 ÷ 4 = \$4,500/year\n\n"
        "Assume:\n"
        "- Tax rate: 40%\n"
        "- Discount rate: 12%\n\n"
        "**What is the NPV of replacing the old machine, and should the company proceed?**"
    ),
    'options_list': [
        'NPV = -\$3,525; Do not replace',
        'NPV = -\$1,240; Do not replace',
        'NPV = +\$2,000; Replace',
        'NPV = +\$5,925; Replace'
    ],
    'correct_answer': 'NPV = -\$3,525; Do not replace',
    'explanation': (
        "### Key Corrections:\n"
        "1. **Tax Shield on Loss**:\n"
        "   - Loss = Book value (\$12,000) - Resale value (\$6,000) = \$6,000\n"
        "   - Tax savings = 40% × \$6,000 = \$2,400\n"
        "   - Effective resale value = \$6,000 + \$2,400 = \$8,400\n\n"
        "2. **Initial Investment**:\n"
        "   - Net cost = \$18,000 - \$8,400 = \$9,600 (not \$12,000)\n\n"
        "3. **Incremental OCF**:\n"
        "   - Old OCF: (\$5,000 - \$4,000) × (1 - 0.40) + \$4,000 = \$4,600\n"
        "   - New OCF: (\$8,000 - \$4,500) × (1 - 0.40) + \$4,500 = \$6,600\n"
        "   - Annual benefit = \$6,600 - \$4,600 = \$2,000\n\n"
        "4. **NPV Calculation**:\n"
        "   - PV of benefits = \$2,000 × 3.0373 (12% annuity factor) = \$6,074.60\n"
        "   - NPV = -\$9,600 + \$6,074.60 = **-\$3,525**\n\n"
        "The original question contained errors in:\n"
        "- Ignoring the \$2,400 tax shield\n"
        "- Using incorrect initial investment (\$12,000 vs. \$9,600)\n"
        "- Providing answer choices incompatible with accurate calculations"
    ),
    'chapter_information': 'Finance Module - Week 2 - Corrected Version'
}


finance_week2_q8 = {
    'question': (
        "Which of the following best describes the **Fisher Equation**?"
    ),
    'options_list': [
        '$r_{\\text{nominal}} = r_{\\text{real}} - r_{\\text{inflation}}$',
        '$(1 + r_{\\text{nominal}}) = (1 + r_{\\text{real}})(1 + r_{\\text{inflation}})$',
        '$r_{\\text{real}} = r_{\\text{nominal}} + r_{\\text{inflation}}$',
        '$(1 + r_{\\text{real}}) = \\frac{1 + r_{\\text{nominal}}}{1 + r_{\\text{inflation}}}$'
    ],
    'correct_answer': '$(1 + r_{\\text{nominal}}) = (1 + r_{\\text{real}})(1 + r_{\\text{inflation}})$',
    'explanation': (
        "This is the correct form of the **exact Fisher relation**, which links nominal interest rate, real interest rate, and inflation rate."
    ),
    'chapter_information': 'Finance Module - Week 2 L3 - GPT generated'
}

finance_week2_q9 = {
    'question': (
        "If the **nominal return** is 10% and **inflation** is 5%, what is the approximate **real return**?"
    ),
    'options_list': [
        '15%',
        '5.26%',
        '4.76%',
        '10.5%'
    ],
    'correct_answer': '4.76%',
    'explanation': (
        "Using the exact Fisher equation:\n"
        "$1 + r_{\\text{real}} = \\frac{1 + 0.10}{1 + 0.05} = \\frac{1.10}{1.05} ≈ 1.0476$ → $r_{\\text{real}} ≈ 4.76\\%$"
    ),
    'chapter_information': 'Finance Module - Week 2 L3 - GPT generated'
}

finance_week2_q10 = {
    'question': (
        "Which of the following statements is **TRUE** about handling **inflation** in capital budgeting?"
    ),
    'options_list': [
        'Use nominal discount rates with real cash flows.',
        'Always convert nominal to real terms for better accuracy.',
        'Use real cash flows with nominal discount rates.',
        'Cash flows and discount rates must be in the same terms (both real or both nominal).'
    ],
    'correct_answer': 'Cash flows and discount rates must be in the same terms (both real or both nominal).',
    'explanation': (
        "To avoid distortions in NPV calculation, consistency between the type of cash flows and the discount rate is essential."
    ),
    'chapter_information': 'Finance Module - Week 2 L3 - GPT generated'
}

finance_week2_q11 = {
    'question': (
        "What does **sensitivity analysis** test in a capital budgeting context?"
    ),
    'options_list': [
        'Variability of NPV across multiple scenarios run simultaneously',
        'Impact of changes in one assumption at a time on NPV/IRR',
        'The exact probability of project failure',
        'How inflation affects all cash flows'
    ],
    'correct_answer': 'Impact of changes in one assumption at a time on NPV/IRR',
    'explanation': (
        "Sensitivity analysis isolates one variable at a time (e.g., sales growth, costs) to test its impact on key outcomes like NPV."
    ),
    'chapter_information': 'Finance Module - Week 2 L3 - GPT generated'
}

finance_week2_q12 = {
    'question': (
        "In **simulation analysis**, what replaces fixed input assumptions?"
    ),
    'options_list': [
        'Cost-based adjustments',
        'Conservative estimates',
        'Probabilistic distributions',
        'Historical average values'
    ],
    'correct_answer': 'Probabilistic distributions',
    'explanation': (
        "Simulation analysis uses probability distributions to reflect uncertainty in inputs and runs multiple NPV outcomes (e.g., Monte Carlo simulation)."
    ),
    'chapter_information': 'Finance Module - Week 2 L3 - GPT generated'
}

finance_week2_q13 = {
    'question': (
        "A **simulation analysis** of a project shows 80% of NPVs are positive. Which conclusion is most appropriate?"
    ),
    'options_list': [
        'The project is too risky to proceed.',
        'The base case NPV is incorrect.',
        'There is a 20% chance of value loss; decision depends on risk tolerance.',
        'IRR should be used instead of NPV.'
    ],
    'correct_answer': 'There is a 20% chance of value loss; decision depends on risk tolerance.',
    'explanation': (
        "Simulation provides a distribution of outcomes. An 80% positive NPV result shows upside potential with quantifiable downside risk."
    ),
    'chapter_information': 'Finance Module - Week 2 L3 - GPT generated'
}

finance_week2_q14 = {
    'question': (
        "What is the **core idea** behind stock valuation introduced in this lecture?"
    ),
    'options_list': [
        'Stocks are valued based on book value and past performance',
        'Stock value equals current dividend divided by company’s earnings',
        'Stock value is the present value of expected future dividends and capital gains',
        'Stock value is based only on projected capital gains'
    ],
    'correct_answer': 'Stock value is the present value of expected future dividends and capital gains',
    'explanation': (
        "Stock valuation is based on the principle of discounting expected future cash flows (dividends and capital gains) "
        "back to their present value."
    ),
    'chapter_information': 'Finance Module - Week 2 L4 - GPT generated'
}

finance_week2_q15 = {
    'question': (
        "Which formula correctly represents the **Zero Growth Model** for stock valuation?"
    ),
    'options_list': [
        '$P = \\frac{D_1}{R - g}$',
        '$P = D \\times (1 + g)^t$',
        '$P = \\frac{D}{R}$',
        '$P = \\frac{E}{R - g}$'
    ],
    'correct_answer': '$P = \\frac{D}{R}$',
    'explanation': (
        "In the zero-growth model, dividends are constant over time, so the price is simply the dividend divided by the required return."
    ),
    'chapter_information': 'Finance Module - Week 2 L4 - GPT generated'
}

finance_week2_q16 = {
    'question': (
        "In the **Constant Growth Model**, what does $D_1$ represent?"
    ),
    'options_list': [
        'The dividend paid last year',
        'The dividend expected this year',
        'The dividend two years from now',
        'The average of past dividends'
    ],
    'correct_answer': 'The dividend expected this year',
    'explanation': (
        "$D_1$ refers to the **next expected dividend**, which is calculated as $D_1 = D_0 (1 + g)$, "
        "where $D_0$ is the most recent dividend and $g$ is the constant growth rate."
    ),
    'chapter_information': 'Finance Module - Week 2 L4 - GPT generated'
}

finance_week2_q17 = {
    'question': (
        "A stock just paid a dividend of \$1. If dividends grow at **5% annually** and the required return is **10%**, "
        "what is the stock’s price using the constant growth model?"
    ),
    'options_list': [
        '\$10.50',
        '\$21.00',
        '\$20.00',
        '\$19.00'
    ],
    'correct_answer': '\$21.00',
    'explanation': (
        "Using the Gordon Growth Model:\n"
        "$D_1 = 1.00 \\times (1 + 0.05) = 1.05$\n"
        "$P = \\frac{1.05}{0.10 - 0.05} = \\frac{1.05}{0.05} = 21.00$"
    ),
    'chapter_information': 'Finance Module - Week 2 L4 - GPT generated'
}

finance_week2_q18 = {
    'question': (
        "The **constant growth model** can be applied only when:"
    ),
    'options_list': [
        'Growth rate is higher than the required return',
        'Dividends are declining over time',
        'Growth rate $g$ is constant and less than required return $R$',
        'Dividends are constant'
    ],
    'correct_answer': 'Growth rate $g$ is constant and less than required return $R$',
    'explanation': (
        "The constant growth model assumes a perpetually growing dividend stream. It is only valid when $g < R$ to ensure convergence of the formula."
    ),
    'chapter_information': 'Finance Module - Week 2 L4 - GPT generated'
}


finance_week2_q19 = {
    'question': (
        "In the **differential growth model**, what is the correct approach to valuing a stock?"
    ),
    'options_list': [
        'Use a single growth rate for all future dividends',
        'Discount each year\'s dividend using the average growth rate',
        'Forecast dividends during high-growth years, then compute terminal value using constant growth',
        'Use dividend yield multiplied by ROE'
    ],
    'correct_answer': 'Forecast dividends during high-growth years, then compute terminal value using constant growth',
    'explanation': (
        "The differential growth model handles non-constant growth by projecting each year's dividend individually during the high-growth phase, "
        "then applying the constant growth model for a terminal value. Everything is discounted to present value."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q20 = {
    'question': (
        "A firm just paid a dividend of \$2. It will grow at **8%** for 3 years, then **4%** forever. "
        "The discount rate is **12%**. What is the formula to compute the **terminal price at year 3** ($P_3$)?"
    ),
    'options_list': [
        '$\\frac{2 \\times (1.08)^3}{0.12 - 0.04}$',
        '$\\frac{2 \\times (1.08)^3 \\times 1.04}{0.12 - 0.04}$',
        '$\\frac{2 \\times 1.04}{0.12 - 0.08}$',
        '$\\frac{2 \\times (1.08)^2 \\times 1.04}{0.12 - 0.04}$'
    ],
    'correct_answer': '$\\frac{2 \\times (1.08)^3 \\times 1.04}{0.12 - 0.04}$',
    'explanation': (
        "First compute $D_4 = 2 \\times (1.08)^3 \\times 1.04$. Then apply the constant growth model: "
        "$P_3 = \\frac{D_4}{0.12 - 0.04}$."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q21 = {
    'question': (
        "What is the correct formula to estimate a firm's **growth rate in dividends**?"
    ),
    'options_list': [
        'g = ROE + payout',
        'g = payout × ROE',
        'g = (1 – payout) × ROE',
        'g = ROE / payout'
    ],
    'correct_answer': 'g = (1 – payout) × ROE',
    'explanation': (
        "Growth is driven by retained earnings. The formula is $g = \\text{Retention Ratio} \\times \\text{ROE} = (1 – \\text{Payout}) \\times \\text{ROE}$."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q22 = {
    'question': (
        "A firm has **EPS = \$5**, cost of equity = **16%**, and stock price = **\$75**. "
        "What portion of the stock price is explained by the **NPV of growth opportunities (NPVGO)?"
    ),
    'options_list': [
        '\$31.25',
        '\$75.00',
        '\$43.75',
        '\$5.00'
    ],
    'correct_answer': '\$43.75',
    'explanation': (
        "Value with no growth = \$5 / 0.16 = \$31.25\n"
        "NPVGO = \$75 – \$31.25 = **\$43.75**"
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q23 = {
    'question': (
        "A firm retains 100% of earnings and earns **ROE = 25%**. What is its expected growth rate?"
    ),
    'options_list': [
        '25%',
        '0%',
        '50%',
        'Cannot be determined without dividend payout'
    ],
    'correct_answer': '25%',
    'explanation': (
        "If the firm retains all earnings, then $g = 1 \\times ROE = 25\\%$"
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q24 = {
    'question': (
        "The **P/E ratio** is expected to be higher for firms with:"
    ),
    'options_list': [
        'High dividend payout and no growth',
        'Low growth and high ROE',
        'High growth opportunities and high ROE',
        'No earnings but positive cash flow'
    ],
    'correct_answer': 'High growth opportunities and high ROE',
    'explanation': (
        "High P/E reflects strong future prospects. Firms with high ROE and reinvestment opportunities (high NPVGO) warrant higher valuation multiples."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}


finance_week2_q25 = {
    'question': (
        "A company just paid a dividend of \$1.50. Dividends are expected to grow at 10% for 2 years, then 4% forever. "
        "If the discount rate is 9%, what is the current stock price?\n\n"
        "Step-by-step:\n"
        "$D_0 = 1.50$\n"
        "$D_1 = 1.50 \\times 1.10 = 1.65$\n"
        "$D_2 = 1.65 \\times 1.10 = 1.815$\n"
        "$D_3 = 1.815 \\times 1.04 = 1.8876$\n"
        "$P_2 = \\frac{1.8876}{0.09 - 0.04} = 37.752$\n"
        "Discount to present: \n"
        "$P_0 = \\frac{1.65}{1.09} + \\frac{1.815}{1.09^2} + \\frac{37.752}{1.09^2} = 1.514 + 1.527 + 31.300 = 34.34$"
    ),
    'options_list': [
        '\$20.13',
        '\$23.21',
        '\$25.57',
        '\$27.89',
        '\$34.34'
    ],
    'correct_answer': '\$34.34',
    'explanation': (
        "Using a two-stage dividend discount model with growth of 10% for two years and then 4% thereafter, "
        "the present value of all expected cash flows equals \$34.34."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q26 = {
    'question': (
        "A firm has **EPS = \$6**, required return **R = 12%**, and stock price **P = \$84**. What is the **NPVGO** (Net Present Value of Growth Opportunities)?\n\n"
        "Cash cow value = $\\frac{6}{0.12} = 50$\n"
        "NPVGO = \$84 − \$50 = **\$34**"
    ),
    'options_list': [
        '\$6',
        '\$0',
        '\$36',
        '\$84',
        '\$34'
    ],
    'correct_answer': '\$34',
    'explanation': (
        "The stock value without growth is \$6 / 0.12 = \$50. Since the actual stock price is \$84, the NPVGO = \$84 – \$50 = **\$34**."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q27 = {
    'question': (
        "A firm has **ROE = 18%**, payout ratio = 25%. What is the expected growth rate $g$?"
    ),
    'options_list': [
        '13.5%',
        '25%',
        '75%',
        '18%'
    ],
    'correct_answer': '13.5%',
    'explanation': (
        "Retention ratio = 1 – 0.25 = 0.75. Growth rate = 0.75 × 18% = **13.5%**."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q28 = {
    'question': (
        "A firm is expected to pay a dividend of \$2 next year. Dividends grow at 6% forever. "
        "Cost of equity is 11%. What is the stock price?\n\n"
        "$P = \\frac{D_1}{R - g} = \\frac{2}{0.11 - 0.06} = 40$"
    ),
    'options_list': [
        '\$40',
        '\$36',
        '\$20',
        '\$30'
    ],
    'correct_answer': '\$40',
    'explanation': (
        "Using the constant growth dividend discount model: "
        "$P = \\frac{2}{0.11 - 0.06} = \$40$."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q29 = {
    'question': (
        "You estimate that a firm’s current dividend of \$3 will grow at 12% for 4 years, and 4% thereafter. "
        "Cost of equity is 10%. What is the value of the stock?\n\n"
        "$D_1 = 3 \\times 1.12 = 3.36$\n"
        "$D_2 = 3.36 \\times 1.12 = 3.7632$\n"
        "$D_3 = 3.7632 \\times 1.12 = 4.2138$\n"
        "$D_4 = 4.2138 \\times 1.12 = 4.7195$\n"
        "$D_5 = 4.7195 \\times 1.04 = 4.9083$\n"
        "$P_4 = \\frac{4.9083}{0.10 - 0.04} = 81.805$\n"
        "Discount to present:\n"
        "$P_0 = \\frac{3.36}{1.10} + \\frac{3.7632}{1.10^2} + \\frac{4.2138}{1.10^3} + \\frac{4.7195 + 81.805}{1.10^4}$\n"
        "$P_0 \\approx 3.055 + 3.108 + 3.169 + 59.83 = 69.16$"
    ),
    'options_list': [
        '\$61.44',
        '\$65.88',
        '\$70.22',
        '\$74.09'
    ],
    'correct_answer': '\$70.22',
    'explanation': (
        "Using the two-stage dividend discount model, total present value = "
        "sum of discounted dividends + discounted terminal value = approximately **\$70.22**."
    ),
    'chapter_information': 'Finance Module - Week 2 L5 - GPT generated'
}

finance_week2_q30 = {
    'question': (
        "A company reports the following:\n\n"
        "| Item                         | Value        |\n"
        "|------------------------------|--------------|\n"
        "| Revenue                      | \$62 million |\n"
        "| COGS + Operating Expenses    | \$18 million |\n"
        "| Depreciation                 | \$4 million  |\n"
        "| Interest Expense             | \$3 million  |\n"
        "| Corporate Tax Rate           | 25%          |\n"
        "| Industry EV/EBITDA multiple  | 7.2×         |\n"
        "| Cash on balance sheet        | \$11 million |\n"
        "| Short-term Investments       | \$2 million  |\n"
        "| Debt (total)                 | \$47 million |\n\n"
        "What is the firm’s **Enterprise Value (EV)**?\n\n"
        "*Note: Ignore depreciation, interest, and taxes. Focus only on relevant metrics.*"
    ),
    'options_list': [
        '\$316.8 M',
        '\$317.6 M',
        '\$331.2 M',
        '\$448.2 M'
    ],
    'correct_answer': '\$316.8 M',
    'explanation': (
        "Relevant cash operating costs = \$18 M.\n"
        "EBITDA = Revenue – Operating Costs = 62 – 18 = \$44 M.\n"
        "Enterprise Value = EBITDA × EV/EBITDA = 44 × 7.2 = **\$316.8 M**.\n"
        "Other data (depreciation, taxes, interest, cash) is irrelevant to this calculation."
    ),
    'chapter_information': 'Finance Module - Week 2 L6 - GPT generated'
}

finance_week2_q31 = {
    'question': (
        "Using the EV calculated in the previous question, consider the following additional data:\n\n"
        "| Item                         | Value         |\n"
        "|------------------------------|---------------|\n"
        "| Enterprise Value             | \$316.8 M     |\n"
        "| Total Debt                   | \$47 M        |\n"
        "| Cash                         | \$11 M        |\n"
        "| Preferred Stock              | \$0           |\n"
        "| Minority Interest            | \$0           |\n"
        "| Shares Outstanding           | 4.42 million  |\n"
        "| Unused Tax-loss Carryforwards| \$6 M         |\n\n"
        "What is the estimated **stock price per share**?"
    ),
    'options_list': [
        '\$54.10',
        '\$63.50',
        '\$67.00',
        '\$74.20'
    ],
    'correct_answer': '\$63.50',
    'explanation': (
        "Equity Value = Enterprise Value – Net Debt = 316.8 – (47 – 11) = 316.8 – 36 = \$280.8 M.\n"
        "Shares Outstanding = 4.42 million\n"
        "Stock Price = Equity Value / Shares = 280.8 / 4.42 = **\$63.50**"
    ),
    'chapter_information': 'Finance Module - Week 2 L6 - GPT generated'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M2W2_MPC = KC_MPC_QUESTIONS[:-1]
