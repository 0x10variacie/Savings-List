import time
from datetime import datetime
import calendar

# Preliminary list of variables and lists
day = range(1,31)
month = range(1,12)
year = 0

isav = 0
savvalue = 0
dsval = 0

vc_input = 0
vc_period = 0

sdate = []
sval = []
svald = []
cur = "USD"
slist = []

# Functions
def content_check():
    if slist:
        if len(slist[0]) == 3:
            sdate,sval,svald = slist[0]
            print(sdate,sval,svald)
    else:
        print("No records so far\n")

def newdmy():
    while True:
        iday = int(input("Enter a day: "))
        if 1 <= iday <= 31:
            day = int(iday)
        else:
            print("Please enter the day between 1 and 31!")
        imon = int(input("Enter a month: "))
        if 1 <= imon <= 12:
            month = int(imon)
        else:
            print("Please enter the month between 1 and 12!")
        iyear = int(input("Enter a year: "))
        if 1 <= int(iyear) <= 10000:
            year = int(iyear)
        else:
            print("Please enter the valid year!")
        if day != "" and month != "" and year != "":
            sdate = f"{day}.{month}.{year}"
            print(f"Date saved: {sdate}\n")
            break
    return sdate

def newval():
    while True:
        isav = float(input("Enter your saved amount: "))
        if isav != "" and isav is not None:
            savvalue = float(isav)
            print(f"Saved amount recorded: {savvalue:.2f}\n")
            sval = (f"{savvalue:.2f}")
            break
        else:
            print("Please enter your saved amount!")
    return sval

def ds():
    while True:
        def ds_output():
            print(f"Daily spendings: {dsval:.2f} {cur}\n")
        dsdate = datetime.now()
        dsyear,dsmonth = dsdate.year,dsdate.month
        dsval_input = float(input("Enter your value: "))
        if dsval_input != "" and dsval_input is not None:
            dsval_choice = input("Do you want to calculate per Whole month or per Remaining days? (W/R) ").upper()
            if dsval_choice == "":
                print("Please make a choice!")
            elif dsval_choice == str('W'):
                dsval = float(dsval_input) / 30
                ds_output()
            elif dsval_choice == str('R'):
                    dsdate = datetime.now()
                    dsyear, dsmonth, dsday = dsdate.year, dsdate.month, dsdate.day
                    dsremain = int(calendar.monthrange(dsyear, dsmonth)[1] - dsdate.day)
                    if dsremain > 0:
                        dsval = float(dsval_input) / dsremain
                        ds_output()
            break
        else:
            print("Please enter your value!")

def vc():
    while True:
        def vc_output():
            print(f"You should have at least {vc_value:.2f} {cur}\n")
        vc_input = float(input("Enter your daily spendings value: "))
        if vc_input != "" and vc_input is not None:
            vc_choice = input("Do you want to calculate for Whole month or for specific Remaining days? (W/R) ").upper()
            if vc_choice == "":
                print("Please make a choice!")
            elif vc_choice == str('W'):
                vc_value = float(vc_input) * 30
                vc_output()
            elif vc_choice == str('R'):
                vc_period = 0
                vc_period = input("How many days remain in the current month? ")
                if vc_period == "":
                    vc_period = int(vc_period)
                vc_value = float(vc_input) * float(vc_period)
                vc_output()
            break
        else:
            print("Please enter your value!")

#def vldfcl():
    #while True:


def setcur(cur):
    print (f"The current currency is {cur}.")        
    while True:
        newcur = input("Please enter the new currency: ").upper()
        if len(newcur) == 3:
            cur = str(newcur.upper())
            print("New currency set")
            break
        elif len(newcur) != 3:
            print("Error: the new currency should contain 3 letters in accordance with ISO 4217!")                
    return cur    

# Startup
print("Savings List v1.0 DEVTEST")
time.sleep(1.5)
print("by M. Veselov")
time.sleep(1)
print("")
print("for help, type 'help'")
print("for quit, type 'quit'\n")
time.sleep(0.5)

content_check()

# Core goes here
while True:
    prompt = input("> ")

    if prompt == str("ds"):
        ds()

    if prompt == str("vc"):
        vc()


    if prompt == str("hist"):
        if slist:
            for x in slist:
                print(x)
        else:
            print("No records so far\n")

    if prompt == str("add"):
        sdate = newdmy()
        sval = newval()
        slist.append(sdate+": "+sval+" "+cur)

    if prompt == str("del"):
        if slist:
            for i,x in enumerate(slist):
                delask = input(f"You're about to delete the recent record: {x}\nDo you wish to permanently delete it? (y/n) ")
                if delask == 'n':
                    break
                elif delask == 'y':
                    slist.pop(i)
                    print("Record deleted\n")
        else:
            print("No records so far\n")
                

    if prompt == str("cur"):
        cur = setcur(cur)
    
    if prompt == str("about"):
        print("Savings List v1.0 DEVTEST")
        print("by M. Veselov")
        print("\nAllows to record savings by adding or deleting entries to the built-in list.")
        print("\nThe script is being developed as a motivation for my thirst of getting job\nwritten in Python")
        
    if prompt == str("help"):
        print("HELP PAGE\n")
        print("about - displays the About page")
        print("help - displays this page")
        print("quit - terminates this program")
        print("\nMAIN COMMANDS")
        print("ds - calculation of daily spendings")
        print("vc - calculation of value through period and daily spendings")
        print("hist - displays all the records")
        print("add - add a new record")
        print("del - delete the recent record")
        print("\nSETTINGS")
        print("cur - sets new currency")
    if prompt == str("quit"):
        break
    

