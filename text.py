# text-based rpg: Field
# ask user for name and greet them
tiredness = 50
name = input("Welcome to Your Dream. What is your name? ")
print("")
print(f"Welcome {name}.")
print("To answer, input the letter within the square brackets.")
print(f"Your tiredness is {tiredness}.")
print("")
input("Type to continue: ").lower().strip()
# start game
# first main decision
print("")
print("You awake standing in a vast wheat field during midnight.")
print("[L]ook around")
print("[S]tart walking")
print("Sit [d]own")

ans1 = input("I will ").lower().strip()
print("")
print("")
print("")
print("")
# decision 1
if ans1 == "l":
    print("There are no buildings in sight but a line of telephone poles.")
    print(f"Your {tiredness}% tired")
    print("[f]ollow the poles")
    print("[r]un away")
    
    ans2 = input("I will ").lower().strip()
    print("")
    print("")
    print("")
    print("")
# decision 2
    if ans2 == "f":
        print("Eventually you reach a long road with no cars")
        tiredness -= 10
        print(f"Your {tiredness}% tired")
        print("[w]ait for a car")
        print("walk [o]n the road")
        print("walk [a]long the road")
        
        ans3 = input("I will ").lower().strip()
        print("")
        print("")
        print("")
        print("")
# decision 3
        if ans3 == "w":
            print("You start slowly drifting back to sleep. A car drives by but does not see you.")
            tiredness = 100
            print(f"Your {tiredness}% tired")
            
        elif ans3 == "o":
            print("You get tired of walking, but a car stops behind you, honking.")
            tiredness += 10
            print(f"Your {tiredness}% tired")
            print("[h]itchhike")
            print("[r]un away")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
# decision 4
            if ans4 == "h":
                print("You get in, and the driver begins driving. You slowly drift back to sleep. You wake up in your bed.")
                tiredness += 10
                print(f"Your {tiredness}% tired")
                print("[s]tart the day")
                print("[g]o back to sleep")
                
                ans5 = input("I will ").lower().strip()
                print("")
                print("")
                print("")
                print("")
# decision 5 
                if ans5 == "s":
                    print("You start the day. You got through the dream.")
                    tiredness = 0
                    print(f"Your {tiredness}% tired")
                    
                if ans5 == "g":
                    print("You go back to sleep quickly. You go through it all over again.")
                    tiredness = 100
                    print(f"Your {tiredness}% tired")
                
            elif ans4 == "r":
                print("You run away, startled by the car. You trip in a ditch, and feel immense pain in your leg. Your eyes close and everything's dark.")
                tiredness = 100
                print(f"Your {tiredness}% tired")
                
        elif ans3 == "a":
            print("After a while a car drives by but is startled by your appearance on their side. They swerve into you and you pass out.")
            tiredness = 100
            print(f"Your {tiredness}% tired")
            
        else:
            print("Not an action. You get confused and drift to sleep.")
            tiredness = 100
            print(f"Your {tiredness}% tired")
        
    elif ans2 == "r":
        print("You find a big red barn and a tall metal silo")
        tiredness -= 10
        print(f"Your {tiredness}% tired")
        print("[c]heck inside the barn")
        print("c[h]eck inside the silo")
        
        ans3 = input("I will ").lower().strip()
        print("")
        print("")
        print("")
        print("")
        
        
        if ans3 == "h":
            print("It is completely empty besides the metal ladder that reaches the top.")
            tiredness += 10
            print(f"Your {tiredness}% tired")
            print("[c]limb the ladder quickly")
            print("climb [t]he ladder slowly")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "c":
                print("You climb the ladder, but lose your grip from your tiredness and fall.")
                tiredness = 100
                print(f"Your {tiredness}% tired")
                
            elif ans4 == "t":
                print("You climb the ladder, you get tired but eventually get to the top.")
                tiredness -= 20
                print(f"Your {tiredness}% tired")
                print("[l]ook at the sky")
                print("[j]ump off the silo")
                
                ans5 = input("I will ").lower().strip()
                
                if ans5 == "l":
                    print("The sky is so beautiful you slowly fall asleep. You wake up in your bed.")
                    tiredness = 20
                    print(f"Your {tiredness}% tired")
                    print("[s]tart the day")
                    print("[g]o back to sleep")
                
                    ans5 = input("I will ").lower().strip()
                    print("")
                    print("")
                    print("")
                    print("")
                
                    if ans5 == "s":
                        print("You start the day. You got through the dream.")
                        tiredness = 0
                        print(f"Your {tiredness}% tired")
                    
                    if ans5 == "g":
                        print("You go back to sleep quickly. You go through it all over again.")
                        tiredness = 100
                        print(f"Your {tiredness}% tired")
                    
                elif ans5 == "j":
                    print("You jump off and everything's dark.")
                    tiredness = 100
                    print(f"Your {tiredness}% tired")
                     
                else:
                    print("Not an action. You get confused and drift to sleep.")
                    tiredness = 100
                    print(f"Your {tiredness}% tired")
        
                
        elif ans3 == "c":
            print("There are no animals in the barn, only piles of hay.")
            tiredness += 10
            print(f"Your {tiredness}% tired")
            print("[t]ake a nap in the hay")
            print("[j]ump face first in the hay ")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "t":
                print("The tiredness of the constant walking made you instantly fall asleep.")
                tiredness = 100
                print(f"Your {tiredness}% tired")
                
            elif ans4 == "j":
                print("You wake up in bed. It was all a dream.")
                tiredness = 20
                print(f"Your {tiredness}% tired")
                print("[s]tart the day")
                print("[g]o back to sleep")
                
                ans5 = input("I will ").lower().strip()
                print("")
                print("")
                print("")
                print("")
                
                if ans5 == "s":
                    print("You start the day. You got through the dream.")
                    tiredness = 0
                    print(f"Your {tiredness}% tired")
                    
                elif ans5 == "g":
                    print("You go back to sleep quickly. You go through it all over again.")
                    tiredness = 100
                    print(f"Your {tiredness}% tired")
                    
                else:
                    print("Not an action. You get confused and drift to sleep.")
                    tiredness = 100
                    print(f"Your {tiredness}% tired")
                
            else:
                print("Not an action. You get confused and drift to sleep.")
                tiredness = 100
                print(f"Your {tiredness}% tired")
                    
        else:
            print("Not an action. You get confused and drift to sleep.")
            tiredness = 100
            print(f"Your {tiredness}% tired")
                    
    else:
        print("Not an action. You get confused and drift to sleep.")
        tiredness = 100
        print(f"Your {tiredness}% tired")
    
