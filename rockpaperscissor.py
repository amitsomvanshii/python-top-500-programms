import random
print("welcome to rock paper scissor game")
print("1 = rock, 2 = paper, 3 = scissor")

user_1 = input("enter your choise: ")
if user_1 == 1:
    print("rock")
elif user_1 == 2:
    print("paper")
else: 
    print("scissor")
    
computer = random.randint(1, 3)
if computer ==1:
    print("rock")
elif computer ==2:
    print("paper")
else:
    print("scissor")  
    
# game logic
if user_1 == computer:
    print("its draw")
elif (user_1 ==1 and computer ==3 ) or \
    (user_1 ==2 and computer==1 ) or \
    (user_1 ==3 and computer ==2):
    print("you win")
else:
    print("computer wins")
    