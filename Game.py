import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    while True:
        choice = input("choose rock, paper ou scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("invalid choice. try again.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You Win!"
    else:
        return "You lose!"

def play_game():
    print("welcome to the Rock, Paper e scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You choose: {user_choice}")
    print(f"the computer choose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
