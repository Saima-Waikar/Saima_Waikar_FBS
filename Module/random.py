import random
print(random.random())
print(random.random()*10000)
print(int(random.random()*1000))
print(random.randint(2,10))
print(random.randrange(100,1000))
li=["apple","mango","banana","grapes"]
print(random.choice(li))
print(random.shuffle(li))