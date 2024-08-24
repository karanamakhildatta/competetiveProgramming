# IMP TIPS
# for shortest Maximimum -> INT_MAX, array[0]
# for largest / longest -> 0, INT_MIN


# Find the Longest Word in a String
def findLongestWord(string):
    string = string.strip()
    words = string.split(" ")
    longestLength = 0  # INT_MIN
    longestWord = ""
    for i in range(len(words)):
        if len(words[i]) > longestLength:
            longestWord = words[i]
            longestLength = len(words[i])
    return longestWord
