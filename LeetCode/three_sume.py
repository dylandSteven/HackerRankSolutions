from typing import List
import collections

class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     def detect_duplicate(self, nums: List[int],matrix: List[int]) :
    #         for i in range(len(matrix)):
    #             if collections.Counter(matrix[i]) == collections.Counter(nums):
    #                 return True
    #         return False
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             for k in range(j+1,len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0 and   i != j and j != k and i != k and detect_duplicate(self,[nums[i] , nums[j] , nums[k]],result) == False:
    #                     result.append([nums[i] , nums[j] , nums[k]])
    #     print(result)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n= len(nums)
        nums.sort()
        for i in range(n-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left< right:
                total = nums[i]+ nums[left]+ nums[right]
                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

solution = Solution()
# solution.threeSum([-1,0,1,2,-1,-4])