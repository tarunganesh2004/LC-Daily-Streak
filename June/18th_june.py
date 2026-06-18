# Angle between hands of a clock LC 1344

hour=12
minutes=30

"""
clock has 360degrees,12hrs
each hour covers = 360/12=30 degrees

Minute hand movement
Minute hand completes one full circle in 60 minutes.
360/60= 6degrees
5min=> 30 degrees
10min => 60 degrees

minute_angle=minutes*6

Hour Hand Movement
every minute, the hour hand moves 0.5 degrees 
(since one hour takes 60minutes, every hour mark is 30 degrees, 
so 30 degrees in 60minutes => per minute 30/60=0.5
)
Example:
3.10 ==> each hour 30, 3*30+ for minutes 10*30/60=95
3.30 ==> 3*30+30*30/60=105
5.20 ==> 5*30+20*0.5=160degrees

hour_angle=hour*30+minutes*0.5

here they asked min of diff, hour-minute angle, 360-diff
"""

def angleClock(hour,minutes):
    minute_angle=minutes*6

    hour_angle=(hour%12)*30+minutes*0.5

    diff=abs(hour_angle-minute_angle)
    return min(diff,360-diff)

print(angleClock(hour,minutes))