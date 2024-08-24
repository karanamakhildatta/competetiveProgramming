number = input()


def square(n):
    return str(int(n) * int(n))


def square_sum(string):
    string = string.strip()
    numbers = string.split("+")
    sum = 0
    for number in numbers:
        sum += int(number)
    return str(sum)


def get_string(string):
    string = string.strip()
    equation = ""
    for number in string:
        equation += square(number) + "+"
    equation = equation[:-1]
    result = square_sum(equation)
    if len(result) == 1 and result == "1":
        return "true"
    else:
        if len(result) > 1:
            return get_string(result)
        else:
            return "false"


def totalSumOfDigits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += square(digit)
        number = number / 10
    return total_sum


def totalSumOfDigits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += square(digit)
        number = number / 10
    return total_sum


def happyNumber2(number):
    integerSum = totalSumOfDigits(number)
    if 0 < integerSum < 9:
        if integerSum == 1:
            return print("true")
        else:
            return print("false")
    else:
        happyNumber2(integerSum)


happyNumber2(number)
