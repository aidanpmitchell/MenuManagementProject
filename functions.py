
def print_main_menu(the_menu):
    """
    Prints the main menu options in a formatted and decorative way.

    This function displays the main menu for the user to interact with. It formats the keys 
    and values of the provided dictionary as options, and includes decorative separators 
    before and after the menu. The function also prompts the user with the question: 
    "What would you like to do?"

    Args:
        the_menu (dict): A dictionary where the keys represent menu option numbers or codes, 
                         and the values are descriptions of the corresponding actions.

    Returns:
        None: This function only prints output to the console and does not return anything.
    """
    print("==========================")
    print("What would you like to do?")
    for key, option in the_menu.items():
        print(f"{key} - {option}")
    print("==========================")


def list_helper(list_menu, restaurant_menu_list, spicy_scale_map):
    """
    Displays all menu items or only vegetarian items based on the user's selection.

    This function prompts the user to choose between displaying all dishes or only vegetarian dishes
    from the restaurant's menu. It calls the `print_restaurant_menu()` function to handle the display.

    Args:
        list_menu (list): A list containing menu options (e.g., ["A - All items", "V - Vegetarian only"]).
        restaurant_menu_list (list): A list of dictionaries where each dictionary represents a dish in the menu.
        spicy_scale_map (dict): A dictionary that maps integer spiciness levels to their string descriptions.

    Returns:
        None: The function does not return anything. It prints the selected menu items to the console.
    
    Helper Functions:
        print_restaurant_menu: A function that prints the restaurant menu to the console.

    Behavior:
        - If the restaurant menu is empty, a warning message is displayed.
        - If the user selects option 'A', all items from the menu are displayed.
        - If the user selects option 'V', only vegetarian items are displayed.
    """
    if len(restaurant_menu_list) == 0:
        print("WARNING: There is nothing to display!")

        input("::: Press Enter to continue")
    else:
        subopt = get_selection("List", list_menu)
        if subopt == 'A':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1)
        elif subopt == 'V':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1,
                                  vegetarian_only=True)


