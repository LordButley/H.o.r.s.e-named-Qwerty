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
score_data = [0 ,0 ,0]
username = input("What is your name? ")

def select_theme():
    print("Typing themes:")
    print("1 - Star Wars")
    print("Harry Potter")
    print("Beer brands")
    print("Periodic table of elements")

