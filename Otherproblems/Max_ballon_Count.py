class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}

        # Count frequency of each character
        for ch in text:
            count[ch] = count.get(ch, 0) + 1

        # Find maximum possible balloons
        return min(
            count.get('b', 0),
            count.get('a', 0),
            count.get('l', 0) // 2,
            count.get('o', 0) // 2,
            count.get('n', 0)
        )
