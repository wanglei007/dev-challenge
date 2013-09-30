# Exercises for chapter 2:

# Name: Lei Wang

# EX2.1: 0 indicates octal numeral value
# 02132 = 2 + 3 * 8 + 1 * (8**2) + 2 * (8**3) = 1114
# 02492: octal numeral system uses only digits 0 to 7,  so 9 is invalid token

# EX2.2: before modifying the code, it would produce no output
# here's the modified script
print 5
x = 5
print x+1

# EX2.3
# width/2 = 8 int
# width/2.0 = 8.5 float
# height/3 = 4.0 float
# 1 + 2 * 5 = 11 int
# delimiter * 5 = '.....' str

# EX2.4 - 1
import math
r = 5
volume = 4.0/3 * math.pi * r**3
print volume

# EX2.4 - 2
cost = 24.95 * (1-.4) * 60 + 3 + .75 * (60-1)
print cost

# EX2.4 - 3
running = (8*60+15)*2 + (7*60+12)*3
second = running - (running/60) * 60
minute = 52 + (running/60)
hour = 6 + minute/60
minute = minute - minute/60 * 60
print str(hour)+':' + str(minute) + ':' + str(second)
