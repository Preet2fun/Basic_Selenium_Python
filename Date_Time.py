from datetime import date
from datetime import time
from datetime import datetime


def main():
    
    #some basic concept of how to use datetime and date object in Python
    
    today = date.today()
    print "Today's Date is :", today
    print "Today's Day is :", today.day
    print "Today's month is :", today.month
    print "Today's year is :", today.year
    print "Today's Weekday Day is :", today.weekday()
    
    Date_time = datetime.now().time()
    print "Today's Date & current time is :", Date_time
    
    #Suppose we want to print just the current time without the date.
    t = datetime.time(datetime.now())
    print "Current time :" ,t
    
     #weekday returns 0 (monday) through 6 (sunday)
    wd = date.weekday(today)
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print "today is a " + days[wd]
    
    # Formatting function for date & time function
    # We used the "str f time function" for formatting.
    # This function uses different control code to give an output.
    # Each control code resembles different parameters like year,month, weekday and date 
    
    now = datetime.now()
    print "Year is : ", now.strftime("%Y")
    print "Year is : ", now.strftime("%y")
    print "Month is : ", now.strftime("%B")
    print "month is : ", now.strftime("%b")
    print "Weekday is : ", now.strftime("%A")
    print "Weekday is : ", now.strftime("%a")
    
    
    # With the help of "Strftime" function we can also retrieve local system time, date or both.
    #Times and dates can be formatted using a set of predefined string
    
     #get the current date and time
    now = datetime.now()
    
    # %c - local date and time, %x-local's date, %X- local's time
    print now.strftime("%c")
    print now.strftime("%x")
    print now.strftime("%X")
    
    ##### Time Formatting ####   
    #%I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
    
    print now.strftime("%I:%M:%S %p") # 12-Hour:Minute:Second:AM
    print now.strftime("%H:%M") # 24-Hour:Minute   
    
    
if __name__=="__main__":
    main()