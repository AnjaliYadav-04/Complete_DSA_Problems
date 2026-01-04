class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len=0
        char_set=set()
        for right in range(len(s)): 
         while s[right] in char_set:
             char_set.remove(s[left])
             left+=1
         char_set.add(s[right])   
         max_len=max(max_len, right-left+1)
        return max_len

if __name__ == "__main__":
    solution = Solution()

    # Example inputs
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "",
        "abcdefg"
    ]

    for s in test_cases:
        result = solution.lengthOfLongestSubstring(s)
        print(f'Input: "{s}" --> Length of Longest Substring Without Repeating Characters = {result}')