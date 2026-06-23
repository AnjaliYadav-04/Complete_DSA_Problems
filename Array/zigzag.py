class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        num_values = r - l + 1
        
        # Base case for an array of length 2
        # dp_inc[i] stores ways to end at value (l + i) via an increasing step
        # dp_dec[i] stores ways to end at value (l + i) via a decreasing step
        dp_inc = [i for i in range(num_values)]
        dp_dec = [num_values - 1 - i for i in range(num_values)]
        
        # Iterate from length 3 up to n
        for _ in range(3, n + 1):
            next_inc = [0] * num_values
            next_dec = [0] * num_values
            
            # Prefix sum of dp_dec to optimize the increasing transitions
            prefix_sum = 0
            for i in range(num_values):
                next_inc[i] = prefix_sum % MOD
                prefix_sum += dp_dec[i]
                
            # Suffix sum of dp_inc to optimize the decreasing transitions
            suffix_sum = 0
            for i in range(num_values - 1, -1, -1):
                next_dec[i] = suffix_sum % MOD
                suffix_sum += dp_inc[i]
                
            dp_inc = next_inc
            dp_dec = next_dec
            
        # The total number of valid arrays is the sum of all configurations at length n
        return (sum(dp_inc) + sum(dp_dec)) % MOD
