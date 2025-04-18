import random

class RandomizedSet:

    def __init__(self):
        self.num_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        self.num_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        # Swaps the element to remove with the last element
        index = self.num_to_index[val]
        last_val = self.nums[-1]
        self.nums[index] = last_val
        self.num_to_index[last_val] = index
        # Remove the last element
        self.nums.pop()
        del self.num_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
