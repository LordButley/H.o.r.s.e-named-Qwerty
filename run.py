import random
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('leaderboard')

# sales = SHEET.worksheet('Sheet1')

# data = sales.get_all_values()

# print(data)

print("Welcome to Gamename")
print("Take a typing challenge and see how you compare to others")
print("You have 100 seconds to type as many answers as possible")
print("You can only make so many mistakes")
print("Good luck!")

# score_data = [0, 0, 0]
# username = input("What is your name? ")

ANSWERS_STAR_WARS = ["Jedi", "Lightsaber", "Skywalker", "Luke", "Leia", "Darth", "Vader", "Maul", "Padawan", "Obi wan", "Kenobi", "Millenium", "Falcon", "Clone", "Droid", "Palpatine", "Emporer", "Republic", "Galaxy", "Hoth", "Endor", "Anakin", "Han Solo", "Tatooine"]
ANSWERS_ELEMENTS = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium"]
ANSWERS_HARRY_POTTER = ["Harry", "Potter", "Ron", "Weasley", "Hermione", "Granger", "Voldemort", "Snape", "Professor", "Dumbledore", "Draco", "Malfoy", "Wand", "Owl", "Broomstick", "Philosopher", "Chamber", "Prisoner", "Azkaban", "Dementor"]

class User:
    def __init__ (self):
        self.name = input("What is your name? ")
        self.score = 0


class Quiz:

    # bug2
    def __init__(self):
        self.answers = self.select_theme()
        self.lives = self.select_difficulty()

    def select_theme(self):
        '''
        Function enabling user to select the theme of the typing challenge.
        '''
        print("Typing themes:")
        print("1 - Star Wars")
        print("2 - Harry Potter")
        # print("3 - Beer brands")
        print("3 - Periodic table of elements")
        theme_selection = input("Please enter the number of your choice: ")
        # first bug
        if theme_selection == "1":
            answer_set = random.sample(ANSWERS_STAR_WARS, 10)
            print(answer_set)
        elif theme_selection == "2":
            answer_set = random.sample(ANSWERS_HARRY_POTTER, 10)
            print(answer_set)
        elif theme_selection == "3":
            answer_set = random.sample(ANSWERS_ELEMENTS, 10)
            print(answer_set)
        return answer_set

    def select_difficulty(self):
        '''
        Function enabling user to select the difficulty of the game.
        '''
        print("What difficulty would you like to play?")
        print("1 - Easy")
        print("2 - Normal")
        print("3 - Hard")
        difficulty_selection = input("Please enter the number of your choice: ")
        if difficulty_selection == "1":
            lives = 5
            print(lives)
        elif difficulty_selection == "2":
            lives = 4
            print(lives)
        elif difficulty_selection == "3":
            lives = 3
            print(lives)
        return lives

# class Timer:
#     game_over = time.time() + 100

def new_game():
    print("Start new game?: ")
    new_game = input("Press Y for yes and N for no: ")
    if new_game == "y":
        new_user = User()
        new_game = Quiz()
        # new_timer = Timer()

new_game()



    # def next_question():
    #     for answer in answers:
    #         print(answer)
    #         x = input("Enter answer: ")
    #         if answer == x:
    #             correct_answer += 1
    #         else:
    #             lives -= 1


