from collections import Counter


def smallerNumbersThanCurrent( nums ):
    feven = Counter(nums)
    return feven

    

nums = [8,1,2,2,3,5,6,1,1]
print(smallerNumbersThanCurrent(nums))