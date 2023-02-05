def breakPalindrome(palindromeStr):
    # variable to detect if change was possible
    flag = 0
    # make list out of string
    listStr = list(palindromeStr)

    # if list/string size is even
    if (len(listStr) % 2 == 0):
        # iterate first half characters
        for i in range(0, int(len(listStr) / 2)):
            # if there's a character that's not a, change it to a
            # set flag and break loop
            if (listStr[i] != 'a'):
                listStr[i] = 'a'
                flag = 1
                break
    # if list/string size is odd
    else:
        # iterate first half characters
        for i in range(0, int(len(listStr) / 2)):
            # if there's a character that's not a, change it to a
            # set flag and break loop
            if (listStr[i] != 'a'):
                listStr[i] = 'a'
                flag = 1
                break

    # if flag is set, join list and return
    if flag == 1:
        return ''.join(listStr)

    # else return IMPOSSIBLE
    return 'IMPOSSIBLE'

# Write your code here
if __name__ == '__main__':
    print(breakPalindrome('aaabbaaa'))
    print(breakPalindrome('aaa'))
    print(breakPalindrome('bab'))
    print(breakPalindrome('acca'))
