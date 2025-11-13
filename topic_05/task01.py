import random
stone_paper_scissors = ["stone", "paper", "scissors"]

user_choice = input("Please enter the next of three: 'stone' , 'paper', 'scissors'")
bot_choice = random.choice(stone_paper_scissors)
print(f"Bot choice {bot_choice}")

if user_choice == bot_choice:
    print("It's a draw!")
elif (
    (user_choice == "stone" and bot_choice == "scissors") or
    (user_choice == "scissors" and bot_choice == "paper") or
    (user_choice == "paper" and bot_choice == "stone")
):
    print("You win!")
elif user_choice in stone_paper_scissors:
    print("Bot wins!")
else:
    print("Invalid choice! Please enter 'stone', 'paper', or 'scissors'.")

