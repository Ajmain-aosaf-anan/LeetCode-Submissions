class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge cases for numRows being 1 or greater than or equal to the length of s
        if numRows == 1 or numRows >= len(s):
            return s

        # Initializes a list for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterates through each character in the string
        for char in s:
            rows[current_row] += char
            # Changes direction at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Updates the current row based on the direction
            current_row += 1 if going_down else -1

        # Concatenates all rows to get the final result
        return ''.join(rows)
