import time
class football:
    
    def __init__(self,country,club):

        print("I Love Football")
        print("Please selct country from 1-3 and club from 1-3")
        self.country=country
        a=self.country
        self.club=club
        b=self.club
        if ((a==1) & (b==1)):
            #a=England
            #b=Manchaster_united
            print ("Welcome to MANCHASTER UNITED the club of ENGLAND")
            #b=Liverpool
        elif ((a==1) & (b==2)):
            print ("Welcome to Liverpool the club of ENGLAND" )
        else:
            print ("Invalid Entry")

        time.sleep(3)


a=int(input("Please enter country code : "))
b=int(input("Please enter club code : "))

 

 


t1=football(a,b)

