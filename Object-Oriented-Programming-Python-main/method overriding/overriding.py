class Employee:
    def __init__(self):
        self.first=input("Enter the First name")
        self.last=input("Enter the Last name")
        self.empid=input("Enter the Emp ID")
        self.pay=int(input("Enter the Salary"))

    def display(self):
        print("first name:", self.first)
        print("last name:", self.last)
        print("empid=",self.empid)
        print("pay=", self.pay)

    def pay_raise(self):
        self.pay=int(self.pay)*1.5

class Developer(Employee):
    def pay_raise(self):
        self.pay=int(self.pay)*2.5

class Manager(Employee):
    def pay_raise(self):
        self.pay=int(self.pay)*3.5

e1=Employee()
e2=Manager()
e1.pay_raise()
e2.pay_raise()
e1.display()
e2.display()


