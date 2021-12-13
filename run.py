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
print("You have 60 seconds to type as many answers as possible")
print("You can only make so many mistakes")
print("Good luck!")

# score_data = [0, 0, 0]
# username = input("What is your name? ")

ANSWERS_STAR_WARS = ["Jedi", "Lightsaber", "Skywalker", "Luke", "Leia", "Darth", 
                    "Vader", "Maul", "Padawan", "Obi wan", "Kenobi", "Millenium",
                    "Falcon", "Clone", "Droid", "Palpatine", "Emperor", "Republic",
                    "Galaxy", "Hoth", "Endor", "Anakin", "Han Solo", "Tatooine", "Rey",
                    "Kylo Ren", "Death Star", "Stormtrooper", "Carbonite", "Greivous", "Jabba", "Master", "Dooku"]
ANSWERS_ELEMENTS = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosporous", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium"]
ANSWERS_HARRY_POTTER = ["Harry", "Potter", "Ron", "Weasley", "Hermione", "Granger", "Voldemort", "Snape", "Professor", "Dumbledore", "Draco", "Malfoy", "Wand", "Owl", "Broomstick", "Philosopher", "Chamber", "Prisoner", "Azkaban", "Dementor", "Snitch", "Quidditch", "Seeker", "Hogwarts", "Lupin", "Tonks", "Whomping", "Willow", "Wizards", "Witch"]

class User:
    '''
    Creates an instance of User
    '''
    def __init__ (self):
        self.name = input("What is your name? ")
        self.score = 0


class Quiz:
    '''
    Creates an instance of Quiz
    '''

    # bug2 - did not use self initially
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
        print("3 - Periodic table of elements")
        theme_selection = input("Please enter the number of your choice: ")
        # first bug - input is always a string.
        if theme_selection == "1":
            answer_set = random.sample(ANSWERS_STAR_WARS, len(ANSWERS_STAR_WARS))
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

class Timer:
    '''
    Creates an instance of Timer
    '''

    def __init__(self):
        self.game_over = time.time() + 60

def new_game():
    '''
    Function which builds the game and questions. It calls the classes to be constructed and runs another function which runs through the questions
    '''
    # print("Start new game?: ")
    # start_game = input("Press Y for yes and N for no: ")
    # if start_game == "y":
    new_user = User()
    new_game = Quiz()
    new_timer = Timer()
    x = 0
    # bug 3 - while loop not stopping(for loop inside of while loop)
    # bug 4 = x inside of while loop resetting to 0 everytime
    while new_timer.game_over > time.time() and new_game.lives != 0:
        print(new_game.answers[x])
        answer = input("Enter answer: ")
        if answer == new_game.answers[x]:
            new_user.score += 1
            print(new_user.score)
        else:
            new_game.lives -= 1  
            print(new_game.lives) 
        x = x + 1
        print(f"x is {x}")      
    print("gameover")
    play_game()        

def play_game():
    '''
    Function which is called to play the game. It gives the user a choice as to whether they want to start. If they select yes then the game starts else they are given the option again.
    '''
    print("Start new game?: ")
    start_game = input("Press Y for yes and N for no: ")
    if start_game == "y":
        new_game()
    else:
        play_game()

play_game()

    # def next_question():
    #     for answer in answers:
            # print(answer)
            # x = input("Enter answer: ")
            # if answer == x:
            #     correct_answer += 1
            # else:
            #     lives -= 1


