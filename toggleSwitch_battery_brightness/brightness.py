import screen_brightness_control as pct

#get current brightness value
print(pct.get_brightness())

level=input("Enter brightness level: ")
pct.set_brightness(level)

#brightness value after change
print(pct.get_brightness())