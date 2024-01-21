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

# In run.py

# Function to get user preference for Adventure or Explorer
def get_user_preference():
    """
    Display options for Adventure and Explorer and get user's choice.
    Returns the user's choice as a string.
    """
    print("Please choose your preference:")
    print("1. Adventure")
    print("2. Explorer")

    while True:
        user_choice = input("Enter the number of your preference: ")
        if user_choice in ["1", "2"]:
            return user_choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Function to display countries based on user's preference
def display_countries(user_preference):
    """
    Display the list of countries based on user's preference.
    Returns the list of countries.
    """
    if user_preference == "1":
        # Display countries for Adventure
        adventure_countries = ["New Zealand", "Nepal", "Canada", "Australia", "Costa Rica", "Norway", "Sri Lanka", "Chile", "Bali", "South Africa"]
        print("Here are the countries for Adventure:")
        print(", ".join(adventure_countries))
        return adventure_countries
    elif user_preference == "2":
        # Display countries for Explorer
        explorer_countries = ["Mongolia", "Papua New Guinea", "Bhutan", "Ethiopia", "Madagascar", "Suriname", "Guyana", "Namibia", "Kyrgyzstan", "Laos"]
        print("Here are the countries for Explorer:")
        print(", ".join(explorer_countries))
        return explorer_countries

# Function to check if the entered country is in the list
def is_valid_country(country, countries_list):
    """
    Check if the entered country is in the list of countries.
    Returns True if valid, False otherwise.
    """
    return country in countries_list

# Get user's preference
user_preference = get_user_preference()

# Display countries based on user's preference
selected_countries = display_countries(user_preference)

# Get user's input for the country
chosen_country = input("Enter the country you want to explore: ")

# Validate the entered country
if is_valid_country(chosen_country, selected_countries):
    print(f"You chose {chosen_country}. Let's plan your adventure!")
else:
    print("This country is not on our destinations list. Please, choose one from the list.")






