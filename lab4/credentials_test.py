from credentials import create_user_name, password_is_strong

# This style of testing follows the "Given, When, Then" paradigm, of the Behavior Driven Development framework.
# Given: the preconditions that are true before you invoke the thing you are testing.
# When: the actual invocation of what you are testing
# Then: the expected results of what you are testing, your postconditions

# Creating long, descriptive names is okay here, as long as you prefix with "test_" (required for pytest)
def test_create_user_name_formats_names_correctly():
    # Given I enter "tom" "magnusson"
    first = "tom"
    last = "magnusson"

    # When I create a new username for myself
    actual = create_user_name(first, last)

    # Then it formats in the correct format, with ".", "1" and "@marist.edu"
    expected = "tom.magnusson1@marist.edu"
    assert actual == expected

def test_created_user_name_is_lowercase():
    # Given I enter "TOM" "MAGNUSSON"
    first = "TOM"
    last = "MAGNUSSON"

    # When I create a new username for myself
    actual = create_user_name(first, last)

    # Then it is all lowercase
    expected = "tom.magnusson1@marist.edu"
    assert actual == expected

# Test the positive case first

def test_password_is_strong_password_valid_password():
    # Given I have a password that is at least eight characters long
    # And a mix of upper and lowercase
    password = "Password"

    # When I check if the password is strong
    actual = password_is_strong(password)

    # Then it IS strong
    expected = True
    assert actual == expected

# Then test each negative case

def test_password_is_strong_password_greater_than_seven_characters():
    # Given I have a password that is less than eight characters long
    password = "Short"

    # When I check if the password is strong
    actual = password_is_strong(password)

    # Then it is NOT strong
    expected = False
    assert actual == expected

def test_password_is_strong_password_not_all_lowercase():
    # Given I have a password that is all lowercase (and eight characters long)
    password = "all lowercase"

    # When I check if the password is strong
    actual = password_is_strong(password)

    # Then it is NOT strong
    expected = False
    assert actual == expected

def test_password_is_strong_password_not_all_uppercase():
    # Given I have a password that is all lowercase (and eight characters long)
    password = "ALL UPPERCASE"

    # When I check if the password is strong
    actual = password_is_strong(password)

    # Then it is NOT strong
    expected = False
    assert actual == expected

# TODO: make this pass, you might have to change other tests!
# def test_password_is_strong_password_contains_digit():
#     # Given I have a password that does not contain a digit
#     password = "Does not contain digit"

#     # When I check if the password is strong
#     actual = password_is_strong(password)

#     # Then it is NOT strong
#     expected = False
#     assert actual == expected

