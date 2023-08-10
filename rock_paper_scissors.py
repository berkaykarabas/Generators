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
import random
total = [rock,paper,scissors]


user_choice = int(input("What do you choose\nRock --> 0\nPaper-->1\nScissors-->2 please select: "))
if user_choice == 0:
    user_choice = total[0]
    cpu_choice = random.choice(total)
    if cpu_choice == user_choice:
        print(user_choice)
        print(cpu_choice)
        print("It's draw")
    elif user_choice != cpu_choice:
        if cpu_choice == total[1]:
            print(user_choice)
            print(cpu_choice)
            print("Cpu is win")
        else:
            print(user_choice)
            print(cpu_choice)
            print("you win")
elif user_choice == 1:
    user_choice = total[1]
    cpu_choice = random.choice(total)
    if cpu_choice == user_choice:
        print(user_choice)
        print(cpu_choice)
        print("It's draw")
    elif user_choice != cpu_choice:
        if cpu_choice == total[2]:
            print(user_choice)
            print(cpu_choice)
            print("Cpu is win")
        else:
            print(user_choice)
            print(cpu_choice)
            print("you win")
elif user_choice == 2:
    user_choice = total[2]
    cpu_choice = random.choice(total)
    if cpu_choice == user_choice:
        print(user_choice)
        print(cpu_choice)
        print("It's draw")
    elif user_choice != cpu_choice:
        if cpu_choice == total[0]:
            print(user_choice)
            print(cpu_choice)
            print("Cpu is win")
        else:
            print(user_choice)
            print(cpu_choice)
            print("you win")


