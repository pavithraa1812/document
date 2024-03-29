class Employee:
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+last+'@gmail.com'
        self.pay=pay

    def empname(self):
        return '{} {}'.format(self.first,self.last)

    def amt(self):
        self.pay=int(self.pay*self.raise_amt)

    def __repr__(self):
        return '{} , {} , {}'.format(self.first,self.last,self.email)

    def __str__(self):
        return '{}'.format(self.pay)

    def __add__(self,other):
        return self.pay+other.pay

    def __len__(self,v):
        return len(v)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
#operator overloading
print(1000+100000)
str1='Pavithraa'
str2='Sathish'
print(str1+str2)

#inbulid function
print(int.__add__(100,10000))
print(str.__add__(str1,str2))

emp1=Employee(str1,str2,50000)
emp2=Employee('mithra',str2,30000)

print(emp1.__repr__())
print(emp1.__str__())

print(emp1.pay + emp2.pay)
print(emp1.__len__(emp1.empname()))
