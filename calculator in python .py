print("1. Add ")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")
print("5. Modulas")

method=input("Enter the method : \n "  )

if method=="1":
    num1=int(input("Enter a number : \n"))
    num2=int(input("Enter a number : \n"))
    print("THE ANSWER IS ",num1+num2)
elif method=="2":
    num1=int(input("Enter a number : \n"))
    num2=int(input("Enter a number : \n"))
    print("THE ANSWER IS ",num1-num2)

elif method=="3":
    num1=int(input("Enter a number : \n"))
    num2=int(input("Enter a number : \n"))
    print("THE ANSWER IS ",num1*num2)

elif method=="4":
    num1=int(input("Enter a number : \n"))
    num2=int(input("Enter a number : \n"))
    print("THE ANSWER IS ",num1/num2)
else:
    num1=int(input("Enter a number : \n"))
    num2=int(input("Enter a number : \n"))
    print("THE ANSWER IS ",num1%num2)
   


