string = input()
memory = {}

# store the colors of the rods in a dictionary
for i in range(0, len(string), 2):
    rod = string[i + 1]
    color = string[i]
    if rod in memory:
        memory[rod].append(color)
    else:
        memory[rod] = [color]

# check if all the colors like red, green, blue are present in the memory
count = 0
for rod in memory:
    memory[rod] = set(memory[rod])
    print(len(memory[rod]))
    if len(memory[rod]) == 3:
        count += 1

print(count)
