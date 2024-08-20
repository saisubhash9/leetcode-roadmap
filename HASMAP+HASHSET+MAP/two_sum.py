# brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
                    return ans



# using hash map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hash_map:
                return [hash_map[compliment], i]
            hash_map[nums[i]] = i
        return []
