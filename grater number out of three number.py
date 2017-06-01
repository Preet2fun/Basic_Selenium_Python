a=int(input("please enter first number : "))
b=int(input("please enter Second number : "))
c=int(input("please enter Third number : "))
if ((a>b) & (a>c)):
    print(a,"is grater then",b,"and",c)
elif ((b>a) & (b>c)):
    print(b,"is grater then",a,"and",c)
elif ((c>a) & (c>b)):
    print(c,"is grater then",a,"and",b)

input("Press Enter to Quit")
  
