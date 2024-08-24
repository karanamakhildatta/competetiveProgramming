# reverse the only letters in the string and keep the other characters as it is
def reverseOnlyLetters(string):
    left = 0
    right = len(string) - 1
    string = list(string)
    while left < right:
        if not string[left].isalpha():
            left += 1
        elif not string[right].isalpha():
            right -= 1
        else:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
    return "".join(string)
