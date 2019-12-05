class calculator:
    def __init__(self):
        print("Enter two number:")
        x=input()
        x=x.split(' ')
        self.num1=int(x[0])
        self.num2=int(x[1])

    def add(self):
        return '{}'.format(self.num1+self.num2)

    def sub(self):
        return '{}'.format(self.num1-self.num2)

    def mul(self):
        return '{}'.format(self.num1*self.num2)

    def div(self):
        if(self.num2==0):
            print("\n we cant divided by zero ,so enter the new value")
            self.num2=int(input())
            return '{}'.format(self.num1/self.num2)
        else:
            return '{}'.format(float(self.num1/self.num2))

cal1=calculator()
print("1.ADD 2.SUB 3.MUL 4.DIV")
n=int(input())
if(n==1):
    print(cal1.add())
elif(n==2):
    print(cal1.sub())
elif(n==3):
    print(cal1.mul())
elif(n==4):
    print(cal1.div())
