from prompt import string # type: ignore


def welcome_user():
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name