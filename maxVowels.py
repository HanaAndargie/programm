class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        count = 0
        vowels = "aeiou"
        
        for right in range(k):
            if s[right] in vowels:
                count += 1

        max_count = count
        
        for right in range(k, len(s)):            
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            left += 1
            max_count = max(max_count, count)
