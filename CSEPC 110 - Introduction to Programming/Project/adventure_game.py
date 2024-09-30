# This game was shared with 2 people. They enjoyed the challenge and appreciated the hidden options!
# To exceed requirements, I added three levels of choices, one with more than two options.

def adventure_game():
    print("You are walking through a dark forest and find three items: a MATCH, a FLASHLIGHT, and a MAP.")
    choice1 = input("Which one do you want to pick up? (MATCH/FLASHLIGHT/MAP): ").strip().lower()

    if choice1 == "match":
        print("You pick up the match and strike it. You see a large grizzly bear!")
        choice2 = input("Do you want to RUN or HIDE behind a tree? (RUN/HIDE): ").strip().lower()
        
        if choice2 == "run":
            print("You run as fast as you can and escape the bear. You find safety!")
        elif choice2 == "hide":
            print("You hide behind a tree, but the bear finds you. Game over.")
        else:
            print("Invalid choice. Please type RUN or HIDE.")
    
    elif choice1 == "flashlight":
        print("You pick up the flashlight and turn it on. You see a pathway lit up in front of you.")
        choice3 = input("Do you want to FOLLOW the path or LOOK in the trees? (FOLLOW/LOOK): ").strip().lower()
        
        if choice3 == "follow":
            print("You follow the path and discover a hidden treasure! You win!")
        elif choice3 == "look":
            print("You look in the trees and find a mysterious creature. It offers you a choice: FIGHT or FLEE.")
            choice4 = input("What do you choose? (FIGHT/FLEE): ").strip().lower()
            
            if choice4 == "fight":
                print("You bravely confront the creature and win! You are a hero!")
            elif choice4 == "flee":
                print("You run away safely, but you miss out on an adventure. Game over.")
            else:
                print("Invalid choice. Please type FIGHT or FLEE.")
        else:
            print("Invalid choice. Please type FOLLOW or LOOK.")
    
    elif choice1 == "map":
        print("You pick up the map and see a marked spot deeper in the forest.")
        choice5 = input("Do you want to GO to the marked spot or STAY where you are? (GO/STAY): ").strip().lower()
        
        if choice5 == "go":
            print("You follow the map to the spot and find an ancient chest full of gold! You win!")
        elif choice5 == "stay":
            print("You stay in the forest, but darkness falls, and you lose your way. Game over.")
        else:
            print("Invalid choice. Please type GO or STAY.")
    
    else:
        print("Invalid choice. Please type MATCH, FLASHLIGHT, or MAP.")

# Start the game
adventure_game()
