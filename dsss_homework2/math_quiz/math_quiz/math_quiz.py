import random

def generate_random_number(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.
    
    Args:
        min_value (int): The minimum value.
        max_value (int): The maximum value.
    
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)
    
def generate_random_operator():
    """
    Randomly selects a mathematical operator from a list of operators: +, -, *.
    Args:
        No args.
        
    Returns:
        str: A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])
    
def calculate_answer(num1, num2, operator):
    """
    Calculates the result of applying an operator on two numbers.
    
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        operator (str): The mathematical operator (+, -, or *).
    
    Returns:
        tuple: A string representing the math problem, and the answer to the problem.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # for multiplication (*)
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Runs the math quiz game, where the player is asked a series of math questions 
    and needs to provide the correct answers to score points.
    """
    score = 0
    total_questions = 5  # Number of questions in the game (set to a fixed value)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = calculate_answer(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        
        # Input handling with error checking
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue  # Skip to the next iteration if input is invalid

        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
