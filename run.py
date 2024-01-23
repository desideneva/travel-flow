import gspread
from google.oauth2.service_account import Credentials
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('travel_flow')
destinations_worksheet = SHEET.worksheet("destinations")

destinations_countries_list = destinations_worksheet.col_values(2)[2:]

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
            if int(user_choice) == 1:
                get_user_adventure_preference()
            elif int(user_choice) == 2:
                get_user_cultural_preference()
            elif int(user_choice) == 3:
                get_user_active_preference()
            elif int(user_choice) == 4:
                get_user_relaxing_preference()
            elif int(user_choice) == 5:
                get_user_family_preference()
            elif int(user_choice) == 6:
                get_user_solo_preference()
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

def get_user_adventure_preference():
    print("Please choose your preference:")
    print("1. Adventure")
    print("2. Explorer")

    while True:
        user_choice = input("Enter the number of your preference: ")
        if user_choice in ["1", "2"]:
            display_countries_for_adventure(user_choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")
# Function to display countries based on user's preference
def display_countries_for_adventure(get_user_adventure_preference):
    """
    Display the list of countries based on user's preference.
    Returns the list of countries.
    """
    if user_preference == "1":
        # Display countries for Adventure
        adventure_countries = ["New Zealand", "Nepal", "Canada", "Australia", "Costa Rica", "Norway", "Sri Lanka", "Chile", "Bali", "South Africa"]
        print("Here are the countries for Adventure:")
        print(", ".join(adventure_countries))
        handle_country_selection(countries_list)

    elif user_preference == "2":
        # Display countries for Explorer
        explorer_countries = ["Mongolia", "Papua New Guinea", "Bhutan", "Ethiopia", "Madagascar", "Suriname", "Guyana", "Namibia", "Kyrgyzstan", "Laos"]
        print("Here are the countries for Explorer:")
        print(", ".join(explorer_countries))
        handle_country_selection(countries_list)            

def get_user_cultural_preference():
    print("Please choose your cultural preference:")
    print("1. In-depth Cultural")
    print("2. Food & Culinary")

    while True:
        user_preference = input("Enter the number of your preference: ")
        if user_preference in ["1", "2"]:
            display_countries_for_cultural(user_preference)
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
def display_countries_for_cultural(cultural_preference):
    countries_list = destinations_worksheet.col_values(int(cultural_preference) + 1)[1:]
    print(f"Here are the countries for In-depth Cultural:")
    print(", ".join(countries_list))
    handle_country_selection(countries_list)


def get_user_active_preference():
    print("Please choose your active preference:")
    print("1. Hiking and Trekking")
    print("2. Skiing")

    while True:
        user_choice = input("Enter the number of your preference: ")
        if user_choice in ["1", "2"]:
            display_countries_for_active(user_choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")

def display_countries_for_active(active_preference):
    countries_list = destinations_worksheet.col_values(int(active_preference) + 1)[1:]
    print(f"Here are the countries for Hiking and Trekking/Skiing:")
    print(", ".join(countries_list))
    handle_country_selection(countries_list)

def get_user_relaxing_preference():
    """
    Function to prompt the user to choose their relaxing preference.
    """
    print("Please choose your relaxing preference.")
    display_countries_for_relaxing("4")

def display_countries_for_relaxing(relaxing_preference):
    """
    Display the list of countries for Health, Spa & Wellbeing based on user's preference.
    Args:
        relaxing_preference (str): The user's relaxing preference.
    """
    # Retrieve the list of countries from the corresponding column in the spreadsheet
    countries_list = destinations_worksheet.col_values(8)[1:]
    print(f"Here are the countries for Health, Spa & Wellbeing:")
    print(", ".join(countries_list))
    handle_country_selection(countries_list)

def get_user_family_preference():
    """
    Function to prompt the user to choose their family preference.
    """
    print("Please choose your family preference.")
    display_countries_for_family("5")

def display_countries_for_family(family_preference):
    """
    Display the list of countries for Family based on user's preference.
    Args:
        family_preference (str): The user's family preference.
    """
    # Retrieve the list of countries from the corresponding column in the spreadsheet
    countries_list = destinations_worksheet.col_values(10)[1:]
    print(f"Here are the countries families prefer to visit:")
    print(", ".join(countries_list))
    handle_country_selection(countries_list)

def handle_country_selection(selected_countries):
    while True: 
            # Get user's input for the country
            chosen_country = input("Enter the country you want to explore: ")
            # Validate the entered country
            if is_valid_country(chosen_country, selected_countries):
                print(f"You chose {chosen_country}. Let's plan your unforgettable journey!")
                restart()
            else:
                print("This country is not on our destinations list. Please, choose one from the list.")

# Function to check if the entered country is in the list
def is_valid_country(country, countries_list):
    """
    Check if the entered country is in the list of countries.
    Returns True if valid, False otherwise.
    """
    return country in countries_list

def restart():
    while True:
        choice = input("Do you want to start again? yes / no\n ")

        if choice in ["yes", "no"]:
            if choice == "yes":
                get_user_preferences()
            elif choice == "no":
                sys.exit()
        else:
            print("Invalid option. Type yes or no")

get_user_preferences()

         

 


 








 