def get_selection(action, suboptions, to_upper=True, go_back=False):
    """
    Prompts the user to select an option from a submenu and returns the selection.

    This function displays a submenu based on the provided `suboptions` dictionary and 
    prompts the user to select an option. It validates the selection by checking if it 
    matches one of the available keys in `suboptions`. If an invalid option is provided, 
    the menu is reprinted, and the user is asked to make a valid choice. Optionally, 
    the user's input can be converted to uppercase and a "Go back to main menu" option can 
    be enabled.

    Args:
        action (str): The action the user is performing (e.g., "edit", "delete"), which 
                      will be printed in the prompt message.
        suboptions (dict): A dictionary where the keys are submenu option identifiers, 
                           and the values are descriptions of those options.
        to_upper (bool, optional): If True (default), the user's selection will be 
                                   automatically converted to uppercase. If False, the 
                                   input will be used as-is.
        go_back (bool, optional): If True, an additional option "M" is provided to allow 
                                  the user to return to the main menu. Defaults to False.

    Returns:
        str: The key corresponding to the user's selection (usually an uppercase string, 
             unless `to_upper` is set to False). If `go_back` is True and the user selects 
             "M", it will return "M" to indicate returning to the main menu.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What field would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper()
        if go_back and selection.upper() == 'M':
            return 'M'

    print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection


def print_restaurant_menu(restaurant_menu, spicy_scale_map, name_only=False,
                          show_idx=True, start_idx=0, vegetarian_only=False):
    """
    Prints the restaurant menu with optional filters and formatting.

    This function displays a list of dishes from the restaurant menu. It can optionally show 
    only the names of the dishes, display dish indices, and filter the output to show only 
    vegetarian items. The function also formats and displays additional information about 
    each dish, including calories, price, vegetarian status, and spiciness level.

    Args:
        restaurant_menu (list): A list of dictionaries where each dictionary represents a dish, 
                                with keys such as "name", "calories", "price", "is_vegetarian", 
                                and "spicy_level".
        spicy_scale_map (dict): A dictionary that maps integer spiciness levels to their 
                                corresponding string descriptions (e.g., {1: "Mild", 4: "Very Spicy"}).
        name_only (bool, optional): If True, only the name of the dish is printed. If False (default), 
                                    additional information about each dish is also printed.
        show_idx (bool, optional): If True (default), the index of each dish is printed before 
                                   its name. If False, no index is shown.
        start_idx (int, optional): The starting index for dish numbering if `show_idx` is True. 
                                   Defaults to 0.
        vegetarian_only (bool, optional): If True, only dishes with "is_vegetarian" set to "yes" 
                                          are printed. If False (default), all dishes are printed.

    Returns:
        None: This function prints the restaurant menu to the console and does not return a value.

    """
    idx = start_idx
    print("------------------------------------------")
    for dish in restaurant_menu:
        if vegetarian_only and dish["is_vegetarian"].lower() != "yes":
            continue

        if show_idx:
            print(f"{idx}. ", end="")

        print(dish["name"].upper())
        if not name_only:
            print(f"* Calories: {dish['calories']}")
            print(f"* Price: {dish['price']:.1f}")
            print(f"* Is it vegetarian: {dish['is_vegetarian']}")
            print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
            print()

        idx += 1

    print('------------------------------------------')


def is_num(val):
    """
    Checks whether the given value is a valid numeric string.

    This function verifies if the input `val` is a string that represents a valid 
    integer or float. If `val` is not a string, the function immediately returns False. 
    If `val` is a string, the function attempts to convert it to a float. If the conversion 
    succeeds, it returns True, indicating that the string represents a valid number 
    (either integer or float). If the conversion fails, it returns False.

    Args:
        val (str): The value to check if it represents a valid numeric string.

    Returns:
        bool: 
            - True if `val` is a string that can be converted to a valid integer or float.
            - False if `val` is not a string or cannot be converted to a valid number.
    """
    if isinstance(val, str):
        try:
            float(val)
            return True
        except ValueError:
            return False
        except TypeError:
            return False
    else:
        return False


def is_valid_name(name_str):
    """
    Checks if the provided name string is valid based on its length.

    This function validates whether the input `name_str` is a string containing between 
    3 and 25 characters, inclusive. If the input meets the criteria, it returns True. 
    Otherwise, it returns False.

    Args:
        name_str (str): The input string to be validated.

    Returns:
        bool:
            - True if `name_str` is a string with a length between 3 and 25 characters (inclusive).
            - False otherwise (if `name_str` is not a string or does not meet the length requirements).

    """
    if type(name_str) == str and len(name_str) in range(3, 26):
        return True
    else:
        return False


def is_valid_spicy_level(spicy_level_str, spicy_scale_map):
    """
    Validates whether the provided spiciness level string corresponds to a valid spiciness level.

    This function checks if `spicy_level_str` is a string representation of an integer that maps 
    to a valid spiciness level in the `spicy_scale_map` dictionary. The `spicy_scale_map` is a 
    dictionary where keys are integers representing spiciness levels and values are their descriptions 
    (e.g., {1: "Mild", 2: "Medium", 3: "Hot"}). If the spiciness level string is valid, the function 
    returns True, otherwise False.

    Args:
        spicy_level_str (str): A string expected to represent an integer spiciness level.
        spicy_scale_map (dict): A dictionary mapping integer spiciness levels to their corresponding 
                                descriptions (e.g., {1: "Non Spicy", 4: "Very Spicy"}).

    Returns:
        bool:
            - True if `spicy_level_str` is a string that can be converted to an integer and that integer 
              is a key in `spicy_scale_map`.
            - False if `spicy_level_str` is not a valid spiciness level or if the conversion to an integer fails.
    """
    if type(spicy_level_str) == str:
        try:
            spicy_level_str = int(spicy_level_str)
            if spicy_level_str in spicy_scale_map:
                return True
            else:
                return False

        except ValueError:
            return False
        except TypeError:
            return False
    else:
        return False


def is_valid_is_vegetarian(vegetarian_str):
    """
    Validates if the input string indicates whether a dish is vegetarian.

    This function checks if the provided `vegetarian_str` is a valid string representing 
    whether a dish is vegetarian. The valid inputs are case-insensitive "yes" or "no". 
    If the input is valid, the function returns True. Otherwise, it returns False.

    Args:
        vegetarian_str (str): A string that should contain either "yes" or "no", 
                              indicating whether a dish is vegetarian.

    Returns:
        bool:
            - True if `vegetarian_str` is a string and its value is "yes" or "no" 
              (case-insensitive).
            - False if `vegetarian_str` is not a string or does not contain a valid value.
    """
    if type(vegetarian_str) == str:
        if vegetarian_str.lower() == "yes" or vegetarian_str.lower() == "no":
            return True
        else:
            return False
    else:
        return False


def is_valid_price(price_str):
    """
    Validates whether the input string represents a valid price.

    This function checks if the provided `price_str` is a string that contains a valid 
    decimal number, which represents a price. The function relies on `is_num()` to 
    verify if the string can be converted to a valid number (either integer or float).

    Args:
        price_str (str): A string that is expected to contain a valid decimal number 
                         representing the price of an item.

    Returns:
        bool:
            - True if `price_str` is a valid numeric string that represents a price.
            - False if `price_str` is not a valid number or cannot be converted to a number.
    """

    if is_num(price_str):
        return True
    else:
        return False


def is_valid_calories(calories_str):
    """
    Validates whether the input string represents a valid integer for calories.

    This function checks if the provided `calories_str` is a string that can be converted 
    to an integer, representing the number of calories. If the string can be successfully 
    converted to an integer, the function returns True. Otherwise, it returns False.

    Args:
        calories_str (str): A string that is expected to represent a valid integer value for calories.

    Returns:
        bool:
            - True if `calories_str` is a valid string containing an integer value.
            - False if `calories_str` cannot be converted to an integer or is not a string.

    """
    if type(calories_str) == str:
        try:
            int(calories_str)
            return True
        except ValueError:
            return False
        except TypeError:
            return False
    else:
        return False


def get_new_menu_dish(dish_list, spicy_scale_map):
    """
    Validates the elements of a dish list and returns a dictionary of the validated dish fields.

    This function validates each element in the `dish_list` sequentially, from the "name" to the 
    "spicy_level" field. If any element fails validation, the function returns a tuple containing 
    the name of the failed parameter and the corresponding value that caused the failure. If all 
    validations pass, the function constructs and returns a dictionary with the dish fields properly 
    set.

    Args:
        dish_list (list): A list containing 5 elements representing the dish fields in the following order:
                          [name, calories, price, is_vegetarian, spicy_level].
        spicy_scale_map (dict): A dictionary that maps integer spiciness levels to descriptions, 
                                used to validate the "spicy_level" field.

    Returns:
        dict or tuple:
            - A dictionary with the validated dish fields if all validations pass:
              {
                  "name": name,
                  "calories": calories,
                  "price": price,
                  "is_vegetarian": is_vegetarian,
                  "spicy_level": spicy_level
              }
            - A tuple (field_name, invalid_value) if a validation fails, indicating which field is invalid 
              and the corresponding value that failed validation.

    Validation Rules:
        - "name": Must be a string between 3 and 25 characters.
        - "calories": Must be a string representing an integer value.
        - "price": Must be a string representing a valid decimal number.
        - "is_vegetarian": Must be a string of "yes" or "no".
        - "spicy_level": Must be a string representing an integer value that maps to a key in `spicy_scale_map`.
    """

    if len(dish_list) == 5:
        if is_valid_name(dish_list[0]):
            name = dish_list[0]
            if is_valid_calories(dish_list[1]):
                calories = float(dish_list[1])
                if is_valid_price(dish_list[2]):
                    price = round(float(dish_list[2]), 2)
                    if is_valid_is_vegetarian(dish_list[3]):
                        is_vegetarian = dish_list[3]
                        if is_valid_spicy_level(dish_list[4], spicy_scale_map):
                            spicy_level = int(dish_list[4])
                        else:
                            return "spicy_level", dish_list[4]
                    else:
                        return "is_vegetarian", dish_list[3]
                else:
                    return "price", float(dish_list[2])
            else:
                return "calories", dish_list[1]
        else:
            return "name", dish_list[0]
    else:
        return len(dish_list)

    return {"name": name, "calories": calories, "price": price, "is_vegetarian": is_vegetarian,
            "spicy_level": spicy_level}


def print_dish(dish, spicy_scale_map, name_only=False):
    """
    Prints the details of a dish, optionally displaying only the name.

    This function displays the details of a dish from the provided `dish` dictionary. 
    It prints the dish name, calories, price, vegetarian status, and spiciness level 
    based on the `spicy_scale_map`. If `name_only` is set to True, only the dish name 
    is printed. Otherwise, it prints the full details of the dish.

    Args:
        dish (dict): A dictionary representing the dish, expected to contain the following keys:
            - "name" (str): The name of the dish.
            - "calories" (int or float): The calorie count for the dish.
            - "price" (float): The price of the dish.
            - "is_vegetarian" (str): A string indicating whether the dish is vegetarian 
              ("yes" or "no").
            - "spicy_level" (int): An integer representing the spiciness level of the dish, 
              which corresponds to a key in the `spicy_scale_map`.
        
        spicy_scale_map (dict): A dictionary mapping integer spiciness levels to string 
                                descriptions (e.g., {1: "Mild", 2: "Medium", 3: "Hot"}).
        
        name_only (bool, optional): If True, only the name of the dish is printed. 
                                    Defaults to False.

    Returns:
        None: This function prints the dish information and does not return a value.
    """

    name = dish["name"]
    calories = dish["calories"]
    price = dish["price"]
    is_vegetarian = dish["is_vegetarian"]
    spicy_level = spicy_scale_map[dish["spicy_level"]]

    if name_only:
        print(name.upper())
    else:
        print(name.upper())
        print(f"* Calories: {calories}")
        print(f"* Price: {price}")
        print(f"* Is it vegetarian: {is_vegetarian}")
        print(f"* Spicy level: {spicy_level}")
        print()


def add_helper(restaurant_menu_list, spicy_scale_map):
    """
    Allows the user to add a new dish to the restaurant menu, validating input fields.

    This function prompts the user to input details for a new dish (name, calories, price, 
    vegetarian status, and spicy level). It validates the input by calling `get_new_menu_dish()`. 
    If the input is valid, the new dish is appended to the `restaurant_menu_list`, and the dish 
    details are printed. If the input is invalid, an appropriate error message is shown. 
    The function will continue prompting the user to add more dishes until they choose to stop.

    Args:
        restaurant_menu_list (list): A list of dictionaries where each dictionary represents a dish 
                                     in the restaurant menu.
        spicy_scale_map (dict): A dictionary mapping integer spiciness levels to string descriptions 
                                (e.g., {1: "Mild", 2: "Medium", 3: "Hot"}), used to validate and 
                                describe the spiciness level of the dish.

    Returns:
        None: This function does not return a value. It updates `restaurant_menu_list` in place.

    Helper Functions:
        - get_new_menu_dish(): Validates and constructs a dish dictionary from user input.
        - print_dish(): Prints the details of the newly added dish.
    """
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter each required field, separated by commas.")
        print("::: name of the dish, calories, price, is it vegetarian ( yes | no ), spicy_level ( 1-4 )")
        dish_data = input("> ")
        dish_values = dish_data.split(",")
        result_dict = get_new_menu_dish(dish_values, spicy_scale_map)
        if type(result_dict) == dict:
            restaurant_menu_list.append(result_dict)
            print(f"Successfully added a new dish!")
            print_dish(result_dict, spicy_scale_map)
        elif type(result_dict) == int:
            print(f"WARNING: invalid number of fields!")
            print(f"You provided {result_dict}, instead of the expected 5.\n")
        else:
            print(f"WARNING: invalid dish field: {result_dict}\n")

        print("::: Would you like to add another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()


def is_valid_index(in_list, idx, start_idx=0):
    """
    Validates whether a string index is a valid index for the given list.

    This function checks if the provided `idx` is a string representing a positive integer 
    index that can access an element in `in_list`. It optionally adjusts the index by 
    subtracting `start_idx` to support non-zero-based indexing. If `idx` is a valid index, 
    the function returns True; otherwise, it returns False.

    Args:
        idx (str): A string that should contain a numeric index to validate.
        in_list (list): The list that `idx` will index.
        start_idx (int, optional): The starting value for indexing (default is 0). This value 
                                   is subtracted from `idx` for zero-based indexing.

    Returns:
        bool:
            - True if `idx` is a valid numeric string representing an index within the bounds 
              of `in_list` after adjusting for `start_idx`.
            - False if `idx` is not a valid integer string, is negative, or exceeds the list's length.
    """
    if type(idx) == str:
        if not idx.isdigit():
            return False
        else:
            idx = int(idx)

        new_idx = int(idx) - start_idx

        if 0 <= new_idx < len(in_list):
            return True
        else:
            return False
    else:
        return False


def delete_dish(in_list, idx, start_idx=0):
    """
    Deletes a dish from the list at the specified index and returns the deleted dish.

    This function removes a dish from `in_list` at the position specified by `idx`. It first checks 
    if the list is empty, then verifies if `idx` is a valid index using the `is_valid_index()` function. 
    If the index is valid, the dish is removed from the list and returned. The function also supports 
    non-zero-based indexing via the `start_idx` parameter.

    Args:
        in_list (list): The list of dishes from which an item will be removed.
        idx (str): A string representing the index of the dish to remove. The index is validated using 
                   `is_valid_index()`.
        start_idx (int, optional): An integer representing the starting value for indexing (default is 0). 
                                   This value is subtracted from `idx` to allow for zero-based indexing.

    Returns:
        - If `in_list` is empty, returns 0.
        - If `idx` is not a string, returns None.
        - If `is_valid_index()` returns False, returns -1.
        - Otherwise, returns the dish that was removed from `in_list`.

    Helper Functions:
        - is_valid_index(): Checks if the provided `idx` is a valid index for `in_list`.
    """
    if not in_list:
        return 0
    elif type(idx) != str:
        return None
    elif not is_valid_index(in_list, idx, start_idx):
        return -1

    return in_list.pop(int(idx) - int(start_idx))


def delete_helper(restaurant_menu_list, spicy_scale_map):
    """
    Allows the user to delete a dish or the entire menu from the restaurant menu.

    This function provides an interface for deleting dishes from the `restaurant_menu_list`. 
    It prompts the user to either delete a specific dish or delete the entire menu. If the input 
    list is empty, a warning is displayed and no deletion occurs. If a dish index is provided 
    and is valid, the dish is removed from the list. If the entire menu is deleted, the list is 
    cleared. The user can continue deleting dishes until they choose to stop.

    Args:
        restaurant_menu_list (list): A list of dictionaries where each dictionary represents 
                                     a dish in the restaurant menu.
        spicy_scale_map (dict): A dictionary mapping integer spiciness levels to string 
                                descriptions (e.g., {1: "Mild", 2: "Medium", 3: "Hot"}), 
                                used when printing the menu.

    Returns:
        list: The updated `restaurant_menu_list` after any deletions have been made.

    Edge Cases:
        - If the menu is empty, the function prints: "WARNING: There is nothing to delete!"
        - If an invalid index is provided, it prints: "WARNING: |{user_option}| is an invalid dish number!"
        - If the user cancels the deletion process, no changes are made to the menu.

    Helper Functions:
        - print_restaurant_menu(): Prints the list of dishes for the user to select from.
        - delete_dish(): Validates the user's input and deletes the specified dish.
    """
    continue_action = 'y'
    while continue_action == 'y':
        if not restaurant_menu_list:
            print("WARNING: There is nothing to delete!")
            break
        print("Which dish would you like to delete?")
        print("Press A to delete the entire menu for this restaurant, M to cancel this operation")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
        user_option = input("> ")
        if user_option == "A" or user_option == "a":
            print(f"::: WARNING! Are you sure you want to delete the entire menu ?")
            print("::: Type Yes to continue the deletion.")
            user_option = input("> ")
            if user_option == "Yes":
                restaurant_menu_list = []
                print(f"Deleted the entire menu.")
            else:
                print(f"You entered '{...}' instead of Yes.")
                print("Canceling the deletion of the entire menu.")
            break
        elif user_option == 'M' or user_option == 'm':
            break
        result = delete_dish(restaurant_menu_list, user_option, 1)
        if type(result) == dict:
            print("Success!")
            print(f"Deleted the dish |{result['name']}|")
        elif result == 0:  # delete_item() returned an error
            print("WARNING: There is nothing to delete.")
        elif result == -1:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid dish number!")

        print("::: Would you like to delete another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
    return restaurant_menu_list


def save_menu_to_csv(restaurant_menu_list, filename):
    """
    Saves the restaurant menu to a CSV file.

    This function writes the details of each dish in the `restaurant_menu_list` to a CSV file 
    specified by `filename`. The file will be created if it doesn't exist, and overwritten if it does. 
    Each dish is expected to be a dictionary with the following keys: "name", "calories", "price", 
    "is_vegetarian", and "spicy_level". The CSV file will contain these values for each dish in order.

    Args:
        restaurant_menu_list (list of dict): A list of dictionaries where each dictionary represents 
                                             a dish in the restaurant menu, containing the following keys:
                                             - "name" (str): The name of the dish.
                                             - "calories" (int or float): The calorie count for the dish.
                                             - "price" (float): The price of the dish.
                                             - "is_vegetarian" (str): A string ("yes" or "no") indicating 
                                               whether the dish is vegetarian.
                                             - "spicy_level" (int): The spiciness level of the dish.
        
        filename (str): The name of the CSV file to save the menu to. Must end with ".csv".

    Returns:
        int:
            - Returns -1 if the `filename` does not end with ".csv".

    Notes:
        - The function requires `csv` and `os` modules.
        - The file is opened with the 'w' (write) mode, so any existing content in the file will be overwritten.
        - The data is written as strings, with each dictionary entry's values converted to strings before writing.
    """
    import csv

    if not filename.endswith('.csv'):
        return -1

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for dish in restaurant_menu_list:
            string_list = [dish['name'], dish['calories'], dish['price'], dish['is_vegetarian'], dish['spicy_level']]
            csv_writer.writerow(string_list)


def save_helper(restaurant_menu_list):
    """
    Prompts the user to save the restaurant menu to a CSV file.

    This function repeatedly asks the user to enter a valid filename for saving the `restaurant_menu_list` 
    to a CSV file. If the filename does not end with '.csv', a warning is displayed, and the user is given 
    the option to try again. Once a valid filename is provided, the menu is saved using the `save_menu_to_csv()` 
    function.

    Args:
        restaurant_menu_list (list): A list of dictionaries where each dictionary represents a dish in the 
                                     restaurant menu, containing the following keys:
                                     - "name" (str): The name of the dish.
                                     - "calories" (int or float): The calorie count for the dish.
                                     - "price" (float): The price of the dish.
                                     - "is_vegetarian" (str): A string ("yes" or "no") indicating 
                                       whether the dish is vegetarian.
                                     - "spicy_level" (int): The spiciness level of the dish.

    Returns:
        None: This function does not return any value. It saves the menu to a file or prompts the user for a valid filename.

    Helper Functions:
        - save_menu_to_csv(): Saves the restaurant menu to a CSV file.
    """
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = save_menu_to_csv(restaurant_menu_list, filename)
        if result == -1:
            print(f"WARNING: |{...}| is an invalid file name!")
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            break


def load_menu_from_csv(filename, restaurant_menu_list, spicy_scale_map):
    """
    Loads the restaurant menu from a CSV file and appends valid dishes to the menu list.

    This function reads the contents of the CSV file specified by `filename` and attempts to 
    append each valid dish to `restaurant_menu_list`. The file is expected to contain dish 
    data in the form of rows, where each row corresponds to a dish. The dish data is validated 
    using the `get_new_menu_dish()` function. Any invalid rows are tracked by their 1-based 
    row index and returned as a list. The function does not clear any existing dishes in 
    `restaurant_menu_list`.

    Args:
        filename (str): The name of the CSV file from which to read the menu data. 
                        The file must have a '.csv' extension.
        restaurant_menu_list (list): A list of dictionaries representing the current restaurant 
                                     menu. The function appends valid dishes from the file to this list.
        spicy_scale_map (dict): A dictionary mapping integer spiciness levels to string 
                                descriptions (e.g., {1: "Mild", 2: "Medium", 3: "Hot"}). 
                                This is required for validating the spiciness level in each dish.

    Returns:
        int:
            - Returns -1 if the filename does not end with '.csv'.
            - Returns None if the file does not exist.
        list:
            - Returns an empty list if the entire file is read successfully and all rows are valid.
            - Returns a list of 1-based indices indicating the rows that contain invalid data.

    Notes:
        - The function requires the `csv` and `os` modules.
        - If the filename does not end with '.csv', the function will return -1.
        - If the file does not exist, the function will return None.
        - The `get_new_menu_dish()` function is used to validate and construct dish objects from the CSV rows.

    Helper Functions:
        - get_new_menu_dish(): Validates each dish and constructs a dictionary representing the dish if valid.
    """
    import csv
    import os

    if not filename.endswith('.csv'):
        return -1

    if not os.path.exists(filename):
        return None

    invalid_rows = []

    with open(filename, 'r') as f:
        menu_reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(menu_reader, start=1):
            dish = get_new_menu_dish(row, spicy_scale_map)
            if isinstance(dish, dict):
                restaurant_menu_list.append(dish)
            else:
                invalid_rows.append(i)

    return invalid_rows


def load_helper(restaurant_menu_list, spicy_scale_map):
    """
    Prompts the user to load a restaurant menu from a CSV file.

    This function asks the user to input the name of a CSV file. It attempts to load the menu from the file 
    using the `load_menu_from_csv()` function, which validates the filename and appends the contents 
    to the existing `restaurant_menu_list`. If the filename is invalid or the file does not exist, 
    the user is prompted to try again.

    Args:
        restaurant_menu_list (list): A list of dictionaries where each dictionary represents a dish 
                                     in the restaurant menu. New dishes from the CSV file are appended 
                                     to this list.
        spicy_scale_map (dict): A dictionary mapping integer spiciness levels to string descriptions 
                                (e.g., {1: "Mild", 2: "Medium", 3: "Hot"}), used when validating the 
                                spiciness level of dishes in the file.

    Returns:
        None: This function does not return any value. It updates the `restaurant_menu_list` with 
              the loaded dishes from the CSV file if valid.

    Helper Functions:
        - load_menu_from_csv(): Loads the menu from a CSV file and appends valid entries to the menu list.
    """
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = load_menu_from_csv(restaurant_menu_list, filename, spicy_scale_map)
        if result == -1:
            print(f"WARNING: |{filename}| is an invalid file name!")
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        elif result is None:
            print(f"WARNING: | {filename} | was not found!")
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully restored restaurant menu from | {filename} |")
            break


def update_helper(restaurant_menu_list, spicy_scale_map):
    """
    Provides an interface for updating a dish's information in the restaurant menu.

    This function allows the user to update a specific field for a selected dish from the 
    `restaurant_menu_list`. It first checks if the menu list is empty and prints a warning if there 
    is nothing to update. If the list is not empty, the function displays the available dishes and 
    asks the user to choose which dish to update. The user then selects the field to update and 
    enters the new value. The function uses `update_menu_dish()` to apply the change, and 
    prints whether the update was successful or if there was an error.

    Args:
        restaurant_menu_list (list): A list of dictionaries where each dictionary represents a dish 
                                     in the restaurant menu. Each dish contains fields like:
                                     - "name" (str)
                                     - "calories" (int or float)
                                     - "price" (float)
                                     - "is_vegetarian" (str)
                                     - "spicy_level" (int)

        spicy_scale_map (dict): A dictionary mapping integer spiciness levels to string 
                                descriptions (e.g., {1: "Mild", 2: "Medium", 3: "Hot"}).

    Returns:
        None: This function does not return any value. It updates the selected dish in 
              `restaurant_menu_list` or prints an error if the update is invalid.

    Helper Functions:
        - print_restaurant_menu(): Displays the current menu with dish names and indices.
        - is_valid_index(): Checks if the selected dish index is valid.
        - get_selection(): Allows the user to select which field to update.
        - update_menu_dish(): Updates the selected field of the dish with the new value.
        - print_dish(): Prints the updated dish details.

    Edge Cases:
        - If the `restaurant_menu_list` is empty:
            WARNING: There is nothing to update!
        - If an invalid dish number is entered:
            WARNING: |3| is an invalid dish number!
        - If an invalid value is entered for a field:
            WARNING: invalid information for the field |price|! The menu was not updated.
    """
    continue_action = 'y'
    while continue_action == 'y':
        if not restaurant_menu_list:
            print("WARNING: There is nothing to update!")
            break
        print("::: Which dish would you like to update?")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
        print("::: Enter the number corresponding to the dish.")
        user_option = input("> ")
        if is_valid_index(restaurant_menu_list, user_option):
            dish_idx = int(user_option) - 1
            subopt = get_selection("update", restaurant_menu_list[dish_idx], to_upper=False, go_back=True)
            if subopt == 'M' or subopt == 'm':
                break
            print(f"::: Enter a new value for the field |{subopt}|")
            field_info = input("> ")
            result = update_menu_dish(restaurant_menu_list, dish_idx, spicy_scale_map, subopt, field_info)
            if type(result) == dict:
                print(f"Successfully updated the field |{subopt}|:")
                print_dish(result, spicy_scale_map)
            else:  # update_menu_dish() returned an error
                print(f"WARNING: invalid information for the field |{subopt}|!")
                print(f"The menu was not updated.")
        else:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid dish number!")

        print("::: Would you like to update another menu dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()


def update_menu_dish(restaurant_menu_list, idx, spicy_scale_map, field_key, field_info, start_idx=0):
    """
    Updates a specified field in a dish from the restaurant menu if the input is valid.

    This function updates a specific field (`field_key`) of a dish in `restaurant_menu_list` 
    located at the index `idx`. The function first validates the index, field, and the value 
    provided in `field_info` using various helper functions. If all validations pass, the dish is 
    updated, and the updated dictionary is returned. If any validation fails, an appropriate error 
    code or message is returned.

    Args:
        restaurant_menu_list (list): A list of dictionaries where each dictionary represents a dish 
                                     in the restaurant menu.
        idx (str): A string representing the index of the dish to update in the `restaurant_menu_list`. 
                   This index is validated to ensure it is a valid index in the list.
        spicy_scale_map (dict): A dictionary mapping integer spiciness levels to their string 
                                descriptions (e.g., {1: "Mild", 2: "Medium", 3: "Hot"}), used to 
                                validate spiciness levels when updating the "spicy_level" field.
        field_key (str): The key in the dish's dictionary that corresponds to the field to be updated 
                         (e.g., "name", "calories", "price", "is_vegetarian", "spicy_level").
        field_info (str): The new value for the field specified by `field_key`. This value will be 
                          validated and converted to the correct type (e.g., string for "name", 
                          integer for "calories").
        start_idx (int, optional): The starting index for adjusting `idx` to 0-based indexing. Defaults to 0.

    Returns:
        dict:
            - If the update is successful, returns the updated dish (dictionary) from `restaurant_menu_list`.
        int:
            - Returns 0 if `restaurant_menu_list` is empty.
            - Returns -1 if `idx` is invalid (i.e., cannot index the list).
            - Returns -2 if `field_key` is not a valid key in the dish dictionary.
        str:
            - If validation fails for a field (e.g., invalid "price"), returns the `field_key` indicating the failed validation.

    Helper Functions:
        - is_valid_index(): Checks if the provided `idx` is a valid index in `restaurant_menu_list`.
        - is_valid_name(), is_valid_calories(), is_valid_price(), is_valid_is_vegetarian(), 
          is_valid_spicy_level(): Validate the corresponding fields based on the field being updated.
    """
    new_idx = str(int(idx) - start_idx)
    int_idx = int(new_idx)

    if not restaurant_menu_list:
        return 0
    elif not is_valid_index(restaurant_menu_list, new_idx) or type(idx) != str:
        return -1
    elif str(field_key) not in restaurant_menu_list[int_idx]:
        return -2

    if field_key == 'name':
        if is_valid_name(field_info):
            restaurant_menu_list[int_idx][field_key] = field_info
            return restaurant_menu_list[int_idx]
        else:
            return field_key
    elif field_key == 'calories':
        if is_valid_calories(field_info):
            restaurant_menu_list[int_idx][field_key] = field_info
            return restaurant_menu_list[int_idx]
        else:
            return field_key
    elif field_key == 'price':
        if is_valid_price(field_info):
            restaurant_menu_list[int_idx][field_key] = field_info
            return restaurant_menu_list[int_idx]
        else:
            return field_key
    elif field_key == 'is_vegetarian':
        if is_valid_is_vegetarian(field_info):
            restaurant_menu_list[int_idx][field_key] = field_info
            return restaurant_menu_list[int_idx]
        else:
            return field_key
    elif field_key == 'spicy_level':
        if is_valid_spicy_level(field_info, spicy_scale_map):
            restaurant_menu_list[int_idx][field_key] = int(field_info)
            return restaurant_menu_list[int_idx]
        else:
            return field_key


def get_restaurant_expense_rating(restaurant_menu_list):
    """
    Calculates the average price of all menu items and determines the restaurant's expense rating.

    This function computes the average price of all dishes in the `restaurant_menu_list`. Based on 
    the computed average price, the restaurant's expense rating is determined and displayed:
    - If the average price is less than 10, the expense rating is "$".
    - If the average price is between 10 and 20 (inclusive of 10), the expense rating is "$$".
    - If the average price is 20 or more, the expense rating is "$$$".

    Args:
        restaurant_menu_list (list): A list of dictionaries where each dictionary represents a dish 
                                     in the restaurant menu. Each dish should have a "price" field 
                                     (float) representing the price of the dish.

    Returns:
        float: The average price of the menu items.
    """
    if not restaurant_menu_list:
        print("No items on the menu to rate.")
        return 0.0  # Handle empty menu list

    total_price = 0
    items = 0

    for item in restaurant_menu_list:
        total_price += item['price']
        items += 1

    avg_price = total_price / items

    if avg_price < 10:
        expense_rating = "$"
    elif avg_price < 20:
        expense_rating = "$$"
    else:
        expense_rating = "$$$"

    print(f"Expense rating is : {expense_rating}")
    print()
    return avg_price
