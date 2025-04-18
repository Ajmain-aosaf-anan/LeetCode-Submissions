class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initializes two pointers
        s_pointer, t_pointer = 0, 0

        # Iterates through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If characters match, move the s pointer
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Always move the t pointer
            t_pointer += 1

        # Checks if all characters of s were found in t
        return s_pointer == len(s)
