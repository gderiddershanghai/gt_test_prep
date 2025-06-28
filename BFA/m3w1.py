# BFA/m3w1.py

KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

BFA_M3W1_MPC = KC_MPC_QUESTIONS[:-1]
