def largestRectangleArea( heights ):
    maximum=0
    stack=[]

    for i ,h in enumerate(heights +[0]):
        while stack and heights[stack[-1]]>h:
            H=heights[stack.pop()]
            if not stack:
                W=i
            else:
                W=i-stack[-1]-1
            maximum=max(maximum,H*W)

        stack.append(i)
    return maximum

heights =[2,1,5,6,2,3]
largestRectangleArea(heights)