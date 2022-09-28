import random
print("Welcome To Rock Paper Scissor Game")
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
 
while True:
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
    choice = int(input("User turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
         
    print("Computer choice is: " + comp_choice_name)
    print(choice_name + " V/s " + comp_choice_name)
    if((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice ==1 )):
        print("paper wins => ", end = "")
        result = "paper"     
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    else:
        print("scissor wins =>", end = "")
        result = "scissor"
    if result == choice_name:
        print("Congratulations!! You Won")
    else:
        print("You lose!!")
    print("Do you want to play again? (y/n)")
    print("press :y for 'yes'")
    print("press :n for 'no'")
    ans = input()
    if ans == 'n' or ans == 'N':
        break
print("Thanks for playing")
