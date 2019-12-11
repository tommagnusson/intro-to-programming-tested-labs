# CMPT 120 Intro to Programming
# Lab #6 – Arithmetic Engine
# Author: Thomas Magnusson
# Created: 2019-10-28

def showIntro():
    print("Welcome to the Arithmetic Engine")
    print("================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()

        # candidate for a refactored function
        if cmd not in ["add", "sub", "mult", "div", "quit"]:
            print(f"'{cmd}' is not a valid command.")
            continue
        elif cmd == "quit":
            break
        
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except:
            print("Whoops, that wasn't a number, try again.")
            continue

        # candidate for a refactored function
        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
            result = num1 - num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            result = num1 // num2
            
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

if __name__ == "__main__":
    main()