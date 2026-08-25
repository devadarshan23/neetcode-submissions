class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        for i,j in enumerate(nums): # enumnerate gives (index,value)
            pairs.append((j,i)) # value first so that it gets sorted by value below
        pairs.sort()
        left = 0
        right = len(pairs)-1

        while left < right :
            current_sum = pairs[left][0] + pairs[right][0]
            if current_sum == target :
                return sorted([pairs[left][1],pairs[right][1]])
            elif current_sum > target :
                right-=1
            else :
                left+=1