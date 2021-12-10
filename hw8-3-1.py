# Author RTS 12/9/21

def count_odds(lst):
    x = 0
    total = 0
    while x < len(lst):
        if lst[x] % 2 != 0:
            total += 1
        x += 1
   
    return total
