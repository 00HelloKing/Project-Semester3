# Discount limitation
# Author:Jin Kaifeng
# ID: W20109678

age = input("Enter your age:")

# age condition
if int(age) <= 19:
	print("Student Discounts")
elif 20 <= int(age) <= 54:
	print("No Age Discounts")
else:
	print("Senior Discounts")
