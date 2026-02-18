import random

print("Rock Paper Scissors Game")
print("1 = Rock, 2 = Paper, 3 = Scissors")

# User input
user = int(input("Enter your choice (1/2/3): "))

# Computer choice
computer = random.randint(1, 3)

# Show computer choice
if computer == 1:
    print("Computer chose: Rock")
elif computer == 2:
    print("Computer chose: Paper")
else:
    print("Computer chose: Scissors")

# Show user choice
if user == 1:
    print("You chose: Rock")
elif user == 2:
    print("You chose: Paper")
elif user == 3:
    print("You chose: Scissors")
else:
    print("Invalid input")
    exit()

# Game logic
if user == computer:
    print("It's a Draw!")
elif (user == 1 and computer == 3) or \
     (user == 2 and computer == 1) or \
     (user == 3 and computer == 2):
    print("You Win!")
else:
    print("Computer Wins!")
