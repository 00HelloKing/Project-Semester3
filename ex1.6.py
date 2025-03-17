# factorial of a number with FOR
# Author:Jin Kaifeng
# ID: W20109678

n = int(input("Enter an integer:"))

# for loop
if n < 0:
	print("Must be positive!")
else:
	res = 1
	for i in range(1,n+1):
		res *= i

# output
print(f"The factorial is:{res}")
