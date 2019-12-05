class developer:
	def __init__(self,name,email,domain):
		self.name=name
		self.email=email
		self.domain=domain
	def fun(self):
		return self.name

class employee:
	def __init__(self):
		print("Enter the value:")
		self.firstname=input()
		self.lastname=input()
	def fullname(self):
		return '{} {}'.format(self.firstname,self.lastname)


dev1=developer('mithra','mithra@gmail.com','dental')
print(dev1.name+' '+dev1.email+' '+dev1.domain)
print(dev1.fun())

emp1=employee()
print("Full Name:"+emp1.fullname())
