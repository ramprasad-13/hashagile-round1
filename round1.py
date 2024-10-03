# Longest Palindromic Substring
# Write a program to find the longest palindromic substring in a given string without using any built-in 
# substring or reverse functions. For example, for input "babad", the output should be "bab" or "aba".
# Instructions: Avoid using any string handling libraries. Implement a solution that checks all substrings 
# manually

#checking if is string palindrome or not using two pointer approach
def isPalindrome(s):
    left=0
    right= len(s)-1
    while(right>left):
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

#writing a method to get all substrings and update the longest substring plaindome in variable and return it
def getLongestPlindromeSubstring(s):
    res=''
    for i in range(len(s)):
        for j in range(i,len(s)):
            temp=s[i:j+1]
            if isPalindrome(temp):
                if(len(temp)>len(res)):
                    res=temp
    return res

#Give input here
s = input("Enter a string : ")
print(getLongestPlindromeSubstring(s))


#sample inputs and outputs
#ramprasad - asa
#hashagile - h
#babad -bab
