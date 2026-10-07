#1.Direct import
import M1
M1.add(12,4)
print(M1.pname)

#2.from modulename import member
from M1 import add
add(9,3)

#3.from modulename import members
from M1 import add,pname
add(9,3)
print(pname)

#4.from modulename import all(*)
from M1 import*
add(12,4)
sub(12,3)
print(pname)

#5.Alicename()
import M1 as m
m.add(9,7)
m.sub(12,7)
print(m.pname)