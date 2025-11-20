from datetime import datetime

s = input("Enter -- > ").strip()

dt = datetime.fromisoformat(s)

day   = dt.day
month = dt.month
year  = dt.year
hour  = dt.hour
minute = dt.minute
second = dt.second

tz = dt.strftime("%z")
tz = int(tz) // 100      #

print(f"{day:02d}-{month:02d}-{year} {hour}:{minute:02d}:{second:02d} {tz:+d}")
