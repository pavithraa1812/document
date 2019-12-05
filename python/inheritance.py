#creating a new class from existing class
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

class Developer(Employee):
    raise_amt=1.05
    def __init__(self,first,last,pay,prog_lan):
        super().__init__(first,last,pay)
        self.prog_lan=prog_lan

class Manger(Employee):
    def __init__(self,first,last,pay,employee=None):
        super().__init__(first,last,pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee

    def add_list(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_list(self):
        if emp in self.employee:
            self.employee.remove(emp)

    def str(self):
        for emp in self.employee:
            print(emp.empname())

class Empdetails(Developer):
    def __init__(self,first,last,pay,prog_lang,skill=None):
        super().__init__(first,last,pay,prog_lang)
        if skill is None:
            self.skill=[]
        else:
            self.skill=skill

    def add_list1(self,s):
        if s not in self.skill:
            self.skill.append(s)

    def details(self):
            return '{}'.format(self.skill)


dev1=Developer('Pavithraa','Sathish',50000,'python')
dev1.amt()
print(dev1.empname())
print(dev1.prog_lan)
mg1=Manger('Mithra','Sathish',60000,[dev1])
mg1.str()
print(isinstance(mg1,Employee))
print(issubclass(Manger,Employee))
det1=Empdetails('Pavithraa','Sathish',50000,'python',['C','C++'])
det1.add_list1('java')
print(det1.details())
