import math
# function


def findMaxAverage( nums, k) :
        l = 0
        r = k - 1
        count = -math.inf
        av = nums[l:r+1]
        sum1 = sum(av)
        while r < len(nums):
            count = max(count, sum1)
    #   [2,5,5,6,8,8]
            r += 1
            sum1=sum1-nums[l]+nums[r]
            l += 1
        return count / k

print(findMaxAverage([1,12,-5,-6,50,3],4))