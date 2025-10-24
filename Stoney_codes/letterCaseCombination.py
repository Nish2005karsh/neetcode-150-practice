def letterCasePermutations(str):
    output=[""]
    for c in s:
        tmp=[]
        if c.isalpha():
            for o in output:
                tmp.append(o+c.lower())
                tmp.append(o+c.upper())
        else:
            for o in output:
                tmp.append(o+c)
        output=tmp
    return output

s = "a1b2"
print(letterCasePermutations(s))
#)
# Output is ["a1b2","a1B2","A1b2","A1B2"]