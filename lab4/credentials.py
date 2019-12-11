# CMPT 120 Intro to Programming
# Lab #4 – Working with Strings and Functions
# Author: Thomas Magnusson
# Created: 2019-10-28

# Why is this returning a list? Why not a tuple?
def get_name():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first, last]

# Good testable function
def create_user_name(first, last):
    '''
    Creates a Marist style email, first.last1@marist.edu
    '''
    return f"{first}.{last}1@marist.edu".lower()

# Good testable function
def password_is_strong(password):
    """
    Checks if a password is strong enough to create a user account.
     - Must be at least 8 characters long
     - Must contain at least one upper case character
     - Must contain at least one lower case character
    """
    return len(password) >= 8 and not password.lower() == password and not password.upper() == password

def get_password_and_check_strength():
    password = input("Create a new password: ")

    while not password_is_strong(password):
        # Error message could be improved
        print("Fool of a Took! That password is feeble!")
        password = input("Create a new password: ")
    print("The force is strong in this one...")

def main():
    [first, last] = get_name()

    username = create_user_name(first, last)
    
    get_password_and_check_strength()
    print("Account configured. Your new email address is",
        username)

# necessary for tests
if __name__ == '__main__':
    main()
