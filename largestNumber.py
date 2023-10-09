def largestNumber( nums ) :
        stringifiedArr = [str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(0,len(nums)-i):
                if j + 1 < len(nums):
                    first,second=stringifiedArr[j][0],stringifiedArr[j + 1][0]
                    if first < second:
                        stringifiedArr[j], stringifiedArr[j + 1] = stringifiedArr[j + 1], stringifiedArr[j]
                    elif stringifiedArr[j][0] == stringifiedArr[j + 1][0]:
                        l = int("".join(stringifiedArr[j] + stringifiedArr[j+1]))
                        r = int("".join(stringifiedArr[j+1] + stringifiedArr[j]))
                        if l < r:
                            stringifiedArr[j], stringifiedArr[j + 1] = stringifiedArr[j+1],stringifiedArr[j]
        return str(int("".join(stringifiedArr)))

nums = [3,30,34,5,9]
print(largestNumber(nums))