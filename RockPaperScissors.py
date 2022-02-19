rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_pick = random.randint(0,2)

print(f"Computer chose {computer_pick}")

if user_pick == 0 and computer_pick == 2:
  print("you win!")
if user_pick == 0  and computer_pick == 2:
  print("You win")
elif computer_pick > user_pick:
  print("You lose")
elif computer_pick == user_pick:
  print("It's a draw")
else:
  print('You typed an invalid number, you loose!')