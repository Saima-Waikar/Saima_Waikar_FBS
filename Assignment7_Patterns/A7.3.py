for i in range(1,6):
    for j in range(1,i+1):
        if(i==5 or i==j):
            print(j,end=" ")
        elif(j==1):
            print("1",end=" ")
        else:
            print(" ",end=" ")
    print(' ')