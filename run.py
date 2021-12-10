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
score_data = [0, 0, 0]
username = input("What is your name? ")

ANSWERS_STAR_WARS = {"Jedi", "Lightsaber", "Skywalker", "Luke", "Leia", "Darth", "Vader", "Maul", "Padawan", "Obi wan", "Kenobi", "Millenium", "Falcon", "Clone", "Droid", "Palpatine", "Emporer", "Republic", "Galaxy", "Hoth", "Endor", "Anakin", "Han Solo", "Tatooine"}
ANSWERS_ELEMENTS = {"Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium"}
ANSWERS_HARRY_POTTER ={"Harry", "Potter", "Ron", "Weasley", "Hermione", "Granger", "Voldemort", "Snape", "Professor", "Dumbledore", "Draco", "Malfoy", "Wand", "Owl", "Broomstick", "Philosopher", "Chamber", "Prisoner", "Azkaban", "Dementor"}

def select_theme():
    '''
    Function to select the theme of the typing challenge.
    '''
    print("Typing themes:")
    print("1 - Star Wars")
    print("2 - Harry Potter")
    # print("3 - Beer brands")
    print("3 - Periodic table of elements")
    theme_selection = input("Please enter the number of your choice: ")
    if theme_selection == 1:
        


