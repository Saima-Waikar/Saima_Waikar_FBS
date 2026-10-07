# 1. Direct import
import mypackage.abc
mypackage.abc.greet()


# 2. From package import member
from mypackage.abc import greet
greet()


# 3. From package import all members
from mypackage.abc import *
greet()
print(name)


# 4. Import with alias
import mypackage.abc as a
a.greet()
print(a.name)