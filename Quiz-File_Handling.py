import os

# Function to display the main menu
def main_menu():
    print("\n============================")
    print("    Welcome to the Quiz App  ")
    print("============================")
    print("1. Login")
    print("2. Register")
    print("3. Play Quiz")
    print("4. Quit")
    print("============================")

# Function to handle login
def login():
    print("\n=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not os.path.exists('users.txt'):
        print("No users found. Please register first.")
        return None

    with open('users.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            stored_username, stored_password = user.strip().split(',')
            if stored_username == username and stored_password == password:
                print(f"Welcome back, {username}!")
                return username
    print("Invalid username or password.")
    return None

# Function to handle registration
def register():
    print("\n=== Register ===")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    # Save the new user to the file
    with open('users.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    print("Registration successful! You can now log in.")

# Function to play the quiz
def play_quiz():
    questions = [
        ("What is the output of `print(2 + 3)`?", "5"),
        ("Which data type is used to store text in Python?", "str"),
        ("What is the correct syntax for defining a function in Python?", "def function_name():"),
        ("Which of the following is the correct way to create a list in Python?", "[]"),
        ("What does `len()` function do?", "Returns the length of an object"),
        ("Which of the following is used to import a module in Python?", "import"),
        ("How do you start a comment in Python?", "#"),
        ("Which of these is an immutable data type in Python?", "tuple"),
        ("What will be the output of `print(type(3.14))`?", "float"),
        ("How do you convert a string to an integer in Python?", "int()")
    ]

    score = 0
    print("\n=== Quiz Time ===")
    
    for i, (question, correct_answer) in enumerate(questions, 1):
        answer = input(f"{i}. {question} ")
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    print(f"\nYour score is: {score}/{len(questions)}")

# Main function to run the app
def main():
    logged_in_user = None  # Variable to track if a user is logged in

    while True:
        main_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            # Login
            if logged_in_user:
                print(f"You are already logged in as {logged_in_user}.")
                continue
            logged_in_user = login()
        elif choice == '2':
            # Register
            register()
        elif choice == '3':
            # Play Quiz
            if not logged_in_user:
                print("You must be logged in to play the quiz.")
                logged_in_user = login()
                if not logged_in_user:
                    continue  # If login fails, return to the main menu
            play_quiz()
        elif choice == '4':
            # Quit
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Check if the program is being run directly
if __name__ == "__main__":
    main()
