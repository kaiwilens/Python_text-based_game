def set_attributes(value, attribute):
    """Verifies integer input for attributes

    :param value: The integer input from the user
    :param attribute: The attribute to be set
    The code attempts to convert the input from the constructor and getters and setters
    and return the integer value for attributes such as strength, damage, health, and max health.
    If the return fails an error message is displayed and the attributes is set to 0.
    """
    try:
        int(value)
        return int(value)
    except ValueError:
        my_banner("Value must be an integer." + attribute.upper() +
                  " set to 0. Use " + attribute.upper() + " setter function to change attribute.")
        return 0


def check_enum(enumerator, value):
    """Verifies value input for enumerators

     :param enumerator: The enumerator that will be checked
     :param value: The value that will be checked against enumerator values
     The code checks the value entered by the user and compares it to the enumerator values.
     If it matches one of the enumerator values then the member variable will be set.
     If it does not then the member variable will be set to NA
     """
    is_valid = False
    for data in enumerator:
        if data == value:
            is_valid = True
            break

    if is_valid:
        return value
    else:
        my_banner("Value must be from enum " + enumerator +" Value has been set to N/A")
        return "na"


def check_boolean(value):
    if value == True or value == False:
        return value
    else:
        my_banner("Value must be TRUE or FALSE. Value has been set to FALSE. USE SETTER TO CHANGE.")
        return False


def my_banner(bannerString):
    """Given a string this will print a banner string which will be the same length of it."""
    print(len(bannerString) * "!")
    print(bannerString)
    print(len(bannerString) * "!")
