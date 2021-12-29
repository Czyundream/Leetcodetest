#两数之和
#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

#采用哈希表
class Solution:
    def twoSum(nums, target):
        ans = dict()
        for idx, val in enumerate(nums):
            if target - val not in ans:
                ans[val] = idx
            else:
                return [ans[target - val], idx]

'''
nums = [11,15,2,7]
target = 9
print(Solution.twoSum(nums,target))
'''
#枚举法
class Solution:
    def twoSum(nums, target) :
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

nums = [11,15,2,7]
target = 9
print(Solution.twoSum(nums,target))