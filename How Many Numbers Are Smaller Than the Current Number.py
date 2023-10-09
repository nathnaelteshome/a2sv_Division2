def smallerNumbersThanCurrent(nums):
    sortedArr=sorted(nums)
    newArr=[]
    for i,num in enumerate(nums):
        newArr.append(sortedArr.index(num))
    return newArr



    

nums = [8,1,2,2,3,5,6,1,1]
print(smallerNumbersThanCurrent(nums))