import random
name = input("Enter your name: ")
player_life = 100 # players hälsa, en integer
Zombie_life = 50 # zombiens hälsa, en integer

while player_life > 0 or Zombie_life > 0: # loop som körs så länge någon av dem har hälsa kvar
    player_life -= random.randint(10, 30) #slupmässig skada mellan 10 och 30
    Zombie_life -= random.randint(5, 20) #slupmässig skada mellan 5 och 20
    print(f"{name}'s life: {player_life}, Zombie's life: {Zombie_life}") # skriver ut hälsan för båda personerna
    if player_life <= 0: # kollar om player har 0 eller mindre hälsa
        print(f"{name} Blev ägd av zombien")
    elif Zombie_life <= 0: # samma sak fast för zombien
        print(f"The Zombie has blev ägd av coola {name}")

    
