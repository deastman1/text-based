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
        
    if ans2 == "r":
        print("You find a big red barn and a tall metal silo")
    
elif ans1 == "s":
    print("You walk for a while but your legs are tired")
    
elif ans1 == "d":
    print("You slowly drift back to sleep")
