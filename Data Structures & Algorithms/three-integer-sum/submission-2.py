class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            target = 0 - nums[x]


            l, r = x + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                
                elif nums[l] + nums[r] < target:
                    l += 1
                
                else:
                    res.append([nums[x], nums[l], nums[r]])


                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    

                    l += 1
                    r -= 1
        
        return res





