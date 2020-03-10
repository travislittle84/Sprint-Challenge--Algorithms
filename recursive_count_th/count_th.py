'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    # base (we'll be removing the first element at the end of recursive case) 
    if len(word) <= 1:
        return 0
    
    # recursive case

    # check if the first two letters equal th
    if word[0:2] == 'th':
        return count_th(word[1:]) + 1 # +1 for match and remove first letter from word in function call
    # remove letter from word and call function with out + 1 because no match
    return count_th(word[1:])

# print(count_th("abcthefgtht"))