import random

# Rock Paper Scissors Game
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [Rock, Paper, Scissors]

while True:
    try:
        user_choice = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))
        if user_choice not in [0, 1, 2]:
            print("Invalid choice. Please choose 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number (0, 1, or 2).")
        continue

    computer_choice = random.randint(0, 2)

    print(f"\nYou chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
