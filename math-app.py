import time
import random

def targil_plus():
    number = random.randint(1, 99)
    number1 = random.randint(1, 100-number)
    rez = int(input(f"{number}+{number1}="))
    if rez == (number+number1):
        print("CORRECT")
    else:
        print("INCORRECT")
        print("try again later")
        time.sleep(1)
#        exit()

def loop():
    for i in range(10):
        targil_plus()
loop_stop = False
while not loop_stop:
    loop()
    print("Congratulations! You have completed the challenge.")
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        loop_stop = True






