def conqure(li,start,mid,stop):
    left=start
    right=mid+1
    temp=[]
    while left<=mid and right<=stop:
        if li[left]<=li[right]:
            temp.append(li[left])
            left+=1
        else:
            temp.append(li[right])
            right+=1
    while left<=mid:
        temp.append(li[left])
        left+=1
    while right<=stop:
        temp.append(li[right])
        right+=1
    for i in range(len(temp)):
        li[start+i]=temp[i]
def divide(li,start,stop):
    if start<stop:
        mid=(start+stop)//2
        divide(li,start,mid)
        divide(li,mid+1,stop)
        conqure(li,start,mid,stop)
li=[12,2,33,5]
print(f"Unsorted list={li}")
divide(li,0,len(li)-1)
print(f"Sorted List={li}")