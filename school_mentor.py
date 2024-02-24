# Amir Abu Hani
import string

def upper_lower_case():
    user_choice = input("Choose uppercase or lowercase for printing the abc: ")
    if user_choice == "uppercase":
        print(' '.join(string.ascii_uppercase))
    else:
        print(' '.join(string.ascii_lowercase))


def word_in_specific_letter():
    word = ""
    starting_letter = input("Enter your starting letter: ")
    word += starting_letter.upper()
    num_of_chars = int(input("how many letters do you want the word to contain "))
    for _ in range(1, num_of_chars):
        char = input("Enter your char ")
        word += char
    print(f"The word is: {word}")


def multiplication_table():
    n = int(input("Enter the number that you want to create a multiplication_table for him: "))
    print(" ", end="\t")
    for i in range(1, n + 1):
        print(i, end="\t")
    print()
    for i in range(1, n + 1):
        print(i, end="\t")
        for k in range(1, n + 1):
            print(i * k, end="\t")
        print("\t")


def square_number():
    number = int(input("Enter your number for squaring: "))
    square = number ** 2
    print(f"The square number for {number} is: {square} ")


def prime_number():
    your_number = int(input("Enter your number for checking if the number is prime or not: "))
    for num in range(2, int((your_number / 2)) + 1):
        if your_number % num == 0:
            print(f"your number {your_number} is not prime")
            break
    else:
        print(f"your number {your_number} is prime")


def tasks():
    user_choice = int(input("choose the task number you are intersted in:\n"
                            "1- print the abc in uppercase or lowercase\n"
                            "2- print a word starting with a specific letter\n"
                            "3- print N*N multiplication table\n"
                            "4- print square number of a given number\n"
                            "5- check if a given number is prime\n"))

    if user_choice == 1:
        upper_lower_case()
    elif user_choice == 2:
        word_in_specific_letter()
    elif user_choice == 3:
        multiplication_table()
    elif user_choice == 4:
        square_number()
    elif user_choice == 5:
        prime_number()
    else:
        return "Invalid input. must be 1-5"

tasks()
