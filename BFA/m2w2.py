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


a_wee23k2_q1 = {
    'question': (
        "The next dividend payment by Golden Lasso Buffets Inc. will be USD 3.15 per share. "
        "Dividends are expected to grow at 2.2% forever. If the stock sells for USD 49.50 per share, "
        "what is the required rate of return?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '8.56%',
    'explanation': (
        "Using the Gordon Growth Model:\n"
        "$$R = \\frac{D_1}{P_0} + g = \\frac{3.15}{49.50} + 0.022 = 0.0856 \\Rightarrow 8.56\\%$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_we23ek2_q2 = {
    'question': (
        "The next dividend payment by Skippy Inc. will be USD 2.95 per share. "
        "Dividends are expected to grow at 4.8% forever. If the stock sells for USD 53.10 per share, "
        "what is the required rate of return?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '10.36%',
    'explanation': (
        "Using the constant growth DDM:\n"
        "$$R = \\frac{2.95}{53.10} + 0.048 = 0.1036 \\Rightarrow 10.36\\%$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_we23ek2_q3 = {
    'question': (
        "Gruber Corp. pays a constant dividend of USD 8.50 for the next 11 years, "
        "after which no dividends will be paid. If the required return is 9.5%, what is the current stock price?"
    ),
    'options_list': ['do the math'],
    'correct_answer': 'USD 56.50',
    'explanation': (
        "This is a finite annuity:\n"
        "$$P_0 = 8.50 \\times PVIFA(9.5\\%,11) = 8.50 \\times 6.6471 = 56.50$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week22_q4 = {
    'question': (
        "Metallica Bearings Inc. will pay no dividends for 9 years. In year 10, it will pay USD 15.75 "
        "and dividends will grow at 4.8% thereafter. If the required return is 12%, what is the stock price today?"
    ),
    'options_list': ['do the math'],
    'correct_answer': 'USD 78.88',
    'explanation': (
        "Use the two-stage dividend model.\n"
        "First compute the price at year 9 using Gordon Growth:\n"
        "$$P_9 = \\frac{15.75}{0.12 - 0.048} = 218.75$$\n"
        "Discount that back to present:\n"
        "$$P_0 = \\frac{218.75}{(1.12)^9} = 78.88$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week23_q5 = {
    'question': (
        "Stoneworks Inc. has paid a dividend of USD 15 and will increase dividends by USD 3 annually for 5 years. "
        "Then it will pay nothing. If your required return is 11%, how much will you pay for a share today?"
    ),
    'options_list': ['do the math'],
    'correct_answer': 'USD 86.40',
    'explanation': (
        "This is a 5-year increasing cash flow problem:\n"
        "Dividends: 18, 21, 24, 27, 30\n"
        "$$P_0 = \\sum_{t=1}^5 \\frac{D_t}{(1.11)^t} = 86.40$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}


a_week2_q6 = {
    'question': (
        "Merriweather Company is expected to grow at a constant rate of 6%. The company paid a dividend of USD 1.20 last year. "
        "If the required rate of return is 14%, what is the current price of this stock?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '15.90',
    'explanation': (
        "Use the Gordon Growth Model:\n"
        "$$D_1 = 1.20 \\times (1 + 0.06) = 1.272$$\n"
        "$$P_0 = \\frac{D_1}{r - g} = \\frac{1.272}{0.14 - 0.06} = 15.90$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q7 = {
    'question': (
        "Caffe Vita Coffee Roasting Co. is considering replacing its old roasters with new ones. "
        "Old: purchased for USD 3.3M, current market value = USD 1.5M, 11-year life, gross profit = 600K/year, pre-tax income = 300K/year.\n"
        "New: cost = USD 4.5M, life = 10 years, gross margin = USD 1.2M/year, pre-tax income = 750K/year. "
        "Tax rate = 45%, cost of capital = 10%.\n"
        "What is the NPV of the replacement decision?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '-0.56',
    'explanation': (
        "With/without approach:\n"
        "- Incremental annual income = 750K - 300K = 450K taxable → net = 450K × (1 - 0.45) = 247.5K\n"
        "- Annual depreciation cash shield and savings included\n"
        "- Initial net investment = 4.5M - 1.5M = 3.0M\n"
        "- NPV = –0.56M → do not replace"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q8 = {
    'question': (
        "Based on the NPV of –0.56 million from the previous question, should Cafe Vita replace the roasters?"
    ),
    'options_list': ['do the math'],
    'correct_answer': 'No',
    'explanation': (
        "NPV of the replacement is negative (–0.56 million), so the project destroys value. "
        "Management should retain the existing equipment."
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q9 = {
    'question': (
        "Auger Biotech can spend USD 60M now on a promotional campaign. With it: cash flows = 700K/year for 5 years. "
        "Without it: cash flows = –18M/year. Discount rate = 10%.\n"
        "Is the campaign worthwhile? What is the NPV of the difference?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '10.89',
    'explanation': (
        "With/without cash flow delta = 700K - (–18M) = 18.7M/year for 5 years\n"
        "$$NPV = -60 + 18.7M \\times PVIFA(10\\%,5) = -60 + 18.7M \\times 3.791 = 10.89M$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q10 = {
    'question': (
        "McDonald's Chicken Purveyors is considering replacing an industrial fryer.\n"
        "New fryer: cost = USD 440K, life = 7 years, EBITDA = USD 100K/year, straight-line depreciation.\n"
        "Old fryer: market value = USD 269.5K, EBITDA = USD 49K/year, 7 years of depreciation remaining.\n"
        "Tax rate = 21%, discount rate = 12%.\n"
        "What is the NPV of the replacement?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '36717',
    'explanation': (
        "Incremental EBITDA = 100K – 49K = 51K\n"
        "Incremental depreciation = (440K – 308K)/7 = 18.86K\n"
        "Taxable income increase = 51K – 18.86K = 32.14K → tax = 6.75K\n"
        "Net cash flow = EBITDA – tax = 100K – 6.75K = 93.25K\n"
        "NPV = PV of incremental cash flows – (440K – 269.5K) ≈ 36,717 → replace the fryer"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q11 = {
    'question': (
        "O'Reilly Company has USD 1.5 million to invest and considers three independent projects:\n"
        "Alpha: –1,000,000 + [600K, 400K, 250K, 100K, 75K]\n"
        "Omega: –267,000 + [200K, 200K, 50K, 0, 0]\n"
        "Dogwood: –150,000 + [20K, 20K, 120K, 150K, 50K]\n"
        "What is the IRR of the combined cash flows from all three projects?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '24.73%',
    'explanation': (
        "Combine all project cash flows year by year, total investment = –1.417M.\n"
        "Use IRR function on the aggregated cash flows:\n"
        "Total CFs = [–1.417M, 820K, 620K, 420K, 250K, 125K]\n"
        "IRR = 24.73%"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q12 = {
    'question': (
        "Which of the following are valid firm valuation methods? Select all that apply."
    ),
    'options_list': ['do the math'],
    'correct_answer': 'Discounted Cash Flows (DCF), Comparables',
    'explanation': (
        "DCF and Comparables are legitimate valuation methods.\n"
        "- MVA is a performance metric, not a valuation method.\n"
        "- Retained earnings and market cap are balance sheet figures or market stats, not valuation models."
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q13 = {
    'question': (
        "Empty Space Industries is considering replacing a Sampson 1800 Lifter (original cost USD 650K, 6-year life, 1 year used, USD 475K market value)\n"
        "with a SuperMax 1000 (USD 730K, 5-year life, USD 30K salvage, EBITDA = USD 460K/year).\n"
        "Current machine EBITDA = USD 365K/year. Straight-line depreciation. Tax = 21%, discount rate = 14%.\n"
        "What is the NPV of the replacement decision?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '21103',
    'explanation': (
        "Incremental EBITDA = 95K/year. Incremental depreciation lowers taxable income.\n"
        "Tax-adjusted cash flow difference and initial net investment = 730K – 475K = 255K.\n"
        "NPV = 21,103 → buy the SuperMax."
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q14 = {
    'question': (
        "Adult Playtime Corp evaluates 5 mutually exclusive toy projects.\n"
        "Discount rate = 14%. Use NPV and IRR for decision-making.\n"
        "Cash flows (USD thousands) provided for each project over 5 years.\n"
        "Which project has the highest NPV?"
    ),
    'options_list': ['do the math'],
    'correct_answer': 'Interactive DVD',
    'explanation': (
        "NPV for each project computed at 14%:\n"
        "- 'Interactive DVD' has the highest NPV despite higher upfront cost.\n"
        "Management uses both NPV and IRR, but NPV dominates for absolute value creation."
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q15 = {
    'question': (
        "The next dividend payment by Barrelhouse Foods Inc. will be USD 2.85 per share. "
        "Dividends are expected to grow at 1.9% forever. If the stock sells for USD 42.75 per share, what is the required rate of return?"
    ),
    'options_list': ['7.84%', '8.14%', '8.57%', '9.12%'],
    'correct_answer': '8.57%',
    'explanation': (
        "Using the Gordon Growth Model:\n"
        "$$R = \\frac{D_1}{P_0} + g = \\frac{2.85}{42.75} + 0.019 = 0.0857 = 8.57\\%$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment INSPIRED GPT GENERATED'
}

a_week2_q16 = {
    'question': (
        "Zenith Textiles Ltd. will pay a dividend of USD 3.25 next year. "
        "Dividends are expected to grow at 4.5% annually. If the current stock price is USD 58.90, what is the required rate of return?"
    ),
    'options_list': ['9.65%', '9.84%', '10.02%', '10.21%'],
    'correct_answer': '10.02%',
    'explanation': (
        "$$R = \\frac{3.25}{58.90} + 0.045 = 0.1002 = 10.02\\%$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment INSPIRED GPT GENERATED'
}

a_week2_q17 = {
    'question': (
        "Juno Extracts Corp. will pay a fixed dividend of USD 9.75 per year for the next 12 years. "
        "If the required return is 10%, what is the stock’s value today?"
    ),
    'options_list': ['USD 62.75', 'USD 64.95', 'USD 66.43', 'USD 68.20'],
    'correct_answer': 'USD 66.43',
    'explanation': (
        "Finite annuity formula:\n"
        "$$P_0 = 9.75 \\times PVIFA(10\\%,12) = 9.75 \\times 6.811 = 66.43$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment INSPIRED GPT GENERATED'
}

a_week2_q18 = {
    'question': (
        "Atlas Mining Inc. will pay no dividends for 9 years. Starting in year 10, it will pay USD 13.40 "
        "and grow dividends at 6% forever. If the required return is 11%, what is the current price of the stock?"
    ),
    'options_list': ['USD 91.10', 'USD 97.25', 'USD 104.77', 'USD 113.50'],
    'correct_answer': 'USD 104.77',
    'explanation': (
        "First, calculate price at year 9 using Gordon Growth:\n"
        "$$P_9 = \\frac{13.40}{0.11 - 0.06} = 268.00$$\n"
        "Then discount back to present:\n"
        "$$P_0 = \\frac{268.00}{(1.11)^9} = 104.77$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment INSPIRED GPT GENERATED'
}

a_week2_q19 = {
    'question': (
        "Union Pipeworks Co. paid a dividend of USD 12 and will increase dividends by USD 2.50 annually for the next 5 years, "
        "after which it will cease all payouts. If your required return is 9%, what is the stock worth today?"
    ),
    'options_list': ['USD 70.55', 'USD 72.80', 'USD 74.18', 'USD 76.45'],
    'correct_answer': 'USD 74.18',
    'explanation': (
        "Dividends over 5 years: [14.5, 17.0, 19.5, 22.0, 24.5]\n"
        "$$P_0 = \\sum_{t=1}^5 \\frac{D_t}{(1.09)^t} = 74.18$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment INSPIRED GPT GENERATED'
}

a_week2_q2216 = {
    'question': (
        "Papyrus Logistics Inc. will pay a dividend of USD 2.85 next year. "
        "Dividends are expected to grow at 2.5% forever. If the stock sells for USD 41.00, "
        "what is the required rate of return?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '9.45%',
    'explanation': (
        "Using the Gordon Growth Model:\n"
        "$$R = \\frac{D_1}{P_0} + g = \\frac{2.85}{41.00} + 0.025 = 0.0945 \\Rightarrow 9.45\\%$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q11237 = {
    'question': (
        "Clover Medical Supplies will pay a constant dividend of USD 7.25 for the next 10 years, "
        "after which no dividends will be paid. If the required return is 8.7%, what is the current stock price?"
    ),
    'options_list': ['do the math'],
    'correct_answer': 'USD 47.15',
    'explanation': (
        "This is a finite annuity:\n"
        "$$P_0 = 7.25 \\times PVIFA(8.7\\%,10) = 7.25 \\times 6.5038 = 47.15$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_wee44k2_q18 = {
    'question': (
        "Quantum Sprockets Inc. will pay no dividends for 9 years. In year 10, it will pay USD 13.50, "
        "and dividends will grow at 5.2% thereafter. If the required return is 11%, what is the stock price today?"
    ),
    'options_list': ['do the math'],
    'correct_answer': 'USD 90.99',
    'explanation': (
        "Use the two-stage dividend model:\n"
        "$$P_9 = \\frac{13.50}{0.11 - 0.052} = 232.76$$\n"
        "Discount to present:\n"
        "$$P_0 = \\frac{232.76}{(1.11)^9} = 90.99$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_w12eek2_q19 = {
    'question': (
        "Flatiron Textiles Inc. pays a dividend of USD 16 and increases it by USD 3 per year for 5 years. "
        "Then it stops paying dividends. If the required return is 9.5%, how much is the stock worth today?"
    ),
    'options_list': ['do the math'],
    'correct_answer': 'USD 82.39',
    'explanation': (
        "Calculate each year's dividend and discount:\n"
        "Dividends: 19, 22, 25, 28, 31\n"
        "$$P_0 = \\sum_{t=1}^5 \\frac{D_t}{(1.095)^t} = 82.39$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_w22eek2_q20 = {
    'question': (
        "Delorean Dynamics is expected to grow at a constant rate of 5.5%. The company paid a dividend of USD 1.50 last year. "
        "If the required rate of return is 12.5%, what is the current price of this stock?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '22.61',
    'explanation': (
        "Use the Gordon Growth Model:\n"
        "$$D_1 = 1.50 \\times (1 + 0.055) = 1.5825$$\n"
        "$$P_0 = \\frac{D_1}{r - g} = \\frac{1.5825}{0.125 - 0.055} = 22.61$$"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_w11eek2_q21 = {
    'question': (
        "Holocron BioLabs can spend USD 72M now on a viral genomics campaign. "
        "With campaign: expected cash flows = 1.1M/year for 5 years. "
        "Without campaign: expected cash flows = –21M/year. "
        "If the discount rate is 9%, is the campaign worthwhile? What is the NPV of the difference?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '13.96',
    'explanation': (
        "With/without difference = 1.1M - (–21M) = 22.1M per year\n"
        "PVIFA(9%,5) = 3.88965\n"
        "$$NPV = -72 + 22.1 \\times 3.88965 = 13.96M$$ → campaign is worthwhile"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}

a_week2_q22 = {
    'question': (
        "BistroTech Foods is considering replacing its industrial fryer.\n"
        "New fryer: cost = USD 520,000, life = 7 years, EBITDA = USD 120,000/year, straight-line depreciation.\n"
        "Old fryer: market value = USD 295,000, EBITDA = USD 60,000/year, originally cost USD 330,000 (7 years of depreciation remaining).\n"
        "Tax rate = 22%, cost of capital = 11%.\n"
        "What is the NPV of the replacement decision?"
    ),
    'options_list': ['do the math'],
    'correct_answer': '23669.33',
    'explanation': (
        "Incremental EBITDA = 120K – 60K = 60K\n"
        "Incremental Depreciation = (520K – 330K)/7 = 27.14K\n"
        "Taxable income increase = 60K – 27.14K = 32.86K → tax = 7.23K\n"
        "Net annual cash flow = 120K – 7.23K = 112.77K\n"
        "Initial investment = 520K – 295K = 225K\n"
        "NPV = PV of annuity – investment ≈ 23669.33 → Replace the fryer"
    ),
    'chapter_information': 'Finance Module – Week 2 – Self Assessment'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M2W2_MPC = KC_MPC_QUESTIONS[:-1]
