import time
for i in range(1,6):
        a=time.asctime()
        print(a)
        time.sleep(5)
        print ("\n\n")
        for j in range(1,11):
            print (i, "X" , j , "=" , i*j)

    
