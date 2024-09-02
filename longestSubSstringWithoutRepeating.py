s = "pwwkew"

def lengthOfLongestSubstring(s):

    chars = {}

    start = 0
    end = 0
    diff = -1

    for i in range(len(s)):
        
        end = i

        if not chars.get(s[i]):
            chars[s[i]] = 0

        chars[s[i]] += 1

        while (chars[s[i]] > 1):
            chars[s[start]] -= 1
            start += 1

        if end - start > diff:
            diff = end - start 

    return diff + 1

print(lengthOfLongestSubstring(s))