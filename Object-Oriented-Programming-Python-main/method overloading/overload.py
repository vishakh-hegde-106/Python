class student:
        def show(self,name=None,age=None,grade=None):
                if(name==None and age==None and grade==None):
                        print("no data given")
                        print("-------------------")
                elif(age==None and grade==None):
                        self.name=name
                        print("name is",self.name)
                        print("--------------------")
                elif(grade==None):
                        self.name=name
                        self.age=age
                        print("name is",self.name)
                        print("age is",self.age)
                        print("--------------------")
                else:
                        self.name=name
                        self.age=age
                        self.grade=grade
                        print("name is",self.name)
                        print("age is",self.age)
                        print("grade is",self.grade)
                        print("--------------------")
s=student()
while True:
        print("1.no argument \n 2.one argument \n 3.two arguments \n 4.three arguments")
        c=int(input("enter your choice"))
        if(c==1):
                s.show()
        elif(c==2):
                s.show("Vishakh")
        elif(c==3):
                s.show("Vishakh",13)
        elif(c==4):
                s.show("Vishakh",13,90)
        else:
                break
