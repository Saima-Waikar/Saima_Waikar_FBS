def selection(li):
    size = len(li)
    for i in range(0,size-1):
        min_ind = i
        for j in range(i+1,size):
            if(li[j]<li[min_ind]):
                min_ind = j
        li[i],li[min_ind] = li[min_ind],li[i]

li = [60,50,40,30,20,10]
print("Before Sorting:",li)
selection(li)
print("After Sorting",li)      