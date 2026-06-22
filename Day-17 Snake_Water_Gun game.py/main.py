print("=========================")
name = input("Enter Your name: ")
print("Hii 👋",name)
print("Welcome To the Snake Water Game")
print("=========================")
print("Hint = S-snake 🐍" "\nW-water🌊" "\nG-Gun🔫")
import random
play_game = True

while play_game:
   chances = 3 
   user_score = 0
   computer_score = 0
   while chances > 0:
        print(f"\nRemaining Chances: {chances}")
        choices = ["snake", "water","gun"]
        computer_choice = random.choice(choices)
        user_input = input("Choose S\W\G: ").lower()
        if user_input == "s":
            user_input = "snake"
        elif user_input == "w":
            user_input = "water"
        elif user_input == "g":
            user_input = "gun"
        else:
            print("Invalid input ! Please Enter S,W or G Only.")
            continue
        print(f"Computer choose: {computer_choice}")

        if user_input == computer_choice:
            print("It's a Draw!")
        elif user_input == "snake" and computer_choice == "water":
            print("You Win! Snake drinks water")
            user_score += 1
        elif user_input == "water" and computer_choice == "gun":
            print("You Win! Water destroys Gun")
            user_score += 1
        elif user_input == "gun" and computer_choice == "snake":
            print("You Win! Gun kills snake")
            user_score += 1
        else:
            print("Computer Wins! One Chance lost.")
            computer_score += 1
            chances -= 1

        if chances == 0:
            print("=====================")
            print("\nGame Over |  All Chances finished.")
            print(f"Final Score: You {user_score} - Computer {computer_score}")
            
            
            replay = input("Do You Want to Play Again?(Y/N)").lower()

            if replay != "y":
                play_game = False
                break