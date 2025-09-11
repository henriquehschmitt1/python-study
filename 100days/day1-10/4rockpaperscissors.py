import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = [rock, paper, scissors]

userChoice = int(input("Welcome to Rock, Paper, Scissors! Type 0 for rock, 1 for paper and 2 for scissors."))
randomChoice = random.randint(0, 2)

if userChoice == 0:
    print(choices[0])
elif userChoice == 1:
    print(choices[1])
elif userChoice == 2:
    print(choices[2])

print("Computer chose:")
print(choices[randomChoice])


def rps(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        return "You win!"
    else:
        return "You lose!"

rpsResult = rps(userChoice, randomChoice)
print(rpsResult)