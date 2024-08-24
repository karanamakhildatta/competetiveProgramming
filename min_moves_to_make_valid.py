def min_moves_to_make_valid(S):
    open_needed = 0
    close_needed = 0

    for ch in S:
        if ch == "(":
            close_needed += 1
        elif ch == ")":
            if close_needed > 0:
                close_needed -= 1
            else:
                open_needed += 1

    return open_needed + close_needed


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def count_primes(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count


def solve(S):
    M = min_moves_to_make_valid(S)
    return count_primes(M)


string = input()
result = solve(string)
print(result)
