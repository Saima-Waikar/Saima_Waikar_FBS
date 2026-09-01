def linearsearch(li,searchele):
    for ind in range(0,len(li)):
        if(searchele == li[ind]):
            return ind
    else:
        return -1

li = [45,67,89,43,21,34,65,78,90]
searchele = int(input("Enter number to searched:"))

res = linearsearch(li,searchele)
#print(res)
if(res!=-1):
    print(f"{searchele} element is present in list")
else: 
    print(f"{searchele} element is not present in the list")