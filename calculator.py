
import math
from datetime import datetime, date, time, timedelta
print(math.sqrt(16))          # 4.0 - square root
print(math.pow(2, 3))         # 8.0 - 2^3
print(math.factorial(5))      # 120
print(math.gcd(12, 18))       # 6 - greatest common divisor
print(math.pi)                # 3.141592653589793
print(math.e)                 # 2.718281828459045
print(math.sin(math.radians(90)))  # 1.0

#  Date time 
print("\n\n Date time\n") 
now = datetime.now()
print(now)                # Current date and time
print(now.date())         # Date only
print(now.time())         # Time only
d = date(2025, 12, 25)
t = time(10, 30)
print(d, t)               # 2025-12-25 10:30:00
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print(tomorrow, yesterday)
