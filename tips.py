import random
import pyjokes

# =========================
# THE TIPS AI
# Created by Sommay Singh
# =========================

def show_menu():
    print("\n==============================")
    print("         THE TIPS AI")
    print("==============================")
    print("c      - Calculator")
    print("game   - Guessing Game")
    print("joke   - Random Joke")
    print("abcd   - Alphabet")
    print("count  - Counter")
    print("sommay - About Creator")
    print("rr     - Memory Vault")
    print("exit   - Close Program")
    print("==============================")

while True:

    show_menu()

    command = input("What do you want to do? : ").strip().lower()

    # =========================
    # EXIT
    # =========================
    if command == "exit":
        print("Thank you for using The Tips AI!")
        break

    # =========================
    # CALCULATOR
    # =========================
    elif command == "c":

        try:
            num1 = float(input("First Number : "))
            op = input("Operator (+ - * / %) : ")
            num2 = float(input("Second Number : "))

            if op == "+":
                answer = num1 + num2

            elif op == "-":
                answer = num1 - num2

            elif op == "*":
                answer = num1 * num2

            elif op == "/":
                answer = num1 / num2

            elif op == "%":
                answer = num1 % num2

            else:
                answer = "Invalid Operator"

            print("Answer =", answer)

        except:
            print("Invalid Input!")

    # =========================
    # GUESSING GAME
    # =========================
    elif command == "game":

        print("\nI am thinking of a number between 1 and 100.")

        secret_number = random.randint(1, 100)
        attempts = 0

        while True:

            guess = input("Enter guess (or exit) : ")

            if guess.lower() == "exit":
                break

            try:
                guess = int(guess)
                attempts += 1

                if guess < secret_number:
                    print("Too Low!")

                elif guess > secret_number:
                    print("Too High!")

                else:
                    print(
                        f"Correct! Number was {secret_number}"
                    )
                    print(
                        f"You won in {attempts} attempts."
                    )
                    break

            except:
                print("Enter a valid number!")

    # =========================
    # JOKE
    # =========================
    elif command == "joke":

        print("\nRandom Joke:\n")
        print(pyjokes.get_joke())

    # =========================
    # ABCD
    # =========================
    elif command == "abcd":

        print(
            "\nA B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        )
        print(
            "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        )

    # =========================
    # COUNTER
    # =========================
    elif command == "count":

        try:
            limit = int(
                input("Count up to : ")
            )

            for i in range(1, limit + 1):
                print(i)

        except:
            print("Invalid Number!")

    # =========================
    # CREATOR INFO
    # =========================
    elif command == "sommay":

        print("""
==============================
ABOUT THE CREATOR
==============================

Creator : Sommay Singh

Class : 7

This project was created
using Python.

Features:
- Calculator
- Guessing Game
- Joke Generator
- Counter
- Memory Vault

This is my first AI project.

==============================
""")

    # =========================
    # MEMORY VAULT
    # =========================
    elif command == "rr":

        knowledge = {}

        try:
            with open("memory.txt", "r") as f:

                for line in f:

                    if "|" in line:

                        key, value = line.strip().split("|", 1)
                        knowledge[key] = value

        except:
            pass

        print("\n=== MEMORY VAULT ===")
        print("Example:")
        print("name = Sommay")
        print("name = delete")
        print("Type exit to leave.")

        while True:

            user = input("\nVault : ").strip().lower()

            if user == "exit":
                break

            elif "=" in user:

                key, value = user.split("=", 1)

                key = key.strip().lower()
                value = value.strip()

                if value.lower() == "delete":

                    if key in knowledge:

                        del knowledge[key]
                        print("Deleted!")

                    else:

                        print("Not Found!")

                else:

                    knowledge[key] = value
                    print("Saved!")

                with open("memory.txt", "w") as f:

                    for k, v in knowledge.items():
                        f.write(k + "|" + v + "\n")

            elif user in knowledge:

                print(
                    "Stored Value :",
                    knowledge[user]
                )

            else:

                print("Not Found!")

    # =========================
    # INVALID COMMAND
    # =========================
    else:

        print("Invalid Command!")