nums = input().split(' ')
odd_numbers = []

for item in nums:
    if (int(item)) % 2 is 1:
        odd_numbers.append(int(item))
    if (int(item)) % 2 is -1:
        odd_numbers.append(int(item))
print(len(odd_numbers))






