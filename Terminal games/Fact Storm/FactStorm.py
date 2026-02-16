'''
🧠 Fact Storm
A Simple Python Quiz Game

Fact Storm is a fun and interactive terminal-based quiz game built with Python.  
It challenges your general knowledge with random questions every round — test your brain, one fact at a time!

---

Features
- 20 unique general knowledge questions  
- Random 5-question selection per round  
- Smart scoring system with ✅ / ❌ feedback  
- Simple replay loop  
- Clean and beginner-friendly Python structure  

---

How It Works
1. Run the script in your terminal:
   ```bash
   python fact_storm.py
The program will display 5 random questions.

Type your answers — spelling matters!

Get your score and feedback:

5/5 → You won! 🏆

3–4 → Not bad 😉

0–2 → Try again later 😅

Choose to play again or exit.

⚙️ Requirements

Python 3.7+

No external libraries needed

Example Gameplay
🧠 Welcome to Fact Storm!
Now you can exercise your brain...

🧠 Which ocean is the deepest on Earth?
Answer: ...
✅ Correct!

🧠 Who invented the telephone?
Answer: alexander..
✅ Correct!

Your final score: 5/5
🏆 You won!

Do you want to finish the game? (y/n): y
'''


import random

Questions_list = {
    "What is the largest planet in our solar system?": "jupiter",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What is the capital city of Australia?": "canberra",
    "Which ocean is the deepest on Earth?": "pacific",
    "How many bones are in the adult human body?": "206",
    "What is the hardest natural substance on Earth?": "diamond",
    "Which country is known as the Land of the Rising Sun?": "japan",
    "Who wrote the play 'Hamlet'?": "william shakespeare",
    "What is the chemical symbol for water?": "h2o",
    "Which planet is closest to the Sun?": "mercury",
    "What is the largest mammal in the world?": "blue whale",
    "In what year did man first land on the moon?": "1969",
    "Which animal is known for its black and white stripes?": "zebra",
    "What is the smallest prime number?": "2",
    "Which element has the chemical symbol 'O'?": "oxygen",
    "Who invented the telephone?": "alexander graham bell",
    "How many continents are there on Earth?": "7",
    "What is the capital city of Canada?": "ottawa",
    "Which bird is known for its colorful tail feathers?": "peacock",
    "Which language has the most native speakers worldwide?": "mandarin"
}

#A function for quiz running
def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        print("\U0001F9E0 "+question)
        user_answer = input("Answer: ").strip().lower()
        if user_answer == answer:
            print("Correct \u2705")
            score += 1
        else:
            print("Wrong \u274C")
    return score


#A function for calculating user's score
def calculate_score(score):
    if score==5:
        print(f"You won! \U0001F3C6\nYour score is {score} of 5")
    elif 3<= score <=4:
        print(f"Not bad \U0001F609.\nYour score is {score} of 5")
    else:
        print(f"Try again later \U0001F605.\nYour score is {score} of 5")



print("\U0001F4A1 Hello, Welcome to Fact Strom!\nNow you can exercise your brain...\n\n")


while True:
    
    #Selecting unique questions
    selected_questions = dict(random.sample(list(Questions_list.items()), 5))
    calculate_score(run_quiz(selected_questions))

    #Game finishing
    leave_game=input("Do you want to finish the game ? (y/n) : ").strip().lower()
    if leave_game=='y':
        print("Please come back soon \U0001F60A")
        break