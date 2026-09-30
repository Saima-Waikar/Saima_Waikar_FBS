class list:
    def __init__(self,l1,l2):
        self.l1 = l1
        self.l2 = l2
    def display(self):
        print(self.l1+self.l2)
l=list([1,2,3],[4,5,6])
l.display()