def longestPalindrome(input_str):
    if len(input_str) < 1:
        return " "

    
    #Initialize Tracking Variables

    res = ""
    reslen = 0

    #Iterate Through Each Character

    for i in range(len(input_str)):

        #odd length
        l, r = i, i
        while l >= 0 and r < len(input_str) and input_str[l] == input_str[r]:
            if (r - l + 1) > reslen:
                res = input_str[l:r+1]
                reslen = r - l + 1
            l -= 1
            r += 1

        #even length 
