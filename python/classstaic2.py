import datetime

class Employee:
    num_of_emp=0
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+last+'@gmail.com'
        self.pay=pay

    def empname(self):
        return '{} {}'.format(self.first,self.last)

    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amt=amt

    @classmethod
    def from_str(cls,emp):
        first,last,pay=emp.split(',')
        return cls(first,last,pay)

    @staticmethod
    def workingday(day):
        if day.weekday() ==5 or day.weekday() ==6:
            return False
        return True

emp1=Employee('pavithraa','sathish',50000)
print(emp1.email)
print(emp1.empname())
print(emp1.raise_amt)
emp1.set_raise_amt(1.05)
print(emp1.raise_amt)

emp2='mithra,sathish,50000'
new_emp2=Employee.from_str(emp2)
print(new_emp2.email)
print(new_emp2.empname())

my_date=datetime.date(2016, 12, 19)
print(Employee.workingday(my_date))
