# factorial of a number with While Loop
# Author:Jin Kaifeng
# ID: W20109678

n = int(input("Enter an integer:"))

# while loop
if n < 0:
	print("Must be positive!")
else:
	res = 1
	while n > 0:
		res *= n
		n -= 1

# output
print(f"The factorial is:{res}")
