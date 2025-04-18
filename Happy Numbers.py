class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum_of_squares(num: int) -> int:
            return sum(int(digit) ** 2 for digit in str(num))

        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = get_sum_of_squares(n)

        return True
