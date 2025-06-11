# text-based rpg: Field
# ask user for name and greet them
name = input("Welcome to Your Dream. What is your name? ")
print(f"Welcome {name}.")
# start game
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
if ans1 == "l":
    print("There are no buildings in sight but a line of telephone poles.")
    print("[f]ollow the poles")
    print("[r]un away")
    
    ans2 = input("I will ").lower().strip()
    print("")
    print("")
    print("")
    print("")
    
    if ans2 == "f":
        print("Eventually you reach a long road with no cars")
        print("[w]ait for a car")
        print("walk [o]n the road")
        print("walk [a]long the road")
        
        ans3 = input("I will ").lower().strip()
        print("")
        print("")
        print("")
        print("")
        
        if ans3 == "w":
            print("You start slowly drifting back to sleep. A car drives by but does not see you.")
            
        elif ans3 == "o":
            print("You get tired of walking, but a car stops behind you, honking.")
            print("[h]itchhike")
            print("[r]un away")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "h":
                print("You get in, and the driver begins driving. You slowly drift back to sleep. You wake up in your bed.")
                print("[s]tart the day")
                print("[g]o back to sleep")
                
                ans5 = input("I will ").lower().strip()
                print("")
                print("")
                print("")
                print("")
                
                if ans5 == "s":
                    print("You start the day. You got through the dream.")
                    
                if ans5 == "g":
                    print("You go back to sleep quickly. You go through it all over again.")
                
            elif ans4 == "r":
                print("You run away, startled by the car. You trip in a ditch, and feel immense pain in your leg. Your eyes close and everything's dark.")
                
        elif ans3 == "a":
            print("After a while a car drives by but is startled by your appearance on their side. They swerve into you and you pass out.")
            
        else:
            print("Not an action. You get confused and drift to sleep.")
        
    elif ans2 == "r":
        print("You find a big red barn and a tall metal silo")
        print("[c]heck inside the barn")
        print("c[h]eck inside the silo")
        
        ans3 = input("I will ").lower().strip()
        print("")
        print("")
        print("")
        print("")
        
        
        if ans3 == "h":
            print("It is completely empty besides the metal ladder that reaches the top.")
            print("[c]limb the ladder quickly")
            print("climb [t]he ladder slowly")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "c":
                print("You climb the ladder, but lose your grip from your tiredness and fall.")
                
            elif ans4 == "t":
                print("You climb the ladder, you get tired but eventually get to the top.")
                print("[l]ook at the sky")
                print("[j]ump off the silo")
                
                ans5 = input("I will ").lower().strip()
                
                if ans5 == "l":
                    print("The sky is so beautiful you slowly fall asleep. You wake up in your bed.")
                    print("[s]tart the day")
                    print("[g]o back to sleep")
                
                    ans5 = input("I will ").lower().strip()
                    print("")
                    print("")
                    print("")
                    print("")
                
                    if ans5 == "s":
                        print("You start the day. You got through the dream.")
                    
                    if ans5 == "g":
                        print("You go back to sleep quickly. You go through it all over again.")
                    
                elif ans5 == "j":
                     print("You jump off and everything's dark.")
                     
                else:
                    print("Not an action. You get confused and drift to sleep.")   
        
                
        elif ans3 == "c":
            print("There are no animals in the barn, only piles of hay.")
            print("[t]ake a nap in the hay")
            print("[j]ump face first in the hay ")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "t":
                print("The tiredness of the constant walking made you instantly fall asleep.")
                
            elif ans4 == "j":
                print("You wake up in bed. It was all a dream.")
                print("[s]tart the day")
                print("[g]o back to sleep")
                
                ans5 = input("I will ").lower().strip()
                print("")
                print("")
                print("")
                print("")
                
                if ans5 == "s":
                    print("You start the day. You got through the dream.")
                    
                if ans5 == "g":
                    print("You go back to sleep quickly. You go through it all over again.")
                    
                else:
                  print("Not an action. You get confused and drift to sleep.")
                
            else:
              print("Not an action. You get confused and drift to sleep.")
                    
        else:
          print("Not an action. You get confused and drift to sleep.")
                    
    else:
        print("Not an action. You get confused and drift to sleep.")
    
elif ans1 == "s":
    print("You walk for a while but your legs are tired")
    print("[s]leep")
    print("[k]eep going")
    
    ans2 = input("I will ").lower().strip()
    print("")
    print("")
    print("")
    print("")
    
    if ans2 == "s":
        print("You slowly drift back to sleep...")
    
    if ans2 == "k":
        print("You find a big red barn and a tall metal silo")
        print("[c]heck inside the barn")
        print("c[h]eck inside the silo")
        
        ans3 = input("I will ").lower().strip()
        print("")
        print("")
        print("")
        print("")
        
        if ans3 == "h":
            print("It is completely empty besides the metal ladder that reaches the top.")
            print("[c]limb the ladder quickly")
            print("climb [t]he ladder slowly")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "c":
                print("You climb the ladder, but lose your grip from your tiredness and fall.")
                
            elif ans4 == "t":
                print("You climb the ladder, you get tired but eventually get to the top.")
                print("[l]ook at the sky")
                print("[j]ump off the silo")
                
                ans5 = input("I will ").lower().strip()
                
                if ans5 == "l":
                    print("The sky is so beautiful you slowly fall asleep. You wake up in your bed.")
                    print("[s]tart the day")
                    print("[g]o back to sleep")
                
                    ans5 = input("I will ").lower().strip()
                    print("")
                    print("")
                    print("")
                    print("")
                
                    if ans5 == "s":
                        print("You start the day. You got through the dream.")
                    
                    if ans5 == "g":
                        print("You go back to sleep quickly. You go through it all over again.")
                    
                elif ans5 == "j":
                     print("You jump off and everything's dark.")
                     
                else:
                    print("Not an action. You get confused and drift to sleep.")   
        
                
        elif ans3 == "c":
            print("There are no animals in the barn, only piles of hay.")
            print("[t]ake a nap in the hay")
            print("[j]ump face first in the hay ")
            
            ans4 = input("I will ").lower().strip()
            print("")
            print("")
            print("")
            print("")
            
            if ans4 == "t":
                print("The tiredness of the constant walking made you instantly fall asleep.")
                
            elif ans4 == "j":
                print("You wake up in bed. It was all a dream.")
                print("[s]tart the day")
                print("[g]o back to sleep")
                
                ans5 = input("I will ").lower().strip()
                print("")
                print("")
                print("")
                print("")
                
                if ans5 == "s":
                    print("You start the day. You got through the dream.")
                    
                if ans5 == "g":
                    print("You go back to sleep quickly. You go through it all over again.")
                    
                else:
                  print("Not an action. You get confused and drift to sleep.")
                
            else:
              print("Not an action. You get confused and drift to sleep.")
                    
        else:
          print("Not an action. You get confused and drift to sleep.")
                    
    else:
        print("Not an action. You get confused and drift to sleep.")
    
elif ans1 == "d":
    print("You slowly drift back to sleep")
    
else:
    print("Not an action. You get confused and drift to sleep.")
