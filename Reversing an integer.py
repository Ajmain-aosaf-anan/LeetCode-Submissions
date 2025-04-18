class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Stores the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Checks for overflow before actually adding the digit
            if (reversed_num > INT_MAX // 10) or (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            if (reversed_num < INT_MIN // 10) or (reversed_num == INT_MIN // 10 and -digit < INT_MIN % 10):
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num
