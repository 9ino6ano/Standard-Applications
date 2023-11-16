import psutil

def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d"% (hours ,minutes,seconds)

battery=psutil.sensors_battery()
percent=battery.percent
time=convertTime(battery.secsleft)

print("Battery percentage :",percent)
print("Power plugged in:",battery.power_plugged)

#convert time to hours and min
print("Battery left:",time)


"""
[track any phone number using = https://track.bzfrs.co/SHFxj]
Learn how to create a project in python that can check battery percentage of system ,not only percentage we will also find the time remaining and plug in status.
"""
