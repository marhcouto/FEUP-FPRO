#ZERO SUM TRIPLET



def triplet(atuple):
    final_tuple = ()
    for i in atuple:
        for n in atuple:
            for r in atuple:
                if i == n or i == r or n == r:
                    break
                elif i + n + r == 0:
                    final_tuple = (r, n, i)
    return final_tuple

print(triplet((-5, -4, -1, 4, 2, -2, -7, -4)))
            
            
        