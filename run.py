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
SHEET = GSPREAD_CLIENT.open('travel_flow')


def get_user_preferences():
    """
    Function to get user preferences for the type of travel experience.
    Returns:
        int: User preference as a number.
    """    
    print("Welcome to Travel-Flow! Let's help you find your ideal destination.")
    print("What type of travel experience are you looking for?")
    print("1. Adventure\n2. Cultural\n3. Active\n4. Relaxing\n5. Family\n6. Solo")

    while True:
        user_choice = input("Enter the number corresponding to your preference: ")

        if user_choice.isdigit() and 1 <= int(user_choice) <= 6:
            return int(user_choice)
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

    user_preference = get_user_preferences()
    print(f"You chose preference number {user_preference}.")





