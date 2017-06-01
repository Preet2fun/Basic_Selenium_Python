#Whileloop does the exactly same thing what "if statement" does, 
#but instead of running the code block once, they jump back to the point where it began the code and repeats the whole process again.

def main():
    x=0
    #Case 1
    while (x<5):
        print x
        x+=1
    
    #Case 2    
    for x in range(2,10):
        print x
    
    #Case 3    
    abc = ['cricket','football','rugby','kabbadi']
    for a in abc:
        print a    
    
    #Case 4    
    for a in range(100,120):
        if (a==110): break
        print a
        
    #Case 5
    for b in range(10,100):
        if (b%10==0): continue
        print b
        
        
    #Case 6
    xyz = ['a','b','c','d','e']
    for c ,m in enumerate (xyz):
        print c,m       

if __name__=="__main__":
    main()