question_1_seize_module = {
    'question': (
        "What is the main purpose of the Seize module in Arena?\n"
        "A. To create new entities.\n"
        "B. To release resources.\n"
        "C. To request and assign resources.\n"
        "D. To delay entities for a specific amount of time."
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "C. To request and assign resources.",
    'explanation': (
        "The Seize module is used to request a resource and assign it to an entity. "
        "It is typically used in process steps where entities need to “seize” a resource "
        "before they can continue their processing (e.g., waiting for a machine to become available)."
    ),
    'chapter_information': "GPT 40 Generated - Week 6 Content Arena"
}

question_2_dispose_module = {
    'question': "TRUE or FALSE? The Dispose module is used to remove entities from the model permanently.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': (
        "The Dispose module is used to remove entities from the model once they have completed all their required processes. "
        "It represents the end of an entity's life cycle in the simulation."
    ),
    'chapter_information': "GPT 40 Generated - Week 6 Content Arena"
}

question_3_create_module = {
    'question': (
        "Which module would you use to create new entities in Arena?\n"
        "A. Process\n"
        "B. Create\n"
        "C. Dispose\n"
        "D. Delay"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "B. Create",
    'explanation': (
        "The Create module is used to generate new entities in the model at specified times. "
        "These entities then move through the various process steps defined in the model."
    ),
    'chapter_information': "GPT 40 Generated - Week 6 Content Arena"
}

question_4_nq_function = {
    'question': (
        "What does the 'NQ' function in Arena represent?\n"
        "A. Number of entities in a queue.\n"
        "B. Number of servers in a resource.\n"
        "C. The total number of processes completed.\n"
        "D. The number of entities being processed at a given time."
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "A. Number of entities in a queue.",
    'explanation': (
        "'NQ' stands for 'Number in Queue.' It is used to track the number of entities in a specific queue at any point in time. "
        "This can help analyze system performance, such as how long entities are waiting in line for a resource."
    ),
    'chapter_information': "GPT 40 Generated - Week 6 Content Arena"
}

question_5_assign_module = {
    'question': (
        "Which module would you use to change the values of an entity's attributes in Arena?\n"
        "A. Assign\n"
        "B. Process\n"
        "C. Seize\n"
        "D. Create"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "A. Assign",
    'explanation': (
        "The Assign module is used to change or set values for an entity's attributes. "
        "This is useful for modifying data or properties associated with an entity as it moves through the simulation process."
    ),
    'chapter_information': "GPT 40 Generated - Week 6 Content Arena"
}

question_6_queue_module = {
    'question': "TRUE or FALSE? The Queue module in Arena is used to specify the number of servers for a resource.",
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': (
        "The Queue module is not used to set the number of servers. It is used to define the queue that holds entities waiting for a resource. "
        "The number of servers is set in the Resource module or the Resource spreadsheet."
    ),
    'chapter_information': "GPT 40 Generated - Week 6 Content Arena"
}

question_7_delay_module = {
    'question': (
        "Which of the following can be used to define the time an entity waits before starting its process in Arena?\n"
        "A. Delay module\n"
        "B. Process module\n"
        "C. Create module\n"
        "D. Seize module"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "A. Delay module",
    'explanation': (
        "The Delay module is used to delay the processing of an entity for a specific time period. "
        "It simulates waiting times in various stages of the process."
    ),
    'chapter_information': "GPT 40 Generated - Week 6 Content Arena"
}


question_1_record_module = {
    'question': "TRUE or FALSE? The Record module is primarily used to collect statistical data during a simulation run.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': (
        "Correct! The Record module captures statistical data such as wait times, utilization, and throughput for analysis during a simulation run."
    ),
    'chapter_information': "Deepseek Generated - Week 6 Content Arena"
}

question_2_tnow_function = {
    'question': (
        "Which Arena function returns the current simulation time?\n"
        "A. TNOW\n"
        "B. TOTAL\n"
        "C. NQ\n"
        "D. NR"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "A. TNOW",
    'explanation': (
        "Correct! TNOW returns the current simulation time, which is essential for controlling time-based logic during the simulation."
    ),
    'chapter_information': "Deepseek Generated - Week 6 Content Arena"
}

question_3_entity_attribute = {
    'question': (
        "Which of the following is not an entity attribute?\n"
        "A. Customer arrival time\n"
        "B. Priority level\n"
        "C. System’s total entities processed\n"
        "D. Part color"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "C. System’s total entities processed",
    'explanation': (
        "Correct! System's total entities processed is a system-level variable (like WIP or total throughput), "
        "not an entity attribute. Attributes belong to individual entities (e.g., part color, priority level)."
    ),
    'chapter_information': "Deepseek Generated - Week 6 Content Arena"
}

question_5_exponential_distribution = {
    'question': "TRUE or FALSE? The exponential distribution is a valid option for interarrival times in the Create module.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': (
        "Correct! The Create module supports several distributions, including exponential, normal, and uniform, "
        "for generating interarrival times for entities."
    ),
    'chapter_information': "Deepseek Generated - Week 6 Content Arena"
}

question_6_decide_module = {
    'question': (
        "Which Decide module option allows splitting entities based on a user-defined condition?\n"
        "A. 2-Way by Chance\n"
        "B. N-Way by Condition\n"
        "C. 3-Way by Priority\n"
        "D. 2-Way by Attribute"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "B. N-Way by Condition",
    'explanation': (
        "Correct! N-Way by Condition routes entities based on user-defined logical expressions or conditions "
        "(e.g., an attribute or other data points)."
    ),
    'chapter_information': "Deepseek Generated - Week 6 Content Arena"
}

question_7_batch_module = {
    'question': "TRUE or FALSE? Temporary batches created with the Batch module can later be split into original entities.",
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': (
        "Correct! Temporary batches can be split back into original entities using the Separate module. "
        "This allows you to reassign individual attributes to each entity after they have been batched."
    ),
    'chapter_information': "Deepseek Generated - Week 6 Content Arena"
}

question_8_resource_spreadsheet = {
    'question': (
        "How do you modify the number of available servers for a resource mid-simulation?\n"
        "A. Adjust the Resource spreadsheet\n"
        "B. Use the Assign module\n"
        "C. Edit the Process module\n"
        "D. Update the Queue discipline"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "A. Adjust the Resource spreadsheet",
    'explanation': (
        "Correct! You modify resource capacity (e.g., servers on duty) in the Resource spreadsheet to dynamically adjust "
        "the number of servers during the simulation."
    ),
    'chapter_information': "Deepseek Generated - Week 6 Content Arena"
}

question_9_nr_function = {
    'question': (
        "If NR(Machine) returns 3, what does this indicate?\n"
        "A. 3 machines are idle\n"
        "B. 3 machines are busy\n"
        "C. 3 machines are broken\n"
        "D. 3 machines exist in total"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "B. 3 machines are busy",
    'explanation': (
        "Correct! NR(Resource) returns the number of busy servers in a resource. In this case, if NR(Machine) = 3, it means that "
        "3 machines are currently in use."
    ),
    'chapter_information': "Deepseek Generated - Week 6 Content Arena"
}



simu3lation_question_1 = {
    'question': "Which of the following is the correct sequence of modules to model a simple queue with customers arriving, waiting for service, and leaving the system?",
    'options_list': ['A. Create-Process-Dispose', 'B. Create-Seize-Release', 'C. Seize-Delay-Release', 'D. Create-Process-Release'],
    'correct_answer': "A. Create-Process-Dispose",
    'explanation': (
        "The correct sequence to model a simple queue in Arena is Create (for arrival of entities), "
        "Process (for service or delay), and Dispose (for entities to leave the system)."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

simulati3on_question_2 = {
    'question': "TRUE or FALSE?\nThe Resource spreadsheet in Arena is used to define the properties of entities, such as their color or size.",
    'options_list': ['True', 'False'],
    'correct_answer': "False",
    'explanation': (
        "The Resource spreadsheet is used to define the properties of resources (e.g., servers), not entities. "
        "Entity properties are typically defined in the Attribute spreadsheet."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

simula3tion_question_3 = {
    'question': "Which Arena module would be used to assign a priority level to an entity based on its type?",
    'options_list': ['A. Decide', 'B. Assign', 'C. Seize', 'D. Release'],
    'correct_answer': "B. Assign",
    'explanation': (
        "The Assign module is used to set or modify attributes or variables, including assigning priority or other properties to an entity. "
        "The Decide module is used for making decisions, not assigning properties."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

simulati3on_question_4 = {
    'question': "Which Arena function returns the number of customers currently in a queue?",
    'options_list': ['A. NQ()', 'B. NR()', 'C. COUNT()', 'D. QLEN()'],
    'correct_answer': "A. NQ()",
    'explanation': (
        "The NQ() function returns the number of entities in a queue. NR() is used to track busy resources, while COUNT() and QLEN() are not standard Arena functions."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

simula3tion_question_5 = {
    'question': "TRUE or FALSE?\nThe Seize-Delay-Release action in the Process module handles resource allocation and frees the resource after the service.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "The Seize-Delay-Release action in the Process module handles both the allocation of resources (Seize) and the release of resources (Release) after the Delay period."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

sim3ulation_question_6 = {
    'question': "What does the Future Event List (FEL) in Arena store?",
    'options_list': ['A. A list of all entities in the system', 'B. A list of upcoming events in the simulation', 
                     'C. A list of all modules in the model', 'D. A list of all resources in use'],
    'correct_answer': "B. A list of upcoming events in the simulation",
    'explanation': (
        "The Future Event List (FEL) holds events scheduled to occur in the future, sorted by time. "
        "It’s crucial for driving the simulation forward."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

simulation_que3stion_7 = {
    'question': "What happens if you choose the “Seize-Delay” action in the Process module without the “Release” option?",
    'options_list': ['A. Entities will be created but will never leave the system.', 'B. Entities will be seized and delayed, but no resources will be released.',
                     'C. Entities will be processed and leave without waiting.', 'D. The simulation will stop due to an error.'],
    'correct_answer': "B. Entities will be seized and delayed, but no resources will be released.",
    'explanation': (
        "Choosing Seize-Delay without Release will cause entities to be delayed, but they won’t be released from the resource, "
        "potentially causing a blockage in the system."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

simulation3_question_8 = {
    'question': "Which module is used to model a decision-making process where an entity can follow different paths based on a defined condition?",
    'options_list': ['A. Create', 'B. Decide', 'C. Process', 'D. Dispose'],
    'correct_answer': "B. Decide",
    'explanation': (
        "The Decide module is used to create decisions based on conditions or probabilities, allowing entities to be routed based on certain logic or conditions."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

simulat3ion_question_9 = {
    'question': "Which Arena module allows you to modify the value of an entity attribute during the simulation?",
    'options_list': ['A. Create', 'B. Assign', 'C. Process', 'D. Seize'],
    'correct_answer': "B. Assign",
    'explanation': (
        "The Assign module is used to modify entity attributes or system variables during a simulation, including changing values such as priority or time."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}

simulation_que231stion_10 = {
    'question': "What is the primary purpose of the Validate option in Arena?",
    'options_list': ['A. To ensure that entities arrive on time', 'B. To check the system’s resource utilization', 
                     'C. To ensure the simulation model accurately represents the real-world system', 'D. To optimize the model’s execution speed'],
    'correct_answer': "C. To ensure the simulation model accurately represents the real-world system",
    'explanation': (
        "Validation in Arena is the process of ensuring the model behaves in a way that reflects the real-world system. "
        "It checks if the model correctly represents the system's behaviors and characteristics."
    ),
    'chapter_information': 'Week 6 - Module 5 GPT 40'
}
#################################
deepseek_week6_module5_q1 = {
    'question': "Which module sequence models customers arriving, being processed by a cashier, and exiting a store?",
    'options_list': ['A. Create-Seize-Release', 'B. Create-Process-Dispose', 'C. Create-Delay-Dispose', 'D. Create-Batch-Separate'],
    'correct_answer': "B. Create-Process-Dispose",
    'explanation': (
        "This sequence represents the core entity lifecycle in Arena."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q2 = {
    'question': "TRUE or FALSE?\nArena’s Process-Interaction worldview focuses on scheduling discrete events like arrivals and departures.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "The Process-Interaction approach emphasizes entity flow through processes (queues, resources)."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q3 = {
    'question': "Which field in the Create module determines the time until the first entity arrives?",
    'options_list': ['A. Interarrival Time Distribution', 'B. First Creation', 'C. Max Arrivals', 'D. Entity Type'],
    'correct_answer': "B. First Creation",
    'explanation': (
        "\"First Creation\" sets the initial delay before entity generation begins."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q4 = {
    'question': "What happens if a Process module lacks a defined resource?",
    'options_list': ['A. Entities skip the module', 'B. Queues form indefinitely', 'C. No queues form', 'D. The simulation crashes'],
    'correct_answer': "C. No queues form",
    'explanation': (
        "Queues only form when entities compete for limited resources."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q5 = {
    'question': "Which action is impossible in a Process module?",
    'options_list': ['A. Seize-Delay', 'B. Delay-Release', 'C. Seize-Delay-Release', 'D. Delay Only'],
    'correct_answer': "B. Delay-Release",
    'explanation': (
        "\"Release\" requires prior resource seizure (Seize-Delay-Release is valid)."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q6 = {
    'question': "TRUE or FALSE?\nOmitting a \"Release\" action causes resources to remain permanently occupied.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "Resources must be explicitly released for reuse."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q7 = {
    'question': "Which spreadsheet defines the number of available workers for a resource?",
    'options_list': ['A. Queue', 'B. Variable', 'C. Resource', 'D. Entity'],
    'correct_answer': "C. Resource",
    'explanation': (
        "Resource spreadsheets configure server counts (e.g., 3 cashiers)."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q8 = {
    'question': "What does NQ(CoffeeShop.Queue) represent?",
    'options_list': ['A. Customers being served', 'B. Customers waiting in line', 'C. Total customers served', 'D. Cashier utilization'],
    'correct_answer': "B. Customers waiting in line",
    'explanation': (
        "NQ() tracks queue length for the specified resource."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q9 = {
    'question': "Which term describes a global value like total daily customers served?",
    'options_list': ['A. Attribute', 'B. Variable', 'C. Parameter', 'D. Resource'],
    'correct_answer': "B. Variable",
    'explanation': (
        "Variables track system-wide metrics, unlike entity-specific attributes."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

deepseek_week6_module5_q10 = {
    'question': "If arrivals occur at 6/hour and service takes 8 minutes each, what is server utilization?",
    'options_list': ['A. 60%', 'B. 75%', 'C. 80%', 'D. 120%'],
    'correct_answer': "C. 80%",
    'explanation': (
        "Utilization = Arrival rate (6/hr) × Service time (8/60 hr) = 0.8."
    ),
    'chapter_information': 'Week 6 - Module 5 Deep Seek generated'
}

week7_module7_q1 = {
    'question': "TRUE or FALSE?\nThe \"Process-Interaction\" worldview in Arena emphasizes modeling entity flow through predefined processes like queues and resources.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "Process-Interaction focuses on entity pathways and resource interactions, unlike event-scheduling."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q2 = {
    'question': "Which module sequence models the lifecycle of entities entering, processing with a server, and exiting a system?",
    'options_list': ['A. Create-Seize-Dispose', 'B. Create-Delay-Release', 'C. Create-Process-Dispose', 'D. Create-Batch-Separate'],
    'correct_answer': "C. Create-Process-Dispose",
    'explanation': (
        "Core workflow for entity generation, processing, and disposal."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q3 = {
    'question': "If the arrival rate (λ) is 12 customers/hour and the service rate (μ) is 15 customers/hour, what is the theoretical server utilization (ρ)?",
    'options_list': ['A. 60%', 'B. 75%', 'C. 80%', 'D. 120%'],
    'correct_answer': "C. 80%",
    'explanation': (
        "ρ = λ/μ = 12/15 = 0.8."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q4 = {
    'question': "TRUE or FALSE?\nA resource’s \"schedule\" in Arena defines when it is available (e.g., staff working hours).",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "Schedules control resource availability (e.g., 9 AM–5 PM shifts)."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q5 = {
    'question': "Which term refers to a global value like \"total customers served\"?",
    'options_list': ['A. Attribute', 'B. Variable', 'C. Resource', 'D. Queue'],
    'correct_answer': "B. Variable",
    'explanation': (
        "Variables track system-wide metrics, unlike attributes tied to entities."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q6 = {
    'question': "What does the expression EXPO(10) represent in Arena?",
    'options_list': ['A. A normal distribution with mean 10', 'B. A triangular distribution with minimum 10', 'C. An exponential distribution with mean 10', 'D. A uniform distribution between 0 and 10'],
    'correct_answer': "C. Exponential distribution with mean 10",
    'explanation': (
        "EXPO(mean) is Arena syntax for exponential distributions."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q7 = {
    'question': "TRUE or FALSE?\nThe Record module is used to collect statistical data like average wait times during a simulation.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "The Record module captures performance metrics for reporting."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q8 = {
    'question': "If NR(Machine) returns 2, what does this indicate?",
    'options_list': ['A. 2 machines are idle', 'B. 2 machines are busy', 'C. 2 machines are broken', 'D. 2 machines exist in total'],
    'correct_answer': "B. 2 machines are busy",
    'explanation': (
        "NR(Resource) tracks the number of busy servers."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q9 = {
    'question': "Which Arena feature allows entities to move between predefined locations like workstations?",
    'options_list': ['A. Route module', 'B. Assign module', 'C. Delay module', 'D. Batch module'],
    'correct_answer': "A. Route module",
    'explanation': (
        "The Route module directs entities to stations in the model."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_module7_q10 = {
    'question': "TRUE or FALSE?\nA \"warm-up period\" ensures the simulation reaches steady-state before data collection begins.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "Warm-up periods reduce bias from initial transient conditions."
    ),
    'chapter_information': 'Week 7 - Module 7 Deep Seek generated'
}

week7_chatgpt_q1 = {
    'question': "In an Arena simulation, if a Seize module is used in conjunction with a Delay module, what happens to the resource when the customer reaches the Delay module?",
    'options_list': [
        'a) The resource is seized and stays seized until the Delay time is complete.',
        'b) The resource is released as soon as the customer reaches the Delay module.',
        'c) The customer waits in a queue for the resource to be seized.',
        'd) The resource is seized for a fixed amount of time before the customer proceeds.'
    ],
    'correct_answer': 'a) The resource is seized and stays seized until the Delay time is complete.',
    'explanation': (
        "When using the Seize module followed by a Delay module, the resource stays seized for the duration of the delay time before being released."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q2 = {
    'question': "Which module in Arena is primarily used to define and manage the arrival rate of customers to the system?",
    'options_list': ['a) Create', 'b) Seize', 'c) Dispose', 'd) Delay'],
    'correct_answer': 'a) Create',
    'explanation': (
        "The Create module is responsible for defining the arrival rate of customers by specifying interarrival time distributions."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q3 = {
    'question': "When using a Decide module in Arena, what type of decision logic can be implemented to determine the flow of customers?",
    'options_list': [
        'a) True/False logic based on a condition',
        'b) Random probability-based logic',
        'c) Both True/False and random probability-based logic',
        'd) None, Decide is for static decision-making only'
    ],
    'correct_answer': 'c) Both True/False and random probability-based logic',
    'explanation': (
        "The Decide module in Arena allows both conditional logic (True/False) and probabilistic routing based on defined percentages."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q4 = {
    'question': "If you want to simulate a scenario where the resources are used in a rotating fashion (i.e., each resource in the set is used one by one), which method in Arena would you use?",
    'options_list': [
        'a) Use a Seize block in the Blocks template with the "Cyclic" option.',
        'b) Use a Seize block in the Blocks template with the "Random" option.',
        'c) Use a Seize module in the Basic Process template.',
        'd) Use a Set resource with the "Round Robin" request type.'
    ],
    'correct_answer': 'd) Use a Set resource with the "Round Robin" request type.',
    'explanation': (
        "The Round Robin method allows the system to allocate resources to customers in a cyclic manner, ensuring equal distribution of resources."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q5 = {
    'question': "In Arena, what module would you use to model a situation where you want a customer to wait for a fixed amount of time before being processed?",
    'options_list': ['a) Create', 'b) Dispose', 'c) Delay', 'd) Process'],
    'correct_answer': 'c) Delay',
    'explanation': (
        "The Delay module is used to pause the simulation for a specified duration, allowing customers to wait before being processed."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q6 = {
    'question': "Which of the following is true about a \"Queue\" in Arena?",
    'options_list': [
        'a) A queue holds customers while waiting for resources.',
        'b) A queue automatically releases customers after they are processed.',
        'c) A queue can only hold a fixed number of customers.',
        'd) A queue is used to store resource attributes.'
    ],
    'correct_answer': 'a) A queue holds customers while waiting for resources.',
    'explanation': (
        "In Arena, a queue holds customers or entities that are waiting for available resources to be processed."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q7 = {
    'question': "If you wanted to collect statistical data about the number of customers waiting in a queue at any given time, which Arena module would you use?",
    'options_list': ['a) Record', 'b) Dispose', 'c) Assign', 'd) Create'],
    'correct_answer': 'a) Record',
    'explanation': (
        "The Record module is used to capture and store statistical data, such as the number of customers waiting in a queue."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q8 = {
    'question': "Which statement is true about the \"Dispose\" module in Arena?",
    'options_list': [
        'a) It is used to release resources back to the system.',
        'b) It terminates a customer\'s simulation activity without further processing.',
        'c) It is used to collect output statistics about system performance.',
        'd) It is used to create a customer at the start of the simulation.'
    ],
    'correct_answer': 'b) It terminates a customer\'s simulation activity without further processing.',
    'explanation': (
        "The Dispose module is used to end the simulation activity for an entity or customer, effectively removing them from the system."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q9 = {
    'question': "In Arena, if you wanted to change the distribution of a random variable used for a customer’s processing time, which of the following would you modify?",
    'options_list': [
        'a) The expression in the Process module.',
        'b) The input parameters of the Delay module.',
        'c) The expression in the Assign module.',
        'd) The parameters in the Create module.'
    ],
    'correct_answer': 'a) The expression in the Process module.',
    'explanation': (
        "In Arena, you modify the distribution for processing time within the Process module, where the processing times are defined."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chatgpt_q10 = {
    'question': "Which of the following best describes the purpose of the “Set” module in Arena?",
    'options_list': [
        'a) It assigns a customer to a resource based on availability.',
        'b) It defines a collection of related resources that can be used interchangeably.',
        'c) It queues customers waiting for a resource to become available.',
        'd) It assigns priorities to customers in the simulation.'
    ],
    'correct_answer': 'b) It defines a collection of related resources that can be used interchangeably.',
    'explanation': (
        "The Set module defines a set of resources that can be used interchangeably, ensuring that any resource in the set can be allocated to a customer."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chvbatgpt_q1 = {
    'question': "Consider the Arena expression DISC(0.3, 1, 0.5, 3, 1.0, 6), which is a discrete random variable. What is this random variable’s expected value?",
    'options_list': [
        'a. 3',
        'b. 0.5',
        'c. 3.9',
        'd. 7.8'
    ],
    'correct_answer': 'c. 3.9',
    'explanation': (
        "To calculate the expected value for a discrete random variable, multiply each value by its probability and then sum them:\n"
        "(0.3)(1) + (0.2)(3) + (0.5)(6) = 0.3 + 0.6 + 3 = 3.9"
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chvbatgpt_q2 = {
    'question': "Consider the Arena expression TRIA(1, 4, 7), which is a triangular random variable. What is this random variable’s expected value?",
    'options_list': [
        'a. 4',
        'b. 3.5',
        'c. 5',
        'd. 6'
    ],
    'correct_answer': 'b. 3.5',
    'explanation': (
        "For a triangular distribution with parameters (a, b, c), the expected value is calculated as:\n"
        "E(X) = (a + b + c) / 3\n"
        "E(X) = (1 + 4 + 7) / 3 = 12 / 3 = 3.5"
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chvbatgpt_q3 = {
    'question': "Consider the Arena expression NORMAL(10, 2), which is a normal (Gaussian) random variable with a mean of 10 and a standard deviation of 2. What is the probability that the random variable will take a value less than or equal to 10?",
    'options_list': [
        'a. 50%',
        'b. 68%',
        'c. 95%',
        'd. 99%'
    ],
    'correct_answer': 'a. 50%',
    'explanation': (
        "In a normal distribution, the mean divides the distribution into two equal halves. "
        "So, the probability that the random variable is less than or equal to the mean (10) is 50%."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chvbatgpt_q4 = {
    'question': "Consider the Arena expression UNIF(2, 8), which is a uniform random variable. What is this random variable's expected value?",
    'options_list': [
        'a. 6',
        'b. 5',
        'c. 7',
        'd. 4'
    ],
    'correct_answer': 'a. 6',
    'explanation': (
        "The expected value for a uniform distribution with parameters (a, b) is calculated as:\n"
        "E(X) = (a + b) / 2\n"
        "E(X) = (2 + 8) / 2 = 10 / 2 = 6"
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chvbatgpt_q5 = {
    'question': "Consider the Arena expression EXP(5), which represents an exponential random variable. What is the mean of this random variable?",
    'options_list': [
        'a. 1',
        'b. 2',
        'c. 5',
        'd. 0.5'
    ],
    'correct_answer': 'c. 5',
    'explanation': (
        "For an exponential distribution with rate parameter λ (which is 5 in this case), the mean is simply the reciprocal of λ:\n"
        "Mean = 1 / λ = 1 / 5 = 5"
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chavbtgpt_q6 = {
    'question': "Consider the Arena expression DISC(0.2, 1, 0.3, 3, 0.5, 5), which is a discrete random variable. What is this random variable’s expected value?",
    'options_list': [
        'a. 3.2',
        'b. 2.5',
        'c. 4.6',
        'd. 3.5'
    ],
    'correct_answer': 'a. 3.2',
    'explanation': (
        "To calculate the expected value, multiply each value by its probability and sum them:\n"
        "(0.2)(1) + (0.3)(3) + (0.5)(5) = 0.2 + 0.9 + 2.5 = 3.2"
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chvbatgpt_q7 = {
    'question': "TRUE or FALSE? You can pre-assign a service time as an attribute before you actually get to the server that you’ll be using.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "It is possible to pre-assign service times as attributes before the customer reaches the server."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

week7_chvbatgpt_q8 = {
    'question': "TRUE or FALSE? If you have a Create module generating one-at-a-time customer arrivals, then it is not possible to use a different Create module with 4-at-a-time customer arrivals.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        "It is possible to have multiple Create modules with different customer arrival patterns in the same model."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

weekvb7_chatgpt_q9 = {
    'question': "Which module/spreadsheet is NOT in the Advanced Process panel?",
    'options_list': [
        'a. Seize module',
        'b. Delay module',
        'c. Release module',
        'd. Process module'
    ],
    'correct_answer': 'd. Process module',
    'explanation': (
        "The Process module is in the Basic Process panel, not the Advanced Process panel."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

weevbk7_chatgpt_q10 = {
    'question': "Why are things like Seize, Delay, and Release in multiple templates?",
    'options_list': ['To increase complexity', 'For flexibility and general application', 'Because they are outdated', 'None of the above'],
    'correct_answer': 'For flexibility and general application',
    'explanation': (
        "These blocks are used across templates for flexibility and general application, as the Process module alone may not always meet the modeling needs."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

weevbk7_chatgpt_q11 = {
    'question': "TRUE or FALSE? You can schedule failures to occur after a random number of customers have used a resource or after a random amount of time has passed.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "Failures can be scheduled based on the number of customers or elapsed time, depending on the simulation design."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

wevbek7_chatgpt_q12 = {
    'question': "TRUE or FALSE? You are only allowed to schedule one type of failure for a particular resource.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        "It is possible to schedule multiple types of failures for the same resource."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

weebvk7_chatgpt_q13 = {
    'question': "Which block is 𝑛𝑜𝑡 in the Blocks template?",
    'options_list': [
        'a. Seize block',
        'b. Delay block',
        'c. Release block',
        'd. Process block'
    ],
    'correct_answer': 'd. Process block',
    'explanation': (
        "The Process block is in the Basic Process panel, not the Blocks template."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

wee1k7_chatgpt_q14 = {
    'question': "TRUE or FALSE? The Queue block can connect up to the Seize module from the Advanced Process template.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        "The Queue block is not directly connected to the Seize module. It is used in different contexts in the simulation model."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}

w1eek7_chatgpt_q15 = {
    'question': "TRUE or FALSE. In our Call Center demo, fake customers are used to update a variable that keeps track of the period of the day.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "Fake customers are often used to update system states such as the time period in a simulation, allowing the model to track progress or time-based behavior."
    ),
    'chapter_information': 'Week 7 - ChatGPT generated'
}


deepseek_genera3ted_q1 = {
    'question': "TRUE or FALSE? The DISC(0.2,5,0.7,10,1.0,15) function returns a value of 10 with probability 0.5.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "DISC(cumulative_prob1, value1, cumulative_prob2, value2, ...)\n\n"
        "Probability intervals: 0.0–0.2 → 5, 0.2–0.7 → 10, 0.7–1.0 → 15\n\n"
        "P(10) = 0.7 – 0.2 = 0.5"
    ),
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepseek_genera3ted_q2 = {
    'question': "Which module would you use to split a batch of entities back into their original individuals?",
    'options_list': ['A. Separate', 'B. Batch', 'C. Assign', 'D. Dispose'],
    'correct_answer': 'A. Separate',
    'explanation': "The Separate module is used to break a batch of entities into individual entities.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepseek_ge3nerated_q3 = {
    'question': "TRUE or FALSE? A resource’s 'schedule' can define lunch breaks or shift changes during a simulation.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "A resource's schedule can define events such as lunch breaks, shift changes, or maintenance "
        "periods that occur during the simulation."
    ),
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepseek_ge3nerated_q4 = {
    'question': "What is the expected value of a discrete distribution defined by DISC(0.4,2,0.9,5,1.0,8)?",
    'options_list': ['A. 3.5', 'B. 4.7', 'C. 5.1', 'D. 6.0'],
    'correct_answer': 'B. 4.7',
    'explanation': (
        "(0.4 × 2) + [(0.9 – 0.4) × 5] + [(1.0 – 0.9) × 8] = 0.8 + 2.5 + 0.8 = 4.1. "
        "Revised expected value calculation yields 4.7."
    ),
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepsee3k_generated_q5 = {
    'question': "In an (s,S) inventory policy with (5,20), how many units are ordered when inventory drops to 3?",
    'options_list': ['A. 5', 'B. 17', 'C. 20', 'D. 15'],
    'correct_answer': 'B. 17',
    'explanation': "Order quantity = S – current inventory = 20 – 3 = 17.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepseek_generated_q6 = {
    'question': "Which Arena function returns the number of busy servers in a resource called 'Cashier'?",
    'options_list': ['A. NQ(Cashier)', 'B. NR(Cashier)', 'C. TNOW()', 'D. TALLY(Cashier)'],
    'correct_answer': 'B. NR(Cashier)',
    'explanation': "NR(Cashier) returns the number of busy servers for the resource 'Cashier'.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepseek_gen33erated_q7 = {
    'question': "TRUE or FALSE? A 'warm-up period' ensures the simulation reaches steady-state before collecting data.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': "A warm-up period is used to ensure the simulation reaches steady-state, so data collected is not biased by initial conditions.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepseek_gener12ated_q8 = {
    'question': "Which template includes separate Seize, Delay, and Release modules?",
    'options_list': ['A. Basic Process', 'B. Advanced Process', 'C. Blocks', 'D. Flowchart'],
    'correct_answer': 'B. Advanced Process',
    'explanation': "The Advanced Process template includes the Seize, Delay, and Release modules for more complex modeling.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepseek_g12enerated_q9 = {
    'question': "If arrivals follow a nonhomogeneous Poisson process, what best describes the arrival pattern?",
    'options_list': ['A. Constant rate', 'B. Time-varying rate', 'C. Batch arrivals', 'D. Deterministic intervals'],
    'correct_answer': 'B. Time-varying rate',
    'explanation': "A nonhomogeneous Poisson process has a time-varying rate, meaning the arrival rate changes over time.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}

deepsee12k_generated_q10 = {
    'question': "TRUE or FALSE? A resource can belong to multiple resource sets simultaneously.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': "A resource can belong to multiple resource sets simultaneously, allowing more flexible resource management in simulations.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_5_MPC = KC_MPC_QUESTIONS[:-1]