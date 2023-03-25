#  write a python program  to create the given number is even or  odd.
def checkEvenOdd(num):
    result="even" if num%2==0 else "odd"
    print("%d is %s"%(num,result))
checkEvenOdd(int(input("enter  the number to check whether a  given number is odd or even")))