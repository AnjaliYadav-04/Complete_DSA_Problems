class Solution:
    def processStr(self, s: str, k: int) -> str:

        lengths = []
        curr_len = 0

        # Calculate length after each operation
        for ch in s:
            if ch.isalpha():
                curr_len += 1

            elif ch == '*':
                if curr_len > 0:
                    curr_len -= 1

            elif ch == '#':
                curr_len *= 2

            elif ch == '%':
                pass

            lengths.append(curr_len)

        if k >= curr_len:
            return '.'

        # Traverse backwards
        for i in range(len(s) - 1, -1, -1):

            ch = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0

            if ch.isalpha():

                if k == prev_len:
                    return ch

            elif ch == '*':

                pass

            elif ch == '#':

                if prev_len > 0:
                    k %= prev_len

            elif ch == '%':

                k = curr_len - 1 - k

            curr_len = prev_len

        return '.'
