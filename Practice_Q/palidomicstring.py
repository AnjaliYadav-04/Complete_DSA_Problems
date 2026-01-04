class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0  
        
        def expandAroundCenter(left: int, right: int) -> int:
            # Expand while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  
        
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)    
            len2 = expandAroundCenter(i, i + 1)  
            max_len = max(len1, len2)
            
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]



if __name__ == "__main__":
   
    s = input("Enter a string: ")
    
    solution = Solution()
    result = solution.longestPalindrome(s)
    
    print("Longest Palindromic Substring:", result)