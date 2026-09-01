def binarysearch(li,searchele):
    beg = 0
    end = len(li) - 1
    while(beg<=end):
        mid = (beg+end)//2
        if(searchele==li[mid]):
            return mid
        elif(searchele<li[mid]):
            end = mid - 1
        elif(searchele>li[mid]):
            beg = mid + 1
    else:
            return -1

li = [10,20,30,40,50,60]
ele = int(input("Enter element to be searched:"))
res = binarysearch(li,ele)
if(res!=-1):
    print(f"{ele} is present in the list at index {res}")
else:
    print(f"{ele} is not present in the list")

