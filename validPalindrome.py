import math

input = " "

def validPalindrome(input):

    cleaned_input = ""

    for i in input:
        if i.isalnum():
            cleaned_input += i.lower()
    

    for i in range(int(math.ceil(len(cleaned_input) / 2))):
        if cleaned_input[i] != cleaned_input[-1 - i]:
            return False
    
    return True

print(validPalindrome(input))
