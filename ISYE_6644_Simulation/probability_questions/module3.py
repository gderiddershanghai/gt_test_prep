module3_question1 = {
    'question': (
        "A refrigerator manufacturer subjects his finished products to a final inspection. Of interest are two categories of defects: scratches or flaws in the porcelain finish, and mechanical defects. "
        "The number of each type of defect is a random variable. The results of inspecting 50 refrigerators are shown in the following joint pmf table, where $X$ represents the occurrence of finish defects and $Y$ represents the occurrence of mechanical defects:\n\n"
        "| Y \\ X | 0  | 1  | 2  | 3  | 4  | 5  |\n"
        "|--------|----|----|----|----|----|----|\n"
        "| 0      | 11/50 | 4/50 | 2/50 | 1/50 | 1/50 | 1/50 |\n"
        "| 1      | 8/50  | 3/50 | 2/50 | 1/50 | 1/50 |     |\n"
        "| 2      | 4/50  | 3/50 | 2/50 | 1/50 |     |     |\n"
        "| 3      | 3/50  | 1/50 |      |      |     |     |\n"
        "| 4      | 1/50  |      |      |      |     |     |\n\n"
        "Find the marginal probability mass functions of $X$ and $Y$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The marginal pmf for $X$ is:\n"
        "$f_X(x) = \\{27/50, 11/50, 6/50, 3/50, 2/50, 1/50\\}$ for $x = 0, 1, 2, 3, 4, 5$\n\n"
        "The marginal pmf for $Y$ is:\n"
        "$f_Y(y) = \\{20/50, 15/50, 10/50, 4/50, 1/50\\}$ for $y = 0, 1, 2, 3, 4$."
    ),
    'explanation': (
        "To find the marginal pmf of $X$, sum over all values of $Y$ for each $X$. Similarly, to find the marginal pmf of $Y$, sum over all values of $X$ for each $Y$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question2 = {
    'question': (
        "Find the conditional pmf of mechanical defects $Y$, given that there are no finish defects ($X=0$)."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "$f_{Y|X=0}(y) = \\frac{f(0, y)}{f_X(0)} = \\left\\{\n"
        "\\begin{array}{ll}\n"
        "11/27 & \\text{if } y = 0 \\\\\n"
        "8/27 & \\text{if } y = 1 \\\\\n"
        "4/27 & \\text{if } y = 2 \\\\\n"
        "3/27 & \\text{if } y = 3 \\\\\n"
        "1/27 & \\text{if } y = 4 \\\\\n"
        "0 & \\text{otherwise.}\n"
        "\\end{array}\n"
        "\\right.$"
    ),
    'explanation': (
        "The conditional pmf is obtained by dividing the joint probability $f(0,y)$ by the marginal probability $f_X(0)$, which is $27/50$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question3 = {
    'question': (
        "Consider a situation in which the surface tension and acidity of a chemical product are measured. The variables are coded such that surface tension is measured on a scale $0 \\leq X \\leq 2$, and acidity is measured on a scale $2 \\leq Y \\leq 4$. The joint pdf of $(X, Y)$ is:\n\n"
        "$f(x, y) = \\left\\{ \\begin{array}{ll} c(6 - x - y) & \\text{if } 0 \\leq x \\leq 2, 2 \\leq y \\leq 4 \\\\\n"
        "0 & \\text{otherwise}. \\end{array} \\right.$\n\n"
        "(a) Find the appropriate value of $c$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "By integrating $f(x, y)$ over the given range and setting it equal to 1:\n\n"
        "$\\int_{2}^{4} \\int_{0}^{2} c(6 - x - y) \\ dx \\ dy = 1$.\n\n"
        "This gives $c = 1/8$."
    ),
    'explanation': (
        "The total probability must integrate to 1. Solving for $c$ involves evaluating the double integral of $c(6 - x - y)$ over the given region."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question4 = {
    'question': (
        "Consider the joint pdf $f(x, y) = c(6 - x - y)$ for $0 \\leq x \\leq 2$ and $2 \\leq y \\leq 4$. "
        "Calculate the probability that $X < 1$ and $Y < 3$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The probability is:\n\n"
        "$P(X < 1, Y < 3) = \\int_{2}^{3} \\int_{0}^{1} \\frac{1}{8} (6 - x - y) \\, dx \\, dy = \\frac{3}{8}$."
    ),
    'explanation': (
        "Integrate the given joint pdf $f(x, y)$ over the region $0 \\leq x < 1$ and $2 \\leq y < 3$ to compute the desired probability."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question5 = {
    'question': (
        "For the joint pdf $f(x, y) = c(6 - x - y)$, calculate the probability that $X + Y \\leq 4$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The probability is:\n\n"
        "$P(X + Y \\leq 4) = \\int_{2}^{4} \\int_{0}^{4 - y} \\frac{1}{8} (6 - x - y) \\, dx \\, dy = \\frac{2}{3}$."
    ),
    'explanation': (
        "To find $P(X + Y \\leq 4)$, integrate the joint pdf over the appropriate triangular region defined by $0 \\leq x \\leq 2$, $2 \\leq y \\leq 4$, and $x + y \\leq 4$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question6 = {
    'question': (
        "Find the marginal pdf of $X$ for the joint pdf $f(x, y) = c(6 - x - y)$ where $0 \\leq x \\leq 2$ and $2 \\leq y \\leq 4$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The marginal pdf of $X$ is:\n\n"
        "$f_X(x) = \\int_{2}^{4} \\frac{1}{8} (6 - x - y) \\, dy = \\frac{3 - x}{4}, \\ 0 < x < 2$."
    ),
    'explanation': (
        "To find the marginal pdf $f_X(x)$, integrate the joint pdf $f(x, y)$ over $y$ in the range $[2, 4]$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question7 = {
    'question': (
        "Given the joint pdf $f(x, y) = cxy^2$ for $0 < x < y^2 < 1$, find the constant $c$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The constant $c$ is:\n\n"
        "$1 = \\int_{0}^{1} \\int_{0}^{y^2} cxy^2 \\, dx \\, dy \\implies c = 14$."
    ),
    'explanation': (
        "To determine $c$, integrate $f(x, y)$ over the given range $0 < x < y^2$ and $0 < y < 1$, and set the integral equal to 1."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question8 = {
    'question': (
        "For the joint pdf $f(x, y) = 14xy^2$ where $0 < x < y^2 < 1$, find the marginal pdf of $Y$, $f_Y(y)$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The marginal pdf of $Y$ is:\n\n"
        "$f_Y(y) = \\int_{0}^{y^2} 14xy^2 \\, dx = 7y^6, \\ 0 < y < 1$."
    ),
    'explanation': (
        "To find $f_Y(y)$, integrate the joint pdf $f(x, y)$ with respect to $x$ over the range $0 < x < y^2$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question9 = {
    'question': (
        "Given the joint pdf $f(x, y) = 14xy^2$ for $0 < x < y^2 < 1$, find the conditional pdf of $X$ given $Y = y$, $f(x|y)$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The conditional pdf is:\n\n"
        "$f(x|y) = \\frac{f(x, y)}{f_Y(y)} = \\frac{2x}{y^4}, \\ 0 < x < y^2 < 1$."
    ),
    'explanation': (
        "The conditional pdf $f(x|y)$ is obtained by dividing the joint pdf $f(x, y)$ by the marginal pdf $f_Y(y)$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question10 = {
    'question': (
        "Given the joint pdf $g(x, y) = 4xye^{-(x^2 + y^2)}$, determine whether $X$ and $Y$ are independent."
    ),
    'options_list': ['Independent', 'Not Independent'],
    'correct_answer': "Independent",
    'explanation': (
        "The joint pdf $g(x, y) = 4xye^{-(x^2 + y^2)}$ can be factored as $g(x, y) = (4xe^{-x^2})(ye^{-y^2})$, "
        "showing that $X$ and $Y$ are independent."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

joint_pdf_exercise = {
    'question': (
        "Suppose that $f(x, y) = 6x$, for $0 \\leq x \\leq y \\leq 1$.\n\n"
        "(a) Find $P(X < 1/2 \\text{ and } Y < 1/2)$.\n"
        "(b) Find the marginal pdf $f_X(x)$ of $X$."
    ),
    'options_list': ["Compute"],
    'correct_answer': (
        "(a) $P(X < 1/2 \\text{ and } Y < 1/2) = \\int_0^{1/2} \\int_0^y 6x \\, dx \\, dy = \\int_0^{1/2} 3y^2 \\, dy = 1/8$\n"
        "(b) $f_X(x) = \\int_x^1 6x \\, dy = 6x(1 - x), \\quad 0 \\leq x \\leq 1$."
    ),
    'explanation': (
        "(a) The probability is computed as a double integral over the region $0 \\leq x < 1/2$ and $0 \\leq y < 1/2$. "
        "Evaluating $\\int_0^{1/2} \\int_0^y 6x \\, dx \\, dy$, the integral simplifies to $\\int_0^{1/2} 3y^2 \\, dy = 1/8$.\n\n"
        "(b) The marginal pdf of $X$ is obtained by integrating $f(x, y)$ over $y$, giving $f_X(x) = \\int_x^1 6x \\, dy = 6x(1 - x)$ for $0 \\leq x \\leq 1$."
    ),
    'chapter_information': "Goldsman Probability Book Part 2.9 (§3.1)"
}

joint_pmf_table_exercise = {
    'question': (
        "Suppose $X$ and $Y$ are discrete random variables with the following joint pmf, where any letters denote probabilities "
        "that you’ll need to figure out:\n\n"
        "\\["
        "\\begin{array}{|c|c|c|c|c|}"
        "\\hline"
        "f(x, y) & X = -3 & X = 0 & X = 5 & P(Y = y) \\\\"
        "\\hline"
        "Y = 8 & 0.2 & a & b & 0.3 \\\\"
        "Y = 27 & c & 0.3 & 0.3 & d \\\\"
        "P(X = x) & e & 0.3 & g & h \\\\"
        "\\hline"
        "\\end{array}"
        "\\]\n\n"
        "(a) Complete the table with the correct values for the letters.\n"
        "(b) Find $P(X \\leq 1)$.\n"
        "(c) Find $P(X = 5 | Y = 27)$."
    ),
    'options_list': ["Calculate"],
    'correct_answer': (
        "(a) The completed table is:\n\n"
        "\\["
        "\\begin{array}{|c|c|c|c|c|}"
        "\\hline"
        "f(x, y) & X = -3 & X = 0 & X = 5 & P(Y = y) \\\\"
        "\\hline"
        "Y = 8 & 0.2 & 0.0 & 0.1 & 0.3 \\\\"
        "Y = 27 & 0.1 & 0.3 & 0.3 & 0.7 \\\\"
        "P(X = x) & 0.3 & 0.3 & 0.4 & 1 \\\\"
        "\\hline"
        "\\end{array}"
        "\\]\n\n"
        "(b) $P(X \\leq 1) = P(X = -3) + P(X = 0) = 0.3 + 0.3 = 0.6$.\n\n"
        "(c) $P(X = 5 | Y = 27) = \\frac{f(5, 27)}{f_Y(27)} = \\frac{0.3}{0.7} = \\frac{3}{7}$."
    ),
    'explanation': (
        "(a) The table is completed using the constraints that the rows and columns must sum to the respective marginal probabilities.\n\n"
        "(b) The probability $P(X \\leq 1)$ is found by summing $P(X = -3)$ and $P(X = 0)$ directly from the table.\n\n"
        "(c) The conditional probability $P(X = 5 | Y = 27)$ is calculated using the formula "
        "$P(X = 5 | Y = 27) = \\frac{f(5, 27)}{f_Y(27)}$, where $f_Y(27)$ is the marginal probability of $Y = 27$."
    ),
    'chapter_information': "Goldsman Probability Book Part 2.9 (§3.8)"
}

joint_pdf_properties = {
    'question': (
        "Suppose that $f(x, y) = cxy^2$, for $0 \\leq x \\leq y^2 \\leq 1$ and $0 \\leq y \\leq 1$.\n\n"
        "(a) Find $c$.\n"
        "(b) Find the marginal pdf of $X$, $f_X(x)$.\n"
        "(c) Find the marginal pdf of $Y$, $f_Y(y)$.\n"
        "(d) Find $E[X]$.\n"
        "(e) Find $E[Y]$.\n"
        "(f) Find the conditional pdf of $X$, given $Y = y$, i.e., $f(x|y)$."
    ),
    'options_list': ["Calculate"],
    'correct_answer': (
        "(a) The value of $c$ is found by integrating $f(x, y)$ over its domain:\n\n"
        "\\[\n"
        "1 = \\int_{0}^{1} \\int_{0}^{y^2} cxy^2 \\ dx \\ dy = \\int_{0}^{1} \\frac{cy^5}{2} \\ dy = \\frac{c}{14}.\n"
        "\\]\n"
        "This implies that $c = 14$.\n\n"
        "(b) The marginal pdf of $X$ is:\n\n"
        "\\[\n"
        "f_X(x) = \\int_{\\sqrt{x}}^{1} 14xy^2 \\ dy = \\frac{14}{3}(x - x^{5/2}), \\quad 0 \\leq x \\leq 1.\n"
        "\\]\n\n"
        "(c) The marginal pdf of $Y$ is:\n\n"
        "\\[\n"
        "f_Y(y) = \\int_{0}^{y^2} 14xy^2 \\ dx = 7y^6, \\quad 0 \\leq y \\leq 1.\n"
        "\\]\n\n"
        "(d) The expected value $E[X]$ is:\n\n"
        "\\[\n"
        "E[X] = \\int_{0}^{1} x f_X(x) \\ dx = \\int_{0}^{1} \\frac{14}{3}x(x - x^{5/2}) \\ dx = \\frac{14}{27}.\n"
        "\\]\n\n"
        "(e) The expected value $E[Y]$ is:\n\n"
        "\\[\n"
        "E[Y] = \\int_{0}^{1} y f_Y(y) \\ dy = \\int_{0}^{1} 7y^7 \\ dy = \\frac{7}{8}.\n"
        "\\]\n\n"
        "(f) The conditional pdf of $X$ given $Y = y$ is:\n\n"
        "\\[\n"
        "f(x|y) = \\frac{f(x, y)}{f_Y(y)} = \\frac{2x}{y^4}, \\quad 0 \\leq x \\leq y^2 \\leq 1.\n"
        "\\]"
    ),
    'explanation': (
        "Each part involves standard integration techniques to compute the marginal distributions, expectations, and conditional density:\n\n"
        "- For (a), integrate $f(x, y)$ over its domain and set the result to 1 to solve for $c$.\n"
        "- For (b) and (c), marginalize by integrating over $y$ or $x$ respectively.\n"
        "- For (d) and (e), use the definitions of expected value with the marginal pdfs.\n"
        "- For (f), compute the ratio of $f(x, y)$ to $f_Y(y)$."
    ),
    'chapter_information': "Goldsman Probability Book Part 2.9 (§3.2)"
}

joint_pmf_social_media = {
    'question': (
        "The following table gives the joint pmf \\( f(x, y) \\) of two random variables: \\( X \\) (the GPA of a university student), "
        "and \\( Y \\) (the average hours a week the student spends on social media):\n\n"
        "\\[\n"
        "\\begin{array}{|c|c|c|c|}\n"
        "\\hline\n"
        "f(x, y) & X = 2 & X = 3 & X = 4 \\\\\n"
        "\\hline\n"
        "Y = 40 & 0.4 & 0.1 & 0.1 \\\\\n"
        "Y = 50 & 0.1 & 0.2 & 0.1 \\\\\n"
        "\\hline\n"
        "\\end{array}\n"
        "\\]\n\n"
        "(a) What’s the probability that a random student spends 50 hours on social media?\n"
        "(b) What’s the conditional probability that a random student spends 50 hours a week on social media given that their GPA is 2?"
    ),
    'options_list': ["Calculate"],
    'correct_answer': (
        "(a) To find \\( P(Y = 50) \\), we sum over all \\( X \\) values in the table:\n\n"
        "\\[\n"
        "f_Y(50) = \\sum_x f(x, 50) = 0.1 + 0.2 + 0.1 = 0.4.\n"
        "\\]\n\n"
        "(b) To find \\( P(Y = 50 \\mid X = 2) \\), we use the conditional probability formula:\n\n"
        "\\[\n"
        "P(Y = 50 \\mid X = 2) = \\frac{f(2, 50)}{f_X(2)} = \\frac{0.1}{0.5} = 0.2.\n"
        "\\]\n"
    ),
    'explanation': (
        "(a) The marginal probability \\( f_Y(50) \\) is obtained by summing all joint probabilities where \\( Y = 50 \\):\n\n"
        "- From the table: \\( 0.1 + 0.2 + 0.1 = 0.4 \\).\n\n"
        "(b) The conditional probability is computed using the formula \\( P(Y \\mid X) = \\frac{f(X, Y)}{f_X(X)} \\):\n\n"
        "- From the table, \\( f(2, 50) = 0.1 \\) and \\( f_X(2) = 0.5 \\).\n\n"
        "- Hence, \\( P(Y = 50 \\mid X = 2) = \\frac{0.1}{0.5} = 0.2 \\)."
    ),
    'chapter_information': "Goldsman Probability Book Part 2.9 (§3.2)"
}

independence_check_joint_pmf = {
    'question': (
        "Consider the random variables \\( X \\) and \\( Y \\) having the following joint pmf:\n\n"
        "\\[\n"
        "\\begin{array}{|c|c|c|c|}\n"
        "\\hline\n"
        "f(x, y) & X = 2 & X = 3 & X = 4 \\\\\n"
        "\\hline\n"
        "Y = 40 & 0.4 & 0.1 & 0.1 \\\\\n"
        "Y = 50 & 0.1 & 0.2 & 0.1 \\\\\n"
        "\\hline\n"
        "\\end{array}\n"
        "\\]\n\n"
        "The marginals are filled as follows:\n\n"
        "\\[\n"
        "\\begin{array}{|c|c|c|c|c|}\n"
        "\\hline\n"
        "f(x, y) & X = 2 & X = 3 & X = 4 & f_Y(y) \\\\\n"
        "\\hline\n"
        "Y = 40 & 0.4 & 0.1 & 0.1 & 0.6 \\\\\n"
        "Y = 50 & 0.1 & 0.2 & 0.1 & 0.4 \\\\\n"
        "\\hline\n"
        "f_X(x) & 0.5 & 0.3 & 0.2 & 1 \\\\\n"
        "\\hline\n"
        "\\end{array}\n"
        "\\]\n\n"
        "Are \\( X \\) and \\( Y \\) independent?"
    ),
    'options_list': ["Yes", "No"],
    'correct_answer': "No",
    'explanation': (
        "To check for independence, we test if \\( f(x, y) = f_X(x)f_Y(y) \\) for all \\( x, y \\):\n\n"
        "- For \\( f(2, 40) = 0.4 \\), we compute \\( f_X(2)f_Y(40) = (0.5)(0.6) = 0.3 \\).\n"
        "- Since \\( f(2, 40) \\neq f_X(2)f_Y(40) \\), \\( X \\) and \\( Y \\) are not independent.\n\n"
        "Thus, \\( X \\) and \\( Y \\) are dependent."
    ),
    'chapter_information': "Goldsman Probability Book Part 2.9 (§3.3)"
}

exponential_lifetimes_comparison = {
    'question': (
        "We have two brands of lightbulbs. Brand \\( X \\) has an \\( \\text{Exp}(\\mu = 1) \\) lifetime with a mean of 1 year. "
        "Brand \\( Y \\) has an \\( \\text{Exp}(\\lambda = 1/2) \\) lifetime with a mean of 2 years. "
        "Assuming that \\( X \\) and \\( Y \\) are independent, what's the probability that \\( X \\) lasts longer than \\( Y \\)?"
    ),
    'options_list': [
        "1/2", 
        "1/3", 
        "2/3", 
        "1/4"
    ],
    'correct_answer': "1/3",
    'explanation': (
        "**Short Explanation:**\n"
        "The result directly follows from a known property of exponential distributions:\n"
        "\\[\n"
        "P(Y < X) = \\frac{\\lambda}{\\lambda + \\mu} = \\frac{1/2}{1/2 + 1} = \\frac{1}{3}.\n"
        "\\]\n\n"
        "**Long Explanation:**\n"
        "**Step 1: Understand the problem setup**\n"
        "The lifetime of Brand \\( X \\), \\( T_X \\), is exponentially distributed:\n"
        "\\[\n"
        "f_X(x) = e^{-x}, \\quad x \\geq 0, \\mu = 1.\n"
        "\\]\n"
        "The mean is 1 year, so \\( \\mu = 1 \\).\n\n"
        "The lifetime of Brand \\( Y \\), \\( T_Y \\), is exponentially distributed:\n"
        "\\[\n"
        "f_Y(y) = \\frac{1}{2} e^{-y/2}, \\quad y \\geq 0, \\lambda = 1/2.\n"
        "\\]\n"
        "The mean is 2 years, so \\( \\lambda = 1/2 \\).\n\n"
        "Since \\( T_X \\) and \\( T_Y \\) are independent, the joint PDF is:\n"
        "\\[\n"
        "f_{X,Y}(x, y) = f_X(x) \\cdot f_Y(y) = e^{-x} \\cdot \\frac{1}{2} e^{-y/2}, \\quad x \\geq 0, y \\geq 0.\n"
        "\\]\n"
        "We want to compute \\( P(X > Y) \\).\n\n"
        "**Step 2: Express \\( P(X > Y) \\) as an integral**\n"
        "The event \\( X > Y \\) corresponds to the region \\( x > y \\). Mathematically:\n"
        "\\[\n"
        "P(X > Y) = \\int_0^\\infty \\int_y^\\infty f_{X,Y}(x, y) \\, dx \\, dy.\n"
        "\\]\n\n"
        "**Step 3: Substitute the joint PDF**\n"
        "Substitute \\( f_{X,Y}(x, y) = e^{-x} \\cdot \\frac{1}{2} e^{-y/2} \\):\n"
        "\\[\n"
        "P(X > Y) = \\int_0^\\infty \\int_y^\\infty e^{-x} \\cdot \\frac{1}{2} e^{-y/2} \\, dx \\, dy.\n"
        "\\]\n\n"
        "**Step 4: Evaluate the inner integral**\n"
        "The inner integral is with respect to \\( x \\), over \\( x \\in [y, \\infty) \\):\n"
        "\\[\n"
        "\\int_y^\\infty e^{-x} \\, dx = \\big[ -e^{-x} \\big]_y^\\infty = e^{-y}.\n"
        "\\]\n"
        "So the integral becomes:\n"
        "\\[\n"
        "P(X > Y) = \\int_0^\\infty e^{-y} \\cdot \\frac{1}{2} e^{-y/2} \\, dy.\n"
        "\\]\n\n"
        "**Step 5: Simplify the integral**\n"
        "Combine the exponential terms:\n"
        "\\[\n"
        "e^{-y} \\cdot e^{-y/2} = e^{-3y/2}.\n"
        "\\]\n"
        "The integral is now:\n"
        "\\[\n"
        "P(X > Y) = \\frac{1}{2} \\int_0^\\infty e^{-3y/2} \\, dy.\n"
        "\\]\n\n"
        "**Step 6: Evaluate the remaining integral**\n"
        "The integral of \\( e^{-ay} \\) is:\n"
        "\\[\n"
        "\\int_0^\\infty e^{-ay} \\, dy = \\frac{1}{a}, \\quad a > 0.\n"
        "\\]\n"
        "Here, \\( a = \\frac{3}{2} \\), so:\n"
        "\\[\n"
        "\\int_0^\\infty e^{-3y/2} \\, dy = \\frac{1}{3/2} = \\frac{2}{3}.\n"
        "\\]\n"
        "Thus:\n"
        "\\[\n"
        "P(X > Y) = \\frac{1}{2} \\cdot \\frac{2}{3} = \\frac{1}{3}.\n"
        "\\]\n\n"
        "**Final Answer:**\n"
        "The probability that \\( X \\) lasts longer than \\( Y \\) is \\( P(X > Y) = \\frac{1}{3} \\)."
    ),
    'chapter_information': "Goldsman Probability Book Part 2.9 (§3.3)"
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

MODULE_3_MPC = KC_MPC_QUESTIONS[:-1]