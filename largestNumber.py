def largestNumber( nums ) :
        st = [str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i,len(nums)-i):
                if j + 1 < len(nums):
                    first,second=st[j][0],st[j + 1][0]
                    if first < second:
                        st[j], st[j + 1] = st[j + 1], st[j]
                    elif st[j][0] == st[j + 1][0]:
                        l = int("".join(st[j] + st[j+1]))
                        r = int("".join(st[j+1] + st[j]))
                        if l < r:
                            st[j], st[j + 1] = st[j+1],st[j]
        return str(int("".join(st)))

nums = [3,30,34,5,9]
print(largestNumber(nums))