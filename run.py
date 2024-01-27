import gspread
from google.oauth2.service_account import Credentials
import sys
from colorama import Fore, Style
import time


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


def print_colorful_heading():
    """
    Function to print a colorful heading using colorama.
    """
    heading = "HELLO"

    # Set the color to magenta and bright style
    print(f"{Fore.MAGENTA}{Style.BRIGHT}", end='')

    # Print each character in the heading with a delay
    for char in heading:
        print(char, end='', flush=True)
        time.sleep(0.5)

    # Reset color after printing the heading
    print(Style.RESET_ALL)


# Call the function to print the colorful heading
print_colorful_heading()


def get_user_preferences():
    """
    Function to get user preferences for the type of travel experience.
    Returns:
        int: User preference as a number.
    """
    print(f"{Fore.GREEN}Welcome to {Fore.BLUE}Travel-Flow!{Style.RESET_ALL}")
    print("Let`s help you find your ideal destination.")
    print("What type of travel experience are you looking for?")
    print("1. Adventure\n"
          "2. Cultural\n"
          "3. Active\n"
          "4. Relaxing\n"
          "5. Family\n"
          "6. Solo")

    while True:
        try:
            user_choice = input("Enter your preference number: ")

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
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue


def get_user_adventure_preference():
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
            display_countries_for_adventure(user_choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")


# Function to display countries based on user's preference
def display_countries_for_adventure(user_preference):
    """
    Display the list of countries based on user's preference.
    Returns the list of countries.
    """
    if user_preference == "1":
        # Display countries for Adventure
        countries_list = destinations_worksheet.col_values(3)[1:]
        print("Here are the top 10 countries for Adventurers:")
        for country in countries_list:
            print(country)
        handle_country_selection(countries_list)

    elif user_preference == "2":
        # Display countries for Explorer
        countries_list = destinations_worksheet.col_values(7)[1:]
        print("Here are the top 10 countries for Explorers:")
        for country in countries_list:
            print(country)
        handle_country_selection(countries_list)


def get_user_cultural_preference():
    """
    Display options for Cultural and get user's choice.
    Returns the user's choice as a string.
    """
    print("Please choose your cultural preference:")
    print("1. In-depth Cultural")
    print("2. Food & Culinary")

    while True:
        user_preference = input("Enter the number of your preference: ")
        if user_preference in ["1", "2"]:
            display_countries_for_cultural(user_preference)
        else:
            print("Invalid choice. Please enter 1 or 2.")


def display_countries_for_cultural(user_preference):
    """
    Display the list of countries based on user's cultural preference.
    Returns the list of countries.
    """
    if user_preference == "1":
        # Display countries for In-depth Cultural
        countries_list = destinations_worksheet.col_values(5)[1:]
        print("Here are the top 10 countries\n"
              "for In-depth Cultural experience:")
        for country in countries_list:
            print(country)
        handle_country_selection(countries_list)
    elif user_preference == "2":
        # Display countries for Food & Culinary
        countries_list = destinations_worksheet.col_values(6)[1:]
        print("Here are the top 10 countries for Food & Culinary experience:")
        for country in countries_list:
            print(country)
        handle_country_selection(countries_list)


def get_user_active_preference():
    """
    Prompt the user to choose their preference for active experiences.
    """
    print("Please choose your active preference:")
    print("1. Hiking and Trekking")
    print("2. Skiing")

    while True:
        user_choice = input("Enter the number of your preference: ")
        if user_choice in ["1", "2"]:
            display_countries_for_active(user_choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")


def display_countries_for_active(user_preference):
    """
    Display the list of countries for Hiking and Trekking
    or Skiing based on user's preference.
    Args:
        active_preference (str): The user's preference for active experiences.
    """
    if user_preference == "1":
        # Display countries for Hiking and Trekking
        countries_list = destinations_worksheet.col_values(4)[1:]
        print("Here are the top 10 countries for Hiking and Trekking:")
        for country in countries_list:
            print(country)
        handle_country_selection(countries_list)
    elif user_preference == "2":
        # Display countries for Skiing
        countries_list = destinations_worksheet.col_values(9)[1:]
        print("Here are the top 10 countries for Skiing:")
        for country in countries_list:
            print(country)
        handle_country_selection(countries_list)


def get_user_relaxing_preference():
    """
    Function to prompt the user to choose their relaxing preference.
    """
    print("Please choose your relaxing preference.")
    display_countries_for_relaxing("4")


def display_countries_for_relaxing(relaxing_preference):
    """
    Display the list of countries for Health, Spa & Wellbeing.
    Args:
        relaxing_preference (str): The user's relaxing preference.
    """
    # Retrieve the countries from the corresponding column in the spreadsheet
    countries_list = destinations_worksheet.col_values(8)[1:]
    print("Here are the countries for Health, Spa & Wellbeing:")
    for country in countries_list:
        print(country)
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
    # Retrieve the countries from the corresponding column in the spreadsheet
    countries_list = destinations_worksheet.col_values(10)[1:]
    print("Here are the countries families prefer to visit:")
    for country in countries_list:
        print(country)
    handle_country_selection(countries_list)


def get_user_solo_preference():
    """
    Prompts the user to choose their solo travel preference.
    """
    print("Please choose your solo preference.")
    display_countries_for_solo("6")


def display_countries_for_solo(solo_preference):
    """
    Prompts user for solo travel preference and displays country list.
    """
    # Retrieve the countries from the corresponding column in the spreadsheet
    countries_list = destinations_worksheet.col_values(11)[1:]
    print("Here are the most popular countries for solo travellers:")
    for country in countries_list:
        print(country)
    handle_country_selection(countries_list)


def handle_country_selection(selected_countries):
    """
    Function to handle the user's selection of a country.
    Keeps prompting the user to enter a valid country from the provided list.
    Restarts the program if a valid country is chosen;
    otherwise, asks for a new selection.
    """
    while True:
        # Get user's input for the country
        chosen_country = input("Enter the country you want to explore: ")
        # Validate the entered country
        if is_valid_country(chosen_country, selected_countries):
            print(f"You chose {chosen_country}.\n"
                  "Let's plan your unforgettable journey!")
            restart()
        else:
            print("This country is not on our destinations list.\n"
                  "Please, choose one from the list.")


# Function to check if the entered country is in the list
def is_valid_country(country, countries_list):
    """
    Check if the entered country is in the list of countries.
    Returns True if valid, False otherwise.
    """
    return country in countries_list


def restart():
    """
    Function to prompt the user if they want to start the program again.
    Accepts 'yes' to restart the program or 'no' to exit.
    """
    while True:
        choice = input("Do you want to start again? yes / no\n ")

        if choice in ["yes", "no"]:
            if choice == "yes":
                get_user_preferences()
            elif choice == "no":
                print("Thank you for using Travel-Flow! Have a great day!")
                sys.exit()
        else:
            print("Invalid option. Type yes or no")


get_user_preferences()
