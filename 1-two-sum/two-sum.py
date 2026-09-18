class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]

# The code above has time complexily of O(n^2) because it is looping through the array n*n times.

class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in nums:
            needed_index = nums.index(needed)
            if needed_index != i: 
                return [needed_index, i]

#This doesn't use nested loops but it is still O(n^2) becuase it looks through all the elements when checking if "needed" is in "nums" and getting index of the complement.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in checked:
                return [checked[needed], i]
            checked[num] = i

#The dictionary method is significantly faster because searching a dictionary takes O(1) constant time, while searching a list takes O(n) linear time.