class Solution:
    def romanToInt(self, s: str) -> int:
        # Map Roman symbols to integer values
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If current value is less than the next, subtract it
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        return total
sol = Solution()
print(sol.romanToInt("III"))       # Output: 3
print(sol.romanToInt("LVIII"))     # Output: 58
print(sol.romanToInt("MCMXCIV"))   # Output: 1994