elif ans1 == "s":
    print("You walk for a while but your legs are tired")
    tiredness += 10
    print(f"Your {tiredness}% tired")
    print("[s]leep")
    print("[k]eep going")
    
    ans2 = input("I will ").lower().strip()
    print("")
    print("")
    print("")
    print("")
    
    if ans2 == "s":
        print("You slowly drift back to sleep...")
        tiredness = 100
        print(f"Your {tiredness}% tired")
    
    elif ans2 == "k":
        print("You find a big red barn and a tall metal silo")
        tiredness += 10
        print(f"Your {tiredness}% tired")
        print("[c]heck inside the barn")
        print("c[h]eck inside the silo")
        
        ans3 = input("I will ").lower().strip()
        print("")
        print("")
        print("")
        print("")
        
        if ans3 == "h":
            print("It is completely empty besides the metal ladder that reaches the top.")
            tiredness += 10
            print(f"Your {tiredness}% tired")
            print("[c]limb the ladder quickly")
            print("climb [t]he ladder slowly")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "c":
                print("You climb the ladder, but lose your grip from your tiredness and fall.")
                tiredness = 100
                print(f"Your {tiredness}% tired")
                
            elif ans4 == "t":
                print("You climb the ladder, you get tired but eventually get to the top.")
                tiredness -= 20
                print(f"Your {tiredness}% tired")
                print("[l]ook at the sky")
                print("[j]ump off the silo")
                
                ans5 = input("I will ").lower().strip()
                
                if ans5 == "l":
                    print("The sky is so beautiful you slowly fall asleep. You wake up in your bed.")
                    tiredness = 20
                    print(f"Your {tiredness}% tired")
                    print("[s]tart the day")
                    print("[g]o back to sleep")
                    
                elif ans5 == "j":
                    print("You jump off and everything's dark.")
                    tiredness = 100
                    print(f"Your {tiredness}% tired")
                
                    ans6 = input("I will ").lower().strip()
                    print("")
                    print("")
                    print("")
                    print("")
                
                    if ans6 == "s":
                        print("You start the day. You got through the dream.")
                        tiredness = 0
                        print(f"Your {tiredness}% tired")
                    
                    elif ans6 == "g":
                        print("You go back to sleep quickly. You go through it all over again.")
                        tiredness = 100
                        print(f"Your {tiredness}% tired")
                    

                    
                     
                    else:
                        print("Not an action. You get confused and drift to sleep.")
                        tiredness = 100
                        print(f"Your {tiredness}% tired")
        
                
        elif ans3 == "c":
            print("There are no animals in the barn, only piles of hay.")
            tiredness += 10
            print(f"Your {tiredness}% tired")
            print("[t]ake a nap in the hay")
            print("[j]ump face first in the hay ")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "t":
                print("The tiredness of the constant walking made you instantly fall asleep.")
                tiredness = 100
                print(f"Your {tiredness}% tired")
                
            elif ans4 == "j":
                print("You wake up in bed. It was all a dream.")
                tiredness = 20
                print(f"Your {tiredness}% tired")
                print("[s]tart the day")
                print("[g]o back to sleep")
                
                ans5 = input("I will ").lower().strip()
                print("")
                print("")
                print("")
                print("")
                
                if ans5 == "s":
                    print("You start the day. You got through the dream.")
                    tiredness = 0
                    print(f"Your {tiredness}% tired")
                    
                elif ans5 == "g":
                    print("You go back to sleep quickly. You go through it all over again.")
                    tiredness = 100
                    print(f"Your {tiredness}% tired")
                    
                else:
                    print("Not an action. You get confused and drift to sleep.")
                    tiredness = 100
                    print(f"Your {tiredness}% tired")
                
            else:
                print("Not an action. You get confused and drift to sleep.")
                tiredness = 100
                print(f"Your {tiredness}% tired")
                    
        else:
            print("Not an action. You get confused and drift to sleep.")
            tiredness = 100
            print(f"Your {tiredness}% tired")
                    
    else:
        print("Not an action. You get confused and drift to sleep.")
        tiredness = 100
        print(f"Your {tiredness}% tired")
    
elif ans1 == "d":
    print("You slowly drift back to sleep")
    tiredness = 100
    print(f"Your {tiredness}% tired")
    
else:
    print("Not an action. You get confused and drift to sleep.")
    tiredness = 100
    print(f"Your {tiredness}% tired")