def minimumRefill(plants, capacityA, capacityB):
    left = 0
    right = len(plants) - 1
    count = 0
    aliceCap = capacityA
    bobCap = capacityB
    while left <= right:
        if left == right:
            if plants[left] > aliceCap and plants[right] > bobCap:
                count += 1
            left += 1
        else:
            if plants[left] <= aliceCap:
                aliceCap = aliceCap - plants[left] 
            else:
                count += 1
                aliceCap = capacityA
                aliceCap = aliceCap - plants[left]

            if plants[right] <= bobCap:
                bobCap = bobCap - plants[right]
            else:
                count += 1
                bobCap = capacityB
                bobCap = bobCap - plants[right]
            left += 1
            right -= 1
    return count

print(minimumRefill([4,2,2,2,1,3,3,5,3,4,2,1,2,3,3,3,5,5],5,5))