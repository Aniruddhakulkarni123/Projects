import random
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

game_images = [rock, paper, scissors]


User_In = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for scissors.\n"))
print(f"User Choice = {User_In}")

if User_In >= 3 or User_In < 0 :
 print("You typed an invalid number")
else:
  print(game_images[User_In])
  
  random_in = random.randint(0, 2)
  print(f"Computer's Choice = {random_in}")
  print(game_images[random_in])
  
  
  if (random_in == 2 and User_In == 0):
    print("You win !")
  elif random_in == 0 and User_In == 2:
    print ("You lose ")
  elif random_in > User_In:
    print("You lose")
  elif User_In > random_in:
    print("You Win !")
  elif random_in == User_In:
    print("It's a DRAW")