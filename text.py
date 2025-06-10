# text-based rpg: Field
# ask user for name and greet them
name = input("Welcome to Field. What is your name? ")
print(f"Welcome {name}.")
# start game
print("")
print("You awake standing in a vast wheat field during midnight.")
print("[L]ook around")
print("[S]tart walking")
print("Sit [d]own")

ans1 = input("I will ").lower().strip()

if ans1 == "l":
    print("There are no buildings in sight but a line of telephone poles.")
    print("[f]ollow the poles")
    print("[r]un away")
    
    ans2 = input("I will ").lower().strip()
    
    if ans2 == "f":
        print("Eventually you reach a long road with no cars")
        print("[w]ait for a car")
        print("walk [o]n the road")
        print("walk [a]long the road")
        
        ans3 = input("I will ").lower().strip()
        
        if ans3 == "w":
            print("You start slowly drifting back to sleep. A car drives by but does not see you.")
            
        elif ans3 == "o":
            print("You get tired of walking, but a car stops behind you, honking.")
            print("[h]itchhike")
            print("[r]un away")
            
            ans4 = input("I will ").lower().strip()
            
            if ans4 == "h":
                print("You get in, and the driver begins driving. You slowly drift back to sleep. You wake up in your bed.")
                
            elif ans4 == "r":
                print("You run away, startled by the car. You trip in a ditch, and feel immense pain in your leg. Your eyes close and everything's dark.")
                
        elif ans3 == "a":
            print("After a while a car drives by but is startled by your appearance on their side. They swerve into you and you pass out.")
        
    if ans2 == "r":
        print("You find a big red barn and a tall metal silo")
        print("[c]heck inside the barn")
        print("c[h]eck inside the silo")
        
        ans3 = input("I will ").lower().strip()
        
        if ans3 == "c":
            print("There are no animals in the barn, only piles of hay.")

        elif ans3 == "h":
            print("It is completely empty besides the metal ladder that reaches the top.")
            print("[t]ake a nap in the hay")
            print("[j]ump face first in the hay ")
            
            ans4 = input("I will ").lower().strip()
            
            if ans4 == "t":
                print("The tiredness of the constant walking made you instantly fall asleep.")
                
            elif ans4 == "j":
                print("You wake up in bed. It was all a dream.")
                print("[s]tart the day")
                print("[g]o back to sleep")
                
                ans5 = input("I will ").lower().strip()
                
                if ans5
    
elif ans1 == "s":
    print("You walk for a while but your legs are tired")
    print("[s]leep")
    print("[k]eep going")
    
    ans2 = input("I will ").lower().strip()
    
    if ans2 == "s":
        print("You slowly drift back to sleep...")
    
     if ans2 == "k":
        print("You find a big red barn and a tall silo")
    
elif ans1 == "d":
    print("You slowly drift back to sleep")
