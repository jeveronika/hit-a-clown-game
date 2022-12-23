import random

pole1 = ["🟧", "🟧", "🟧"]
pole2 = ["🟧", "🟧", "🟧"]
pole3 = ["🟧", "🟧", "🟧"]
all_set = [pole1, pole2, pole3]

clown = str(random.randint(0,2))+str(random.randint(0,2))
nu1 = int(clown[0])
nu2 = int(clown[1])
all_set[nu1][nu2] = "🤡"

print("Hit a clown!!\n")
print(f"{pole1}\n{pole2}\n{pole3}")

### MAIN GAME ###

def play():
    lets_continue = "yes"
    lives = 5 # you can change this number of lives, more the easier the game

    while lives !=0 and lets_continue == "yes":
        lets_continue = input(f"\nType 'yes' if you're ready. Now you have {lives} lives: ").lower()
        
        position = str(random.randint(0,2))+str(random.randint(0,2))
        num1 = int(position[0])
        num2 = int(position[1])
        all_set[num1][num2] = "⭕"

        if all_set[num1][num2] == all_set[nu1][nu2]:
            all_set[num1][num2] = "✅"
            print(f"{pole1}\n{pole2}\n{pole3}")
            print("\nGOT HIM! Nic job!\n")
            break
        elif all_set[num1][num2] != all_set[nu1][nu2]:
            print("\nThis is what you've got:\n")
            print(f"{pole1}\n{pole2}\n{pole3}")
            print("\nYou've missed, try again...")
            lives -= 1
    
        if lives == 0:
            print(f"GAME OVER. You have {lives} lives.")
            break

play()

