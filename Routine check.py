
import os
import datetime
from text_to_speech import speak
os. system('clear')
alarmH = int(input("What hour do you want the alarm to ring? "))
alarmM = int(input("What minute do you want the alarm to ring? "))
amPm = str(input("am or pm? "))
messageUser = str(input("Your message: "))
os. system('clear')
print("Waiting for alarm",alarmH,alarmM,amPm)
if (amPm == "pm"):
        alarmH = alarmH + 12
while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute) :
        print("Time to wake up")
        speak(messageUser, "en", save=True, file="schedule.mp3")
        break