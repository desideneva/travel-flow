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
            return int(user_choice)
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

user_preference = get_user_preferences()
print(f"You chose preference number {user_preference}.")

# Function to get user preference for Adventure or Explorer
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
            return user_choice
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
user_preference = get_user_adventure_preference()

# Display countries based on user's preference
selected_countries = display_countries_for_adventure(get_user_adventure_preference)

# Loop for choosing countries until a valid one is entered
while True:
    # Get user's input for the country
    chosen_country = input("Enter the country you want to explore: ")

    # Validate the entered country
    if is_valid_country(chosen_country, selected_countries):
        print(f"You chose {chosen_country}. Let's plan your adventure!")
        break
    else:
        print("This country is not on our destinations list. Please, choose one from the list.")

# Function to get user preference for Cultural
def get_user_cultural_preference():
    """
    Display options for Cultural and get user's choice.
    Returns the user's choice as a string.
    """
    print("Please choose your cultural preference:")
    print("1. In-depth Cultural")
    print("2. Food & Culinary")

    while True:
        user_choice = input("Enter the number of your preference: ")
        if user_choice in ["1", "2"]:
            return user_choice
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
def display_countries_for_cultural(cultural_preference):
    """
    Display the list of countries based on user's cultural preference.
    Returns the list of countries.
    """
    if cultural_preference == "1":
        # Display countries for In-depth Cultural
        in_depth_cultural_countries = ["Japan", "Peru", "Morocco", "India", "Thailand", "Mexico", "Greece", "Italy", "France", "Egypt"]
        print("Here are the countries for In-depth Cultural:")
        print(", ".join(in_depth_cultural_countries))
        return in_depth_cultural_countries
    elif cultural_preference == "2":
        # Display countries for Food & Culinary
        food_culinary_countries = ["Italy", "Japan", "Mexico", "Thailand", "Peru", "Morocco", "Costa Rica", "Canada", "Netherlands", "Vietnam"]
        print("Here are the countries for Food & Culinary:")
        print(", ".join(food_culinary_countries))
        return food_culinary_countries

# Get user's cultural preference
user_cultural_preference = get_user_cultural_preference()

# Display countries based on user's cultural preference
selected_cultural_countries = display_countries_for_cultural(user_cultural_preference)

# Loop for choosing countries until a valid one is entered
while True:
    # Get user's input for the country
    chosen_cultural_country = input("Enter the country you want to explore: ")

    # Validate the entered country
    if is_valid_country(chosen_cultural_country, selected_cultural_countries):
        print(f"You chose {chosen_cultural_country}. Let's explore the cultural richness!")
        break
    else:
        print("This country is not on our destinations list. Please, choose one from the list.")

# Function to get user preference for Active
def get_user_active_preference():
    """
    Display options for Active and get user's choice.
    Returns the user's choice as a string.
    """
    print("Please choose your active preference:")
    print("1. Hiking and Trekking")
    print("2. Skiing")

    while True:
        user_choice = input("Enter the number of your preference: ")
        if user_choice in ["1", "2"]:
            return user_choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Function to display countries based on user's active preference
def display_countries_for_active(active_preference):
    """
    Display the list of countries based on user's active preference.
    Returns the list of countries.
    """
    if active_preference == "1":
        # Display countries for Hiking and Trekking
        hiking_countries = ["Nepal", "Peru", "Morocco", "India", "Italy", "Thailand", "Switzerland", "New Zealand", "Austria", "France"]
        print("Here are the countries for Hiking and Trekking:")
        print(", ".join(hiking_countries))
        return hiking_countries
    elif active_preference == "2":
        # Display countries for Skiing
        skiing_countries = ["Switzerland", "Austria", "Canada", "Italy", "France", "Finland", "Norway", "Sweden", "Japan", "United States"]
        print("Here are the countries for Skiing:")
        print(", ".join(skiing_countries))
        return skiing_countries

# Get user's active preference
user_active_preference = get_user_active_preference()

# Display countries based on user's active preference
selected_active_countries = display_countries_for_active(user_active_preference)

# Loop for choosing countries until a valid one is entered
while True:
    # Get user's input for the country
    chosen_active_country = input("Enter the country you want to explore: ")

    # Validate the entered country
    if is_valid_country(chosen_active_country, selected_active_countries):
        print(f"You chose {chosen_active_country}. Let's plan your active adventure!")
        break
    else:
        print("This country is not on our destinations list. Please, choose one from the list.")




