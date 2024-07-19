import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERANDS = 3
MAX_OPERANDS = 12
TOTAL_PROBLEMS = 5


def generate_math_problem():
    left = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    right = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("You want to start")
print("----------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_math_problem()

    while True:
        guess = input("problem: " + str(i + 1) + expr + " = ")
        if guess == str(answer):
            break

        wrong += 1
end_time = time.time()
total_time = start_time - end_time

print("---------------------------------")
print("Nice Work")
print("You finished in " + total_time)

