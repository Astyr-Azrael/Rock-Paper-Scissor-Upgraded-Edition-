import random
rock = '✊'
paper = '✋'
scissor = '✌️'
spock = '🖖'
lizard = '🦎'
u_point = 0
c_point = 0
c = False

while c != True:
  print("\n================================")
  print("Rock Paper Scissors Lizard Spock")
  print("================================")

  print("1) ✊")
  print("2) ✋")
  print("3) ✌️")
  print("4) 🦎")
  print("5) 🖖")
  choice = int(input("Pick a number: "))

  if choice == 1:
      print("\nYou chose:", rock)
  elif choice == 2:
      print("\nYou chose:", paper)
  elif choice == 3:
      print("\nYou chose:", scissor)
  elif choice == 4:
      print("\nYou chose:", lizard)
  elif choice == 5:
      print("\nYou chose:", spock)
  else:
      print("Invalid input.")

  cpu = random.randint(1,5)

  if cpu == 1:
      print("CPU chose:", rock)
  elif cpu == 2:
      print("CPU chose:", paper)
  elif cpu == 3:
      print("CPU chose:", scissor)
  elif cpu == 4:
      print("CPU chose:", lizard)
  elif cpu == 5:
      print("CPU chose:", spock)
  else:
      print("Invalid input.")

  if cpu == choice:
      print("It's a tie.")
      c_point = c_point + 0
      u_point = u_point + 0
  elif cpu == 2 and choice == 3:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 3 and choice == 2:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 1 and choice == 2:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 2 and choice == 1:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 4 and choice == 1:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 1 and choice == 4:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 5 and choice == 4:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 4 and choice == 5:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 3 and choice == 5:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 5 and choice == 3:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 4 and choice == 3:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 3 and choice == 4:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 2 and choice == 4:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 4 and choice == 2:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 5 and choice == 2:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 2 and choice == 5:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 1 and choice == 5:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 5 and choice == 1:
      print("You lose.")
      c_point = c_point + 1
  elif cpu == 3 and choice == 1:
      print("You won!")
      u_point = u_point + 1
  elif cpu == 1 and choice == 3:
      print("You lose.") 
      c_point = c_point + 1
  print("\nYour point:", u_point)
  print("CPU point:", c_point)
  print("\nDo you wish to continue? ")   
  print("1) Yes")
  print("2) No")
  game = int(input("Enter your choice(number): "))
  while game != 1 and game != 2:
      print("Invalid inut. Please type the correct input in number(1 for Yes and 2 for No).")
      print("\nDo you wish to continue? ")   
      print("1) Yes")
      print("2) No")
      game = int(input("Enter your choice(number): "))
  
  if game == 1:
          c = False
  elif game == 2:
          c = True
