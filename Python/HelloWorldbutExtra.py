# Hello World but make it ✨ extra ✨, add a little pizazz, sprinkle some tunes, be that weirdo
import datetime
import time
def getNumberSuffix(number):
    if number == 11:
        return "th"
    if number == 12:
        return "th"
    elif number == 13:
        return "th"
    if (number % 10) == 1:
        return "st"
    elif (number % 10) == 2:
        return "nd"
    elif (number % 10) == 3: 
        return "rd"
    else:
        return "th"
months = ["January", "Febrary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("Hello World :)")
name = input("What's your name? ")
age = int(input("And now, how old are you? "))
print("You're going to love (or hate, I suppose) this next bit...")
print("---------- . -------- ^ -------- ' --------- ` -------- ~ ---------")
counter = 1
print("Hello, " + name.capitalize() + ", welcome to the world!")
while counter <= age:
    print("Happy " + str(counter) + getNumberSuffix(counter) + " birthday!")
    time.sleep(1)
    counter += 1
print("Okay I promise it's over now :)")
time.sleep(0.5)
print("If u decided to troll, and now regret the massive loop you had to get through...")
time.sleep(1)
print("Well - it sucks to be you, I guess. \nAnd if you didn't get this far the first time, at least you learned your lesson :D")
print("If you did it (semi) decently, you a real G :)")
print("\nIf you've been in a coma for the past 10 years, a) you're a legend, b) you're probably about to have the shock of your life")
time.sleep(1)
print("The year is %s, the %s" % (datetime.datetime.now().year, datetime.datetime.now().day), end = '')
print(getNumberSuffix(datetime.datetime.now().day), end = '')
print(" of " + months[datetime.datetime.now().month - 1])
time.sleep(1)
print("There's a crappy pandemic, and we've all been waiting a really long time to have our parties and, truly, just totally")
print("\nC")
time.sleep(0.4)
print(" H")
time.sleep(0.4)
print("  I")
time.sleep(0.4)
print("   L")
time.sleep(0.4)
print("    L")
time.sleep(0.2)
print("\nIt's been a realllyyy long time and we're either exhausted, or psycho (or both) (: enjoy what u can of your new life, I guess. ")
print("Good luck, hope you don't catch the 'Rona")