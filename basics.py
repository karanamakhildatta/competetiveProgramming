string = "Hello"
integervalue = 5
floatValue = 5.5
listValue = [1, 2, 3, 4]
tupleValue = (1, 2, 3, 4)

dictionaryValue = {"name": "udaya", "age": 25}
booleanValue = True
setValue = {1, 2, 3, 4}
listTupleValues = list(tupleValue)
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


# "   My name is is Udaya Sree   "

# dict = {"word": "meaning"}
# dict2 = {"udaya": 5, "sree": 4, "akhil": 5, "ramesh": 6}
# dict3 = {
#     "andhra pradesh": "Amaravati",
#     "telangana": "Hyderabad",
#     "tamilnadu": "Chennai",
# }
# print("Capital of Andhra Pradesh is", dict3["andhra pradesh"])
# dict3["karnataka"] = "Banglore"
# print("Capital of Karnataka is", dict3["karnataka"])

# find andhrapradesh is in dict3
# if "andhrapradesh" in dict3:
#     print("Yes")
# "My name is is Udaya Sree"
# words = ['My',"Name","is","is","Udaya","Sree"]
# for word in words:
#     if memory[word]

# remove duplicates and return the string
# remove duplicates and return an array
# remove duplicates and return a dictionary
# remove duplicates and return a set
# remove duplicates and return a tuple
# string = "My name is is akhil akhil"
# result = ""
# array = []
# dict = {}
# set = set()
# tuple_array = tuple(array)
# [1, 2, 3, 4]
# (1, 2, 3, 4)
# [{1: "udaya"}, {2: "sree"}]
# list_array = list(array)


# Remove Duplicate Words in a String
string = input("Enter a string")


# Remove Duplicate Words in a String
def removeDuplicateWords(string):
    string = string.strip()
    words = string.split(" ")
    result = ""
    memory = {}
    for word in words:
        # lowerCaseWord = word.lower()
        if word not in memory:
            result = result + word + " "
            memory[word] = True
    return result.strip()


# Remove Duplicate Words in a String irrespective of case
def removeDuplicateWordsCaseIrrespective(string):
    string = string.strip()
    words = string.split(" ")
    result = ""
    memory = {}
    for word in words:
        lowerCaseWord = word.lower()
        if lowerCaseWord not in memory:
            result = result + word + " "
            memory[lowerCaseWord] = True
    return result.strip()


# result =  "Akhil"
# word = input("Enter your last name")
# full_name = result + " " + word
# result = result + " " + word


# " My name is is udaya sree "
# "My name is udaya sree"

# words = ["My", "my" "name", "is", "is", "udaya", "sree"]
# result = ""
# memory = {}

# word = "My"
# result = "My "
# memory["my"] = True
# memory = {"my": True}

# word = "my"

# word = "name"
# result = "My name "
# memory["name"] = True
# memory = {"My": True, "name": True}

# word = "is"
# result = "My name is "
# memory["is"] = True
# memory = {"My": True, "name": True, "is": True}

# word = "is"

# word = "Udaya"
# result = "My name is Udaya "
# memory["Udaya"] = True
# memory = {"My": True, "name": True, "is": True, "Udaya": True}

# word = "Sree"
# result = "My name is Udaya Sree "
# memory["Sree"] = True
# memory = {"My": True, "name": True, "is": True, "Udaya": True, "Sree": True}
# result.strip()
word1 = input("Enter word1")
print(removeDuplicateWords(word1))
word2 = input("Enter word2")
print(removeDuplicateWords(word2))
word3 = input("Enter word3")
print(removeDuplicateWords(word3))

n = int(input("Enter number of words:"))
sentences = []
for i in range(n):
    sentence = input("Enter Sentence:")
    sentences.append(sentence)
for sentence in sentences:
    print(removeDuplicateWords(sentence))

# Reverse Only Letters
# "My name i123!@#s Udaya Sree 123!@#"
# "eerS ayadU s1i eman yM 123"
# "Udaya Sree"
