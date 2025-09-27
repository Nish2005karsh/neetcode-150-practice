# Consist of string quesitns
# 1.Reverse a string in place
# def reverseStr(stringg):
#     stringg=list(stringg)
#     n=len(stringg)
#     for i in range(n//2):
#         stringg[i],stringg[n-i-1]=stringg[n-i-1],stringg[i]
#     return stringg
# stringg="hello"
# print(reverseStr(stringg))
# 2.Anagrams of each other
# def validAnagram(str1,str2):
#     if(len(str1)!=len(str2)):
#         return False
#     sorted_str1=sorted(str1)
#     sorted_str2=sorted(str2)
#     return sorted_str1==sorted_str2
# str1="listen"
# str2="silent"
# print(validAnagram(str1,str2))
# 3.Find if a string is pallindrome
# Ex->racecar
# def isPallindrom(str):
#     n=len(str)
#     for i in range(n//2):
#         if str[i]!=str[n-i-1]:
#             return False
#     return True
# str="racecar"
# print(isPallindrom(str))
# First letter of each word in upper case
# def letterBig(str):
#     str1=str.split()
#     for i  in range(len(str1)):
#         str1[i]=str1[i].capitalize()
#     return " ".join(str1)
# example_string="hi world"
# print(letterBig(example_string))

# Convert a given string into an integer
# def convertToInt(string1):
#     string2=int(string1)
#     return string2
# string1="hello"
# print(convertToInt(string1))

