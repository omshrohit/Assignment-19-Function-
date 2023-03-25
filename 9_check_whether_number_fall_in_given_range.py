# write a python program to create a function to check wheter a number falls in  a given range.

def checkElement():
    print("enter two number to the range")
    num2,num3=int(input()),int(input())
    num1=int(input("enter  the number whether you want to  check present or not"))
    min=num2 if num2<num3 else num3
    max=num2 if num2>num3 else num3
    for i in range(min,max+1):
        if num1==i:
            print("present")
            break
    else:
        print("not present")

checkElement()