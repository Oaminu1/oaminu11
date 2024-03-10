#!/usr/bin/env python3

'''Description: The script creates an interactive educational game'''

import random

#dictionary of quiz questions
quiz_questions = {
        "Science": {
            "Question 1": {"Question": "How many bones are there in the human body?",
                           "Options": ["A. 206", "B. 300", "C. 150", "D. 120"],
                           "Answer": "A" },
             "Question 2": {"Question": "What is the chemical symbol for Gold?",
                           "Options": ["A. Au", "B. Ag", "C. Hg", "D. Fe"],
                           "Answer": "A" },

            },

        "Countries": {
             "Question 1": {"Question": "What is the capital of France?",
                           "Options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
                           "Answer": "A" },
              "Question 1": {"Question": "What is the capital of Canada?",
                           "Options": ["A. Ottawa", "B. Toronto", "C. Vancouver", "D. Montreal"],
                           "Answer": "A" },
              },

        "General Knowledge": {
             "Question 1": {"Question": "What is the capital of Japan?",
                           "Options": ["A. Tokyo", "B. Beijing", "C. Seoul", "D. Bangkok"],
                           "Answer": "A" },
              "Question 2": {"Question": "Who painted the Mona Lisa?",
                           "Options": ["A. Leonardo da Vinci ", "B. Vincent Van gogh", "C. Michealangelo", "D. Pablo Escobar"],
                           "Answer": "A" },
              }
        }


#dictionary of answers for each question
'''
quiz_answers = {
        



}
'''

#leaderboard to store player scores
leaderboard = {}

def display_leaderboard():
    print("\nLeaderboard:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for i, (player, score) in enumerate(sorted_leaderboard[:5], 1):
        print(f"{i}. {player}: {score} points")

def start_quiz():
    print("Welcome to the Quiz Game!")
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Let's get started.")

    #select a quiz category
    print("\nSelect a quiz category:")
    print("1. Science")
    print("2. Countries and their capital")
    print("3. General Knowledge")

    #Ensure the user enters a valid category choice
    while True:
        try:
            category_choice = int(input("Enter the number of your choice: "))
            if category_choice not in range(1, 4):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the options.")
    selected_category = ["Science", "Countries", "General Knowledge"][category_choice -1]


    print(f"\nYou've chosen the {selected_category} quiz. Lets begin!\n")


    #Initialize players score and lives
    score = 0
    lives = 3

    #retrieve questions for the selected category
    questions = quiz_questions[selected_category]

    #shuffle the questions for variety
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    #iterate through the questions
    for question_key in question_keys:
        question_data = questions[question_key]
        print(question_data["Question"])
        for option in question_data["Options"]:
            print(option)
        user_answer = input("Your answer: ").upper()

        #check if the answer is correct
        if user_answer == question_data["Answer"]:
            print("Correct!")
            score += 10
        else:
            print("Incorrect!")
            lives -= 1
            print(f"You have {lives} lives remaining.")

        #check if player has run out of lives
        if lives == 0:
            print("Game over! You ran out of lives.\nRun code to try again.")
            break

        #update leaderboard with player's score
        leaderboard[name] = score

        print(f"\nYour final score is: {score}")
        display_leaderboard()

#main program
if __name__ == "__main__":
    start_quiz()
