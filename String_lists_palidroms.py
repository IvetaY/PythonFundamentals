string_list = str(input("Enter a string: "))

if string_list[:len(string_list)+1] == string_list[::-1]:
    print("palindrome")
    print(f'{string_list[:len(string_list)+1]}')
    print(f'{string_list[::-1]}')
else:
    print("not palindrome")
    print( f'{string_list[:len(string_list)+1]}' )
    print( f'{string_list[::-1]}' )

