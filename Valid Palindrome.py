class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_chars = [char.lower() for char in s if char.isalnum()]
        filtered_str = ''.join(filtered_chars)
        return filtered_str == filtered_str[::-1]
