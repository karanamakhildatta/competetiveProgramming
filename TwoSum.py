# Enter your code here. Read input from STDIN. Print output to STDOUT

inputForm = list(map(int, input().split()))
numberArray = list(map(int, input().split()))
n = inputForm[0]
t = inputForm[1]

left = 0
right = len(numberArray) - 1

while left < right:
    if numberArray[left] + numberArray[right] < t:
        if numberArray[left] > numberArray[right]:
            right -= 1
        else:
            left += 1
    elif numberArray[left] + numberArray[right] > t:
        if numberArray[left] > numberArray[right]:
            left += 1
        else:
            right -= 1
    else:
        str(left) + " " + str(right)
        break


def add(a,b):
    return a+b

add(1,2) = 3

