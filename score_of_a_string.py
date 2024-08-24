# scrore of a
string = input("Enter a string")
# tip i, i+1
# range = n-1
sum = 0
for i in range(len(string) - 1):
    sum += abs(ord(string[i]) - ord(string[i + 1]))
print(sum)
# ascii value python -> ord()
# absolute difference -> abs()
# range -> range()
