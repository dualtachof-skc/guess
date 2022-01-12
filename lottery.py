import random
number = random.randint(1, 60)
numberB = random.randint(1, 5)
user = int(input("Pick a number 1-60: "))
user = int(input("Pick a number 1-5: "))
if number==user:
    print ('Correct')
elif numberB==user:
    print ('You won')
elif numberB!=user:
    print ('You lost')    
