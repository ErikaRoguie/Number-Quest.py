import random; import sys

def play_game():
    Player_name = input("")
    print("Welcome to Number Quest the Higher/ Lower number guessing game", Player_name + "!")
    number_to_guess = random.randint(1, 100)

    while True:
        guess = int(input("Enter your guess: "))
        print("Guess the number?", guess)
        if guess == number_to_guess:
            print("Great, You guessed it!, want to keep  guessing? Yes, or no.")
            yes = input("Yes or No: ")
            if yes.lower() == "yes":
                print("Great, let's continue!")
                continue
            elif yes.lower() == "no":
                sys.exit()
                print("Game over! See you next time!")
                break
        elif guess < number_to_guess:
            print("Yikes, Too low!, wanted to guess again?")
        elif guess > number_to_guess:
            print("Hum um, Too high!, want to guess again?")

    print("Congratulations! You've guessed the number.")

play_game()
