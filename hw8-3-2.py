# Author RTS 12/9/21

def three_letter_words(lst):
    x = 0
    total = 0
    while x < len(lst):
        if len(lst[x]) == 3:
            total += 1
        x += 1
   
    return total
