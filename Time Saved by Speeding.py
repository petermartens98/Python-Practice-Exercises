# Time Saved by Speeding
# Create a function that calculates the amount of time saved were you traveling with an average speed
# that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.
# Examples:
#   The parameter's format is as follows:
#       (speed limit, avg speed, distance traveled at avg speed)
#   time_saved(80, 90, 40) ➞ 3.3
#   time_saved(80, 90, 4000) ➞ 333.3
#   time_saved(80, 100, 40 ) ➞ 6.0
# Notes:
#   Speed = distance/time
#   The time returned should be in minutes, not hours.
#   Round the answer to one decimal place.
#   The speed limit and average speed are both given in mi/hr]
# Difficulty: Medium
# Date: 8/7/2021

def time_saved(limit,avg_spd,dist):
    time = (dist/limit)-(dist/avg_spd)
    time = time*60
    roundedtime = round(time,1)
    print(str(roundedtime))

time_saved(80,90,40)
time_saved(80,90,4000)
time_saved(80,100,40)


