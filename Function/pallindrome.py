def pallindrome(num):
    temp = num
    reverse = 0
    while(temp>0):                   #to seperate out digit this is used
        d = temp % 10
        temp = temp // 10
        reverse = reverse * 10 + d          #to reverse this is used 
    if(num==reverse):
        return True
    else:
        return False

n = int(input("Enter a number:"))    
print(pallindrome(n))
