def collatz(n):
    string = str(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        string += "," + str(n)
    return string

print(collatz(3))