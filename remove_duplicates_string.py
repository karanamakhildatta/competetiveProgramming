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
