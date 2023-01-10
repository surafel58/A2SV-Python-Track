class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []

        middle = num // 3
        left = middle - 1
        right = middle + 1

        return [left, middle, right]
