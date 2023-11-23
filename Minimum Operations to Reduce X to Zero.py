def minOperations( nums, x) :
        total = sum(nums)
        target = total-x
        n=len(nums)
        if total == x :return n

        curr_sum = 0
        left = 0
        maxLen = -1

        for right in range(n):
            curr_sum += nums[right]
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left +=1
            if curr_sum == target:
                maxLen = max(maxLen, right - left +1)
            
        return -1 if maxLen == -1 else n - maxLen

nums = [3,2,20,1,1,3]
x = 10

print(minOperations(nums,x))