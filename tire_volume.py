import math
import datetime

width_tire = int(input("What's the tire's width? "))
aspect_ratio = int(input("What's the tire's aspect ratio? "))
wheel_diameter = int(input("What's the wheel's diameter in inches? "))

volume = (math.pi * width_tire**2 * aspect_ratio)*(width_tire*aspect_ratio+(2540 *wheel_diameter))/10000000000



todays_date = datetime.datetime.now()
year = todays_date.strftime("%Y")
month = todays_date.strftime("%m")
day = todays_date.strftime("%d")


with open("volumes.txt",'a') as volumes:
     print(f"{month}/ {day}/ {year}, {width_tire}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}", file=volumes)


with open("volumes.txt") as v:
     for line in v:
          print(line)     