# Author RTS 12/9/21

def count_evens(lst):
    total = 0
    x = 0
    while x < len(lst):
        if lst[x] % 2 != 0:
            total += 0
        break
    else:
        if lst[x] % 2 == 0:
            total += x
            x += 1
    return total
