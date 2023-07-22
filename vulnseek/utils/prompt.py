from utils.print import clear_screen_with_message, quit_with_msg


def validate_number_selection(max: int) -> int:
    """
    Validates that the user will input an integer within
    the specified inclusive range of 0 to max

    Handles KeyboardInterrupt
    """
    while True:
        try:
            choice = int(input("> "))
        except ValueError:
            print("Please input a number")
            continue
        except KeyboardInterrupt:
            quit_with_msg()

        if choice > max or choice < 0:
            print(f"Please choose one of the available options from 0 to {max}")
            continue
        elif choice == 0:
            quit_with_msg()

        return choice


def prompt_param_required(param_name):
    """
    Prompts the user to input a non-empty string value for param_name and returns it
    """
    value = ""
    tried = False
    while len(value) == 0:
        if not tried:
            print("Please input the", param_name)
        else:
            print("Please input a non-empty value for", param_name)

        value = input()
        tried = True

    return value


def prompt_param_with_default_value(param_name, default_value):
    """
    Prompts the user to input a value for param_name with the option
    to input an empty string, which will be resolved to default_value
    """
    print("Please input the", param_name)
    print("You can also just press enter and it will default to", default_value)
    value = input()
    if len(value) == 0:
        value = default_value

    return value


def prompt_param_with_default_value_and_name(
    param_name, default_value, default_value_name
):
    """
    Prompts the user to input a value for param_name with the option
    to input an empty string, which will be resolved to default_value
    but will instead show default_value_name to the user
    """
    print("Please input the", param_name)
    print("You can also just press enter and it will default to", default_value_name)
    value = input()
    if len(value) == 0:
        value = default_value

    return value
