d=int(input("enter your choice"))
print("1.string \n 2. tuple \n 3.exit")      
while True:
    if(d==1):
        n1=input("Enter a First String")
        n2=input("Enter a Second String")
        while True:
            print('1.length of the string')
            print('2.concatenation of the string')
            print('3.maximum of string')
            print('4.minimum of string')
            print('5.sorting of string')
            print('6.reverse of string')
            print('7.upper of string')
            print('8.lower of string')
            print('9.Replace Character')
            print('10.Split a String into List')
            ch = int(input('Enter the Number'))
            if ch == 1:
                print(len(n1))
            elif ch == 2:
                print(n1+n2)
            elif ch == 3:
                print(max(n1))
            elif ch == 4:
                print(min(n1))
            elif ch == 5:
                print(sorted(n1))
            elif ch == 6:
                print(n1[::-1])
            elif ch == 7:
                print(n1.upper())
            elif ch == 8:
                print(n1.lower())
            elif ch == 9:
                print(n1.replace("b","a"))
            elif ch == 10:
                print(n1.split())
            else:
                break
    elif(d==2):
        t1 = tuple(input("Enter the tuple: "))
        t2 = tuple(input("Enter the tuple: "))
        while True:
            print("1. Extract a element from tuple ")
            print("2. Length of tuple")
            print("3. Combine two tuples")
            print("4. Repetition of elements in tuple")
            print("5. Count a element in tuple")
            print("6. Print max value in tuple")
            print("7. Print min value in tuple")
            print("8. Convert a tuple to list")
            print("9. Print the last element of tuple")
            print("10. Extract a part of tuple")
            print("0. Exit")
            ch = int(input("Enter the choice: "))
            if ch == 1:
                c = int(input("Enter location: "))
                print(t1[c])
            elif ch == 2:
                print(len(t1))
            elif ch == 3:
                print (t1 + t2)
            elif ch == 4:
                t1=readinput()
                print(t1 * 2)
            elif ch == 5:
                i = input("Enter the element to count: ")
                print(t1.count(i))
            elif ch == 6:
                print(max(t1))
            elif ch == 7:
                print(min(t1))
            elif ch == 8:
                l = list(t1)
                print(l)
            elif ch == 9:
                print(t1[-1])
            elif ch == 10:
                s = int(input("Enter starting index: "))
                e = int(input("Enter ending index: "))
                print(t[s:e])
    else:
        exit()


    
   
