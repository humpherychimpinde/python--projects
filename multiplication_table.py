# Ask the user for input
num = int(input("Enter a number: "))
print(f"\nMultplication Table for {num} :")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# Nested loop to print tables for 1-5
print("\n--- Multiplication Tables from 1 to 5 ---")
for n in range(1, 6):
	print(f"\nTable for {n}:")
	for i in range(1, 11):

		print(f"{n} x {i} = {n * i}")

