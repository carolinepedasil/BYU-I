# This game was shared with 2 people. They enjoyed the challenge and appreciated the hidden options!
# To exceed requirements, I added three levels of choices, one with more than two options.

def adventure_game():
    print("You are walking through a dark forest and find three items: a MATCH, a FLASHLIGHT, and a MAP.")
    choice1 = input("Which one do you want to pick up? (MATCH/FLASHLIGHT/MAP): ").strip().lower()

    if choice1 == "match":
        print("You pick up the match and strike it. You see a large grizzly bear!")
        choice2 = input("Do you want to RUN, HIDE behind a tree, or CLIMB a nearby rock? (RUN/HIDE/CLIMB): ").strip().lower()

        if choice2 == "run":
            print("You run as fast as you can, but the bear is gaining on you!")
            choice3 = input("Do you want to CLIMB a tree, JUMP in a river, or KEEP running? (CLIMB/JUMP/RUN): ").strip().lower()

            if choice3 == "climb":
                print("You climb the tree and the bear can't reach you. After waiting for hours, you escape safely!")
            elif choice3 == "jump":
                print("You jump into the river and are carried away to safety. You win!")
            elif choice3 == "run":
                print("You keep running, but the bear catches up. Game over.")
            else:
                print("Invalid choice. Please type CLIMB, JUMP, or RUN.")
        
        elif choice2 == "hide":
            print("You hide behind a tree, but the bear is sniffing around!")
            choice3 = input("Do you want to THROW a rock, STAY still, or SHOUT? (THROW/STAY/SHOUT): ").strip().lower()

            if choice3 == "throw":
                print("You throw a rock to distract the bear, and it chases the noise. You escape!")
            elif choice3 == "stay":
                print("You stay still, but the bear finds you. Game over.")
            elif choice3 == "shout":
                print("You shout loudly and scare the bear away! You win!")
            else:
                print("Invalid choice. Please type THROW, STAY, or SHOUT.")
        
        elif choice2 == "climb":
            print("You climb a nearby rock, but the bear starts circling!")
            choice3 = input("Do you want to WAIT, THROW something, or JUMP off the rock? (WAIT/THROW/JUMP): ").strip().lower()

            if choice3 == "wait":
                print("You wait patiently until the bear leaves. You escape safely!")
            elif choice3 == "throw":
                print("You throw something at the bear, and it leaves. You win!")
            elif choice3 == "jump":
                print("You jump off the rock and hurt yourself. The bear catches you. Game over.")
            else:
                print("Invalid choice. Please type WAIT, THROW, or JUMP.")
    
    elif choice1 == "flashlight":
        print("You pick up the flashlight and turn it on. You see a pathway lit up in front of you.")
        choice3 = input("Do you want to FOLLOW the path, LOOK in the trees, or TURN off the flashlight? (FOLLOW/LOOK/TURN OFF): ").strip().lower()

        if choice3 == "follow":
            print("You follow the path, but you hear strange noises behind you!")
            choice4 = input("Do you want to RUN, HIDE, or CALL for help? (RUN/HIDE/CALL): ").strip().lower()

            if choice4 == "run":
                print("You run down the path and find a hidden treasure. You win!")
            elif choice4 == "hide":
                print("You hide, but the noise gets closer. Game over.")
            elif choice4 == "call":
                print("You call for help, and someone arrives to guide you to safety. You win!")
            else:
                print("Invalid choice. Please type RUN, HIDE, or CALL.")
        
        elif choice3 == "look":
            print("You look into the trees and see glowing eyes staring back at you!")
            choice4 = input("Do you want to FIGHT, RUN, or INVESTIGATE further? (FIGHT/RUN/INVESTIGATE): ").strip().lower()

            if choice4 == "fight":
                print("You fight the creature and win! You are victorious!")
            elif choice4 == "run":
                print("You run away safely, but miss out on adventure. Game over.")
            elif choice4 == "investigate":
                print("You investigate and discover a friendly creature who shows you a secret path. You win!")
            else:
                print("Invalid choice. Please type FIGHT, RUN, or INVESTIGATE.")
        
        elif choice3 == "turn off":
            print("You turn off the flashlight and wait in the dark.")
            choice4 = input("Do you want to WAIT for daylight, LIGHT a match, or WALK in the dark? (WAIT/LIGHT/WALK): ").strip().lower()

            if choice4 == "wait":
                print("You wait for daylight and find your way out. You win!")
            elif choice4 == "light":
                print("You light a match, but it quickly goes out. You're lost. Game over.")
            elif choice4 == "walk":
                print("You walk in the dark and stumble upon a hidden cave. You win!")
            else:
                print("Invalid choice. Please type WAIT, LIGHT, or WALK.")
    
    elif choice1 == "map":
        print("You pick up the map and see a marked spot deeper in the forest.")
        choice5 = input("Do you want to GO to the marked spot, STAY where you are, or EXPLORE a different area? (GO/STAY/EXPLORE): ").strip().lower()

        if choice5 == "go":
            print("You follow the map to the marked spot, but encounter a fork in the road!")
            choice6 = input("Do you want to go LEFT, RIGHT, or STRAIGHT? (LEFT/RIGHT/STRAIGHT): ").strip().lower()

            if choice6 == "left":
                print("You go left and discover an ancient chest of gold! You win!")
            elif choice6 == "right":
                print("You go right, but get lost. Game over.")
            elif choice6 == "straight":
                print("You go straight and find a hidden cave with treasures. You win!")
            else:
                print("Invalid choice. Please type LEFT, RIGHT, or STRAIGHT.")
        
        elif choice5 == "stay":
            print("You stay in the forest, but darkness falls.")
            choice6 = input("Do you want to LIGHT a fire, BUILD a shelter, or WAIT for help? (LIGHT/BUILD/WAIT): ").strip().lower()

            if choice6 == "light":
                print("You light a fire and keep warm until morning. You survive!")
            elif choice6 == "build":
                print("You build a shelter, but it collapses during the night. Game over.")
            elif choice6 == "wait":
                print("You wait for help, but no one comes. Game over.")
            else:
                print("Invalid choice. Please type LIGHT, BUILD, or WAIT.")
        
        elif choice5 == "explore":
            print("You explore a different area and find a river.")
            choice6 = input("Do you want to CROSS the river, FOLLOW it, or TURN back? (CROSS/FOLLOW/RETURN): ").strip().lower()

            if choice6 == "cross":
                print("You cross the river and find safety. You win!")
            elif choice6 == "follow":
                print("You follow the river and find a hidden village. You win!")
            elif choice6 == "return":
                print("You turn back, but get lost. Game over.")
            else:
                print("Invalid choice. Please type CROSS, FOLLOW, or RETURN.")

    else:
        print("Invalid choice. Please type MATCH, FLASHLIGHT, or MAP.")

adventure_game()
