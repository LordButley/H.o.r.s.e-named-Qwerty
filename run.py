import random
import time
import string
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
leaderboard = SHEET.worksheet('Sheet1')
ordered_leaderboard = SHEET.worksheet("highscore")

print("Welcome to Gamename")
print("Take a typing challenge and see how you compare to others")
print("You have 60 seconds to type as many answers as possible")
print("You can only make so many mistakes")
print("Good luck!")

ANSWERS_STAR_WARS = [
    "Jedi", "Lightsaber", "Skywalker", "Luke", "Leia",
    "Darth", "Vader", "Maul", "Padawan", "Obi Wan",
    "Kenobi", "Millenium", "Falcon", "Clone", "Droid",
    "Palpatine", "Emperor", "Republic", "Galaxy", "Hoth",
    "Endor", "Anakin", "Han Solo", "Tatooine", "Rey",
    "Kylo Ren", "Death Star", "Stormtrooper", "Carbonite",
    "Greivous", "Jabba", "Master", "Dooku", "Mandalorian",
    "Phantom", "Menace", "Attack", "Revenge", "Sith",
    "Hope", "Strikes", "Back", "Return", "Awakens",
    "Jar Jar Binks", "Squadron", "Ewok", "Mace Windu"
    "Planet", "Wookie", "Chewbacca", "Xwing",
    "Alderaan", "Dark side"
    ]

ANSWERS_ELEMENTS = [
    "Hydrogen", "Helium", "Lithium", "Beryllium",
    "Boron", "Carbon", "Nitrogen", "Oxygen",
    "Fluorine", "Neon", "Sodium", "Magnesium",
    "Aluminium", "Silicon", "Phosporous", "Sulfur",
    "Chlorine", "Argon", "Potassium", "Calcium"
    ]

ANSWERS_HARRY_POTTER = [
    "Harry", "Potter", "Ron", "Weasley",
    "Hermione", "Granger", "Voldemort", "Snape",
    "Professor", "Dumbledore", "Draco", "Malfoy", "Wand",
    "Owl", "Broomstick", "Philosopher", "Chamber",
    "Prisoner", "Azkaban", "Dementor", "Snitch", "Quidditch",
    "Seeker", "Hogwarts", "Lupin", "Tonks", "Whomping",
    "Willow", "Wizards", "Witch", "Triwizard",
    "Hagrid", "Hedwig", "Muggle", "Gryffindor",
    "Ravenclaw", "Slytherin", "Mudblood", "Butterbeer",
    "Hufflepuff", "Phoenix", "Diagon", "Horcrux",
    "Lumos", "Avada Kedavra", "Crucio", "Imperio"
    ]


class User:
    '''
    Creates an instance of User
    '''
    def __init__(self):
        self.name = input("What is your name? \n")
        self.score = 0
        self.difficulty = ""


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
        theme_selection = input("Please enter the number of your choice: \n")
        # first bug - input is always a string.
        if theme_selection == "1":
            answer_set = random.sample(ANSWERS_STAR_WARS, len(ANSWERS_STAR_WARS))
        elif theme_selection == "2":
            answer_set = random.sample(ANSWERS_HARRY_POTTER, len(ANSWERS_HARRY_POTTER))
        elif theme_selection == "3":
            answer_set = random.sample(ANSWERS_ELEMENTS, len(ANSWERS_ELEMENTS))
        return answer_set

    def select_difficulty(self):
        '''
        Function enabling user to select the difficulty of the game.
        '''
        print("What difficulty would you like to play?")
        print("1 - Easy")
        print("2 - Normal")
        print("3 - Hard")
        difficulty_selection = input("Please enter the number of your choice: \n")
        if difficulty_selection == "1":
            lives = 5
        elif difficulty_selection == "2":
            lives = 4
        elif difficulty_selection == "3":
            lives = 3
        return lives


class Timer:
    '''
    Creates an instance of Timer. This calculates the time in 60 seconds.
    '''

    def __init__(self):
        self.game_over = time.time() + 60


def new_game():
    '''
    Function which builds the game and questions. It calls the classes to be
    constructed and runs another function which runs through the questions
    '''

    new_user = User()
    new_quiz = Quiz()
    if new_quiz.lives == 5:
        new_user.difficulty = "Easy"
        print(new_user.difficulty)
    elif new_quiz.lives == 4:
        new_user.difficulty = "Normal"
    elif new_quiz.lives == 3:
        new_user.difficulty = "Hard"
    new_timer = Timer()
    x = 0
    # bug 3 - while loop not stopping(for loop inside of while loop)
    # bug 4 = x inside of while loop resetting to 0 everytime
    while new_timer.game_over > time.time() and new_quiz.lives != 0:
        print("       "+new_quiz.answers[x]+"\n")
        answer = string.capwords(input("Enter answer: \n").lower())
        if answer == new_quiz.answers[x]:
            new_user.score += 1
        else:
            new_quiz.lives -= 1
        x += 1
        print(f"Score: {new_user.score}     Lives: {new_quiz.lives}\n")
    user_result = [new_user.name, new_user.score, new_user.difficulty]
    leaderboard.append_row(user_result)
    print("Gameover!\n")
    print(f"{new_user.name} scored {new_user.score} on difficulty {new_user.difficulty.lower()}\n")
    play_game()


def play_game():
    '''
    Function which is called to play the game. It gives the user a choice
    as to whether they want to start. If they select yes then the game starts
    else they are given the option again.
    '''
    print("Start new game?: ")
    start_game = input("Press Y for yes and N for no: \n").lower()
    if start_game == "y":
        new_game()
    else:
        # print("View highscores?")
        # if (input("Press Y for yes and N for no: ").lower()) == "y":
            view_highscore()
            play_game()
    # print("Thanks for playing!")  


def view_highscore():
    '''
    Function retrieves data from an numerically ordered
    spreadsheet and splices the top 5 scores. These
    are then printed in formatted way.
    '''
    print("View highscores?")
    if (input("Press Y for yes and N for no: \n").lower()) == "y":
        scores = SHEET.worksheet("highscore").get_all_values()
        highscores = scores[slice(0, 6, 1)]
        print("\n")
        [print(f"{highscore[0]} --- {highscore[1]} --- {highscore[2]} ") for highscore in highscores]
        print("\n")

play_game()
