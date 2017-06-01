import time
class Man_United:
    def Result(Score,MANU,OTHER_TEAM):
        Score.MANU=MANU
        Score.OTHER_TEAM=OTHER_TEAM
        if (MANU > OTHER_TEAM):
            print("MANCHASTER UNITED")
        elif(MANU < OTHER_TEAM):
            print("OTHER TEAM")
        else:
            print("MATCH DRAW")
            

print("Pppppeeeeeeeeee......Lets Play")
time.sleep(5)


a=input("please enter the final score of Manu : ")
b=input ("please enter the final score of Other team : ")

print ("And the winer is .....")
time.sleep(3)

match=Man_United()
match.Result(a,b)

c=match.MANU
d=match.OTHER_TEAM

time.sleep(2)
print("So final score is MANU {} and Other team {}".format(c,d))
print("Good Bye....")
