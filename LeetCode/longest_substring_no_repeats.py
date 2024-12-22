##FIRST TRY

# def lengthOfLongestSubstring(string):
#     max=0
#     result=[]
#     for i in range(len(string)):
#         result.append(string[0:i])
#     print(result)
#     strings=string_has_same_letter(result)
#     print(strings)
#     for i in strings:
#         if(len(i)>max):
#             max=len(i)
#     print(max)


# def string_has_same_letter(strings):
#     result = []
#     for s in strings:
#         if len(s) == len(set(s)):  # using set to check for unique letters
#             result.append(s)
#     return result
    

# Secont Try
# def lengthOfLongestSubstring( s: str) -> int:
#     if len(s) == 0:
#         return 0
#     if len(s) == 1:
#         return 1
#     max_length = 0
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             if len(s[i:j+1]) == len(set(s[i:j+1])):
#                 if len(s[i:j+1]) > max_length:
#                     max_length = len(s[i:j+1])
#     return max_length


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
        
    seen = {}  # Dictionary to store char -> position
    start = 0  # Start of current window
    max_length = 0
    
    for end, char in enumerate(s):
        print('start:',start,'end:',end)
        # print('end:',end,'char:',char)
        # If we see a char that's already in our current window,
        # move start to position after the last occurrence
        if char in seen and seen[char] >= start:
            print('char:',char,'seen[char]:',seen[char],'start:',start,'seen:',seen)  
            start = seen[char] + 1

        else:
            print(max_length, end - start + 1)
            max_length = max(max_length, end - start + 1)
            
        seen[char] = end
        print('seen:',seen)
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))
