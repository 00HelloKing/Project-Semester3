# Guess a random number
# Author:Jin Kaifeng
# ID: W20109678

import random
number = random.randint(10,20)

found=0

x = input("Guess a Number(10~20):")
while found == 0:
	if int(x) == number:
   		found=1
	else:
   		x = input("Wrong!Enter again:")

# output
print("Congradulations!")

