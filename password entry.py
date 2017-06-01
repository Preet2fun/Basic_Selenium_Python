user=input("please enter user name : ")
pwd=input("please enter password : ")
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
j=2
for i in range(3):
    a=input("please enter username to login : ")
    b=input("please enter password to login : ")
    if ((a==user) & (b==pwd)):
          print("Welcome to Love World")
          break
    else:
        print("only",j-i,"chance left")
        continue
    
