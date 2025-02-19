# hello.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
# Code Explanation:
# greet(name): A function that takes a name as an argument and returns a greeting.
# __main__ block: Ensures that the code only runs when the script is executed directly (not imported into another script).
# input("Enter your name: "): Prompts the user to input their name.
# print(greet(name)): Prints the greeting message using the greet() function.
