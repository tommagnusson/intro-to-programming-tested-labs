# Lab 4

This is a perfect lab to really start testing. It involves refactoring procedural code into modular functions.
Testing is a great way to illustrate the importance of making function sufficiently modular.

If students are struggling to test a function, ask them to consider if they could break that function up, or reconsider the parameters or return values.

The `credentials_test.py` file contains lots of good information about a style of testing taken from Behavior Driven Design (BDD), called "Given, When, Then" style testing.

 - `Given`: List the preconditions and inputs to the function as variables
 - `When`: Invoke the function under test with the appropriate inputs
 - `Then`: Then assert that the post conditions of the function are expected

Also notice the extremely verbose test names. They indicate exactly what kind of conditions are being tested, so when one fails, the test function that fails clearly describes what went wrong.
