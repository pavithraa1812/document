class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        self.first,self.last=name.split(' ')

    @fullname.deleter
    def fullname(self):
        print("deleting name....")
        self.first=None
        self.last=None


emp1=Employee("pavithraa","sathishkumar")
emp1.first="balamithraa"
print(emp1.fullname)
print(emp1.email)
emp1.fullname="Rohit kannan"
print(emp1.fullname)
print(emp1.email)
del emp1.fullname
