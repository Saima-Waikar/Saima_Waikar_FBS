#pass
for i in range(1, 10):
    pass                  #to neglect expected indented block error

#break
for i in range(1, 10):
    if (i == 3):
        break            #to stop loop
    print(i)

#continue
for i in range(1, 10):
    if (i == 3):           #3 is not getting print it will stop current iteration
        continue
    print(i)

#else
for i in range(1, 10):
    if (i == 5):          
         continue
    print(i)
else:
    print("Else excuted")


#else
for i in range(1, 10):
    if (i == 5):          
         break
    print(i)
else:
    print("Else excuted")