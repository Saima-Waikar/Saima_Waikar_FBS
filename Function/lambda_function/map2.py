def chk(num):
    if(num%2==0):
        return 'Even'
    else:
        return 'odd'
data =  [1,2,3,4,5,6,7]
res = list(map(chk,data))
print(res)