# https://leetcode.com/problems/running-sum-of-1d-array
def runningSum(nums: list[int]):
    ans = [0] * len(nums)
    ans[0] = nums[0]

    for i in range(1, len(nums)):
        print(i)
        ans[i] = nums[i] + ans[i - 1]

    return ans


runningSum([1, 2, 3, 4])
