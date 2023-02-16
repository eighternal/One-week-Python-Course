print("="*30)
print("WELCOME TO THE GAME!!!")
print("="*30)

player_1=input("enter player 1's name: ")
player_2=input("enter player 2's name: ")

num_left = 13

while True:
    
    if num_left == 1: 
        print("| "*num_left)
        print(f"There is {num_left} match left.")
        p1_choice = int(input(f"{player_1}, how many matches do you take? "))
        num_left-=p1_choice
        if num_left <= 0:
            print(f"{player_1} wins the game!")
            break


        print("| "*num_left)
        print(f"There is {num_left} match left.")
        p2_choice = int(input(f"{player_2}, how many matches do you take? "))
        num_left-=p2_choice
        if num_left <= 0:
            print(f"{player_2} wins the game!")
            break
    else:
        print("| "*num_left)
    print(f"There are {num_left} matches left.")
    p1_choice = int(input(f"{player_1}, how many matches do you take? "))
    num_left-=p1_choice
    if num_left <= 0:
        print(f"{player_1} wins the game!")
        break


    print("| "*num_left)
    print(f"There are {num_left} matches left.")
    p2_choice = int(input(f"{player_2}, how many matches do you take? "))
    num_left-=p2_choice
    if num_left <= 0:
        print(f"{player_2} wins the game!")
        break


print("GAME OVER!")
