#!/usr/bin/env python3

'''Description: The script creates an interactive educational game with persistent leaderboard storage.'''

import random
import json

# Path to the leaderboard file
LEADERBOARD_FILE = "leaderboard.json"

# Load existing leaderboard data from a file
def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save the leaderboard data to a file
def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

# Display the top players from the leaderboard
def display_leaderboard(leaderboard):
    print("\nLeaderboard:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for i, (player, score) in enumerate(sorted_leaderboard[:5], 1):
        print(f"{i}. {player}: {score} points")

#dictionary of quiz questions
quiz_questions = {
    "Science": {
        "Question 1": {"Question": "How many bones are there in the human body?",
                       "Options": ["A. 206", "B. 300", "C. 150", "D. 120"],
                       "Answer": "A"},
        "Question 2": {"Question": "What is the chemical symbol for Gold?",
                       "Options": ["A. Au", "B. Ag", "C. Hg", "D. Fe"],
                       "Answer": "A"},
        "Question 3": {"Question": "Which vitamin is known as ascorbic acid?",
                       "Options": ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"],
                       "Answer": "C"},
        "Question 4": {"Question": "What gas do plants absorb from the atmosphere for photosynthesis?",
                       "Options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
                       "Answer": "C"},
        "Question 5": {"Question": "What is the most abundant gas in the Earth's atmosphere?",
                       "Options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Argon"],
                       "Answer": "B"},
        "Question 6": {"Question": "What is the boiling point of water at sea level?",
                       "Options": ["A. 90°C", "B. 100°C", "C. 110°C", "D. 120°C"],
                       "Answer": "B"},
        "Question 7": {"Question": "Which part of the cell contains the genetic material?",
                       "Options": ["A. Cytoplasm", "B. Mitochondria", "C. Cell membrane", "D. Nucleus"],
                       "Answer": "D"}
    },
    "Countries": {
        "Question 1": {"Question": "What is the largest country by land area?",
                       "Options": ["A. China", "B. Russia", "C. Canada", "D. United States"],
                       "Answer": "B"},
        "Question 2": {"Question": "Which country has the longest coastline in the world?",
                       "Options": ["A. Indonesia", "B. Norway", "C. Canada", "D. Australia"],
                       "Answer": "C"},
        "Question 3": {"Question": "In which country is the world's highest waterfall located?",
                       "Options": ["A. United States", "B. Canada", "C. Venezuela", "D. Norway"],
                       "Answer": "C"},
        "Question 4": {"Question": "What country is known as the Land of the Rising Sun?",
                       "Options": ["A. China", "B. Japan", "C. South Korea", "D. Thailand"],
                       "Answer": "B"},
        "Question 5": {"Question": "Which country has the most natural lakes?",
                       "Options": ["A. United States", "B. Brazil", "C. Canada", "D. Russia"],
                       "Answer": "C"},
        "Question 6": {"Question": "Which country is home to the Great Barrier Reef?",
                       "Options": ["A. Australia", "B. Brazil", "C. Indonesia", "D. Philippines"],
                       "Answer": "A"},
        "Question 7": {"Question": "Which country is the largest producer of coffee?",
                       "Options": ["A. Colombia", "B. Vietnam", "C. Ethiopia", "D. Brazil"],
                       "Answer": "D"}
    },
    "General Knowledge": {
        "Question 1": {"Question": "Who wrote 'Hamlet'?",
                       "Options": ["A. Charles Dickens", "B. William Shakespeare", "C. Leo Tolstoy", "D. Mark Twain"],
                       "Answer": "B" },
        "Question 2": {"Question": "What is the tallest mountain in the world?",
                       "Options": ["A. K2", "B. Kangchenjunga", "C. Mount Everest", "D. Lhotse"],
                       "Answer": "C" },
         "Question 3": {"Question": "What is the hardest natural substance on Earth?",
                        "Options": ["A. Gold", "B. Iron", "C. Diamond", "D. Quartz"],
                        "Answer": "C" },
         "Question 4": {"Question": "What is the capital of Australia?",
                        "Options": ["A. Sydney", "B. Perth", "C. Canberra", "D. Melbourne"],
                        "Answer": "C" },
         "Question 5": {"Question": "Who is known as the father of computers?",
                        "Options": ["A. Charles Babbage", "B. Alan Turing", "C. Ada Lovelace", "D. John von Neumann"],
                        "Answer": "A" },
         "Question 6": {"Question": "Which planet is known as the Red Planet?",
                        "Options": ["A. Mars", "B. Jupiter", "C. Venus", "D. Mercury"],
                        "Answer": "A" },
         "Question 7": {"Question": "What is the smallest prime number?",
                        "Options": ["A. 1", "B. 2", "C. 3", "D. 5"],
                        "Answer": "B" }
         }
    }

def start_quiz():
    print("Welcome to the Quiz Game!")
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Let's get started.")

    # Load the leaderboard from file
    leaderboard = load_leaderboard()

    # Select a quiz category
    print("\nSelect a quiz category:")
    print("1. Science")
    print("2. Countries")
    print("3. General Knowledge")
    while True:
        try:
            category_choice = int(input("Enter the number of your choice: "))
            if category_choice not in range(1, 4):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the options.")
    selected_category = ["Science", "Countries", "General Knowledge"][category_choice - 1]
    print(f"\nYou've chosen the {selected_category} quiz. Let's begin!\n")

    # Initialize player's score and lives
    score = 0
    lives = 2

    # Retrieve and shuffle questions for the selected category
    questions = quiz_questions[selected_category]
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    # Iterate through the questions
    for question_key in question_keys:
        if lives == 0:
            break  # Exit the loop if the player runs out of lives
        question_data = questions[question_key]
        print(question_data["Question"])
        for option in question_data["Options"]:
            print(option)
        user_answer = input("Your answer: ").upper()

        # Check if the answer is correct
        if user_answer == question_data["Answer"]:
            print("Correct!")
            score += 10
        else:
            print("Incorrect!")
            lives -= 1
            if lives > 0:
                print(f"You have {lives} lives remaining.")

    # Game over messages
    if lives > 0:
        print("\nCongratulations! You completed the game!")
    else:
        print("Game over! You ran out of lives.\nRun the code to try again.")

    print(f"\nYour final score is: {score}")

    # Update and save the leaderboard
    if name in leaderboard:
        leaderboard[name] = max(leaderboard[name], score)
    else:
        leaderboard[name] = score
    save_leaderboard(leaderboard)

    display_leaderboard(leaderboard)

if __name__ == "__main__":
    start_quiz()

