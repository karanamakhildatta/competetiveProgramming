string = "Hello"
integervalue = 5
floatValue = 5.5
listValue = [1, 2, 3, 4]
tupleValue = (1, 2, 3, 4)
dictionaryValue = {"name": "udaya", "age": 25}
booleanValue = True
setValue = {1, 2, 3, 4}

# # conditional statements
# if integervalue == 5:
#     print("Integer value is 5")
# elif floatValue == 5.5:
#     print("Float value is 5.5")
# elif string == "Hello":
#     print("String value is Hello")
# else:
#     print("No match found")

# Logical Operators
# && -> and
# and
# # || -> or
# or
# in
# not or !
# !=
# ==
# ===
# <=
# >=
# <
# >

# listValue = [1, 2, 3, 4]
# Process 1 each element in list
# for value in listValue:
#     print(value)
# Process 2 each element in list
# len(list||tuple||string||dictionary||set)
# n = len(listValue)
# for i in range(len(tupleValue)):
# for i in range(n):
#     print(listValue[i])
# range(lowerlimit, upperlimit, step)
# for i in range(0, 10, 4):
#     print(i)

listValue.append(5)
# for i in range(len(listValue)):
#     print(listValue[i])

# listValue2 = listValue.copy()

# for i in range(len(listValue2)):
#     print(listValue2[i])

# listValue.extend([6, 7, 8])
# for i in range(len(listValue)):
#     print(listValue[i])
# print(listValue.index(4))
# difference between list and tuple
# list is mutable and tuple is immutable
# functions of list:


# Find the Longest Word in a String
def findLongestWord(string):
    string = string.strip()
    words = string.split(" ")
    longestLength = 0  # INT_MIN
    longestWord = ""
    # for word in words:
    #     if len(word) > longestLength:
    #         longestWord = word
    #         longestLength = len(word)
    for i in range(len(words)):
        if len(words[i]) > longestLength:
            longestWord = words[i]
            longestLength = len(words[i])
    return longestWord


# IMP TIPS
# for shortest Maximimum -> INT_MAX, array[0]
# for largest / longest -> 0, INT_MIN


# Find the Shortest Word in a String


def findShortestWord(string):
    string = string.strip()
    words = string.split(" ")
    shortestLength = len(words[0])
    shortestWord = words[0]
    shortestWords = []
    shortestWordsString = ""
    for word in words:
        if len(word) < shortestLength:
            shortestWord = word
            shortestLength = len(word)
            shortestWords.append(word)
            shortestWordsString += word + " "
        elif len(word) == shortestLength:
            shortestWords.append(word)
            shortestWordsString += word + " "

    # for word in words:
    #     if len(word) < shortestLength:
    #         shortestWord = word
    #         shortestLength = len(word)
    return shortestWordsString


# "My name is Udaya Sree"

# ["My", "name", "is", "Udaya", "Sree"]

# longestLength = 0
# 2 > 0
# longestWord = "My"
# longestLength = 2
# 4 > 2
# longestWord = "name"
# longestLength = 4
# 2 > 4
# 5 > 4
# longestWord = "Udaya"
# longestLength = 5

# longestWord = "Udaya"
print(findLongestWord("My name is Udaya Sreee"))
print(findShortestWord("My name is Udaya Sree"))
