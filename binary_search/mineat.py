def minEatingSpeed(piles,h):
    left,right=0,max(piles)
    while left<=right:
        mid=left+(right-left)//2
        hours=0
        for pile in piles:
            hours+=pile//mid
            if pile%mid>0:
                hours+=1
            if hours<=h:
                right=mid-1
            else:
                left=mid+1
    return left
piles=[3,6,7,11]
h=8
print(minEatingSpeed(piles,h))