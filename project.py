#!/usr/bin/env python3

'''Description: The script creates an interactive educational game with persistent leaderboard storage.'''

import tkinter as tk
from tkinter import messagebox
import random
import json

#Creates a Path to the leaderboard file where the games scores will be stored
LEADERBOARD_FILE = "leaderboard.json"

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
                       "Answer": "D"},
        "Question 8": {"Question": "What is the largest planet in our solar system?",
                       "Options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
                       "Answer": "B"},
        "Question 9": {"Question": "What element does 'O' represent on the periodic table?",
                       "Options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Iron"],
                       "Answer": "B"},
        "Question 10": {"Question": "At what temperature does water boil?",
                        "Options": ["A. 212 degrees Fahrenheit", "B. 100 degrees Celsius", "C. Both A and B", "D. 98.6 degrees Fahrenheit"],
                        "Answer": "C"},
        "Question 11": {"Question": "Which of the following is NOT a type of cloud?",
                        "Options": ["A. Cumulus", "B. Stratus", "C. Cirrus", "D. Cumulonimbus", "E. Papyrus"],
                        "Answer": "E"},
        "Question 12": {"Question": "What force pulls objects toward the center of the Earth?",
                        "Options": ["A. Magnetic force", "B. Gravity", "C. Electromagnetic force", "D. Friction"],
                        "Answer": "B"}
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
                       "Answer": "D"},
        "Question 8": {"Question": "Which country has the most islands in the world?",
                       "Options": ["A. Finland", "B. Canada", "C. Indonesia", "D. Sweden"],
                       "Answer": "C"},
        "Question 9": {"Question": "In which country is the ancient city of Petra located?",
                       "Options": ["A. Egypt", "B. Jordan", "C. Israel", "D. Syria"],
                       "Answer": "B"},
        "Question 10": {"Question": "What is the smallest country in the world by land area?",
                        "Options": ["A. Monaco", "B. Nauru", "C. Vatican City", "D. San Marino"],
                        "Answer": "C"},
        "Question 11": {"Question": "Which country is known as the Land of the Thunder Dragon?",
                        "Options": ["A. Bhutan", "B. Nepal", "C. Myanmar", "D. Thailand"],
                        "Answer": "A"},
        "Question 12": {"Question": "Which country is both a continent and a country?",
                        "Options": ["A. Greenland", "B. India", "C. Australia", "D. Antarctica"],
                        "Answer": "C"}
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
                        "Answer": "B" },
         "Question 8": {"Question": "Which country is the largest by land area?",
                        "Options": ["A. China", "B. United States", "C. Canada", "D. Russia"],
                        "Answer": "D"},
         "Question 9": {"Question": "What is the capital city of Italy?",
                        "Options": ["A. Turin", "B. Venice", "C. Rome", "D. Milan"],
                        "Answer": "C"},
         "Question 10": {"Question": "Who painted the Mona Lisa?",
                         "Options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
                         "Answer": "C"},
         "Question 11": {"Question": "Which is the longest river in the world?",
                         "Options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
                         "Answer": "B"},
         "Question 12": {"Question": "What is the hardest natural substance on Earth?",
                         "Options": ["A. Gold", "B. Diamond", "C. Quartz", "D. Iron"],
                         "Answer": "B"}
         }
    }

#Load existing leaderboard data from a file
def load_leaderboard():
#The function loads the leaderboard from the JSON file
#The try and except block would handle error and manage issues that may arise when attempting to open or read the file.
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            #opens the leaderboard file in read mode
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
#If the file does not exist (FileNotFoundError) or if the content is not JSON (JSONDecodeError), then handle these exceptions by returning an empty dictionary.
        return {}

#Save the leaderboard data to a file
def save_leaderboard(leaderboard):
#THe function takes one argument, 'leaderboard', which is a dictionary containing the current leaderboard data
    with open(LEADERBOARD_FILE, "w") as file:
#It opens the file in write mode ('w') and overwrites the content or start a new file if not created yet
        json.dump(leaderboard, file, indent=4)

#THe function starts the game with a welcoming message and prompts the user to enter their name, then they select a category in the quiz.
def play_quiz():
    print("Welcome to the Quiz Game!")
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Let's get started.")
#Select a quiz category
    print("\nSelect a quiz category:")
    print("1. Science")
    print("2. Countries")
    print("3. General Knowledge")

#The while loop is used to ensure the player selects a between option 1-3. If any other input is made there is a valueerror that is raised prompting the user to enter valid input
    while True:
        try:
            category_choice = int(input("Enter the number of your choice: "))
            if category_choice not in range(1, 4):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the options.")

#Adjusting for zero based indexing. whatever input the user makes would become the selected category e.g user selects 1 which is for science then we have 1-1=0 which gives us position 0 in the list. THis goes for all other categories.
    selected_category = ["Science", "Countries", "General Knowledge"][category_choice - 1]
    print(f"\nYou've chosen the {selected_category} quiz. Let's begin!\n")

#Initialize player's score and lives
    score = 0
    lives = 2

#Retrieve and shuffle questions for the selected category
    questions = quiz_questions[selected_category]
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

#Iterate through the questions. THis section is the gameplay loop for the game as the questions are presented to the player, their answer collected and evaluated.
    for question_key in question_keys:
#Checks if player has run out of lives
        if lives == 0:
            break  #Exit the loop if the player runs out of lives
        question_data = questions[question_key]
        print(question_data["Question"])
        for option in question_data["Options"]:
            print(option)
        user_answer = input("Your answer: ").upper()

#Checks if the answer is correct and increases the the players score by 10 if correct. If incorrect, decreases player lives by 1 and informs player.
        if user_answer == question_data["Answer"]:
            print("Correct!")
            score += 10
        else:
            print("Incorrect!")
            lives -= 1
            if lives > 0:
                print(f"You have {lives} live remaining.")

#Game over messages
    if lives > 0:
        print("\nCongratulations! You completed the game!")
    else:
        print("Game over! You ran out of lives.\nRun the code to try again.")

    print(f"\nYour final score is: {score}")
    return name, score


#The function uses Tkinter to create a graphical User interface (GUI) to display the game's leaderboard.
def display_leaderboard_gui(leaderboard):
    root = tk.Tk()
    root.title("Leaderboard")

    tk.Label(root, text="Leaderboard", font=("Arial", 16)).pack(pady=10)
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for i, (player, score) in enumerate(sorted_leaderboard[:5], 1):
        tk.Label(root, text=f"{i}. {player}: {score} points", font=("Arial", 14)).pack()

    tk.Button(root, text="Close", command=root.destroy).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    leaderboard = load_leaderboard()

#This is now correctly expecting two return values.
    name, player_score = play_quiz()

#Load the leaderboard again in case it was updated during the game
    leaderboard = load_leaderboard()

#Checks if player is previously in the leaderboard and checks their score.
    max_score = leaderboard.get(name, 0)
    if player_score > max_score:
        leaderboard[name] = player_score
        save_leaderboard(leaderboard)

    display_leaderboard_gui(leaderboard)
