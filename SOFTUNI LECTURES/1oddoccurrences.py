words = (input().lower()).split(' ')

occurrences = {}

for element in words:
    if element not in occurrences:
        occurrences[element] = 0

    occurrences[element] +=1

odd_occurrences = [key for (key, value) in occurrences.items() if value % 2 ==1]

print(*odd_occurrences, sep=', ')