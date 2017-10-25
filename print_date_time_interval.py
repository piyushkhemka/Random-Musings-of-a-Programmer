from datetime import date, datetime, timedelta

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

# Print dates at time interval of 4 days
# sample output
# 2011-10-10
# 2011-10-14
# .
# .
# .
# 2011-12-01
# 2011-12-05
# 2011-12-09
for result in perdelta(date(2011, 10, 10), date(2011, 12, 12), timedelta(days=4)):
    print result



# Print human readable timestamp at interval of 4 seconds
# sample output
# 2017-10-08 10:23:47
# 2017-10-08 10:23:57
# 2017-10-08 10:24:07
# 2017-10-08 10:24:17
# .
# .
# .
# 2017-10-08 17:43:57
# 2017-10-08 17:44:07
import datetime
start = datetime.datetime.strptime("08/10/2017 10:23:47", "%d/%m/%Y %H:%M:%S")
end = datetime.datetime.strptime("08/10/2017 17:44:12", "%d/%m/%Y %H:%M:%S")
step = datetime.timedelta(seconds=10)
while start <= end:
    print(str(start))
    start += step
