number = int(input("Enter a number: "))
check = (int(input("Enter a number to divide by: ")))
mod = number % 2
if number % 4 ==0:
    print(f"Number {number} is a multiple of 4.")
if mod == 0:
    print(f"Number {number} is even.")
else:
    print(f"Number {number} is odd.")

if number % check == 0:
    print(f"{number} divides evenly by {check}")
else:
    print( f"{number} does not divide evenly by {check}" )


