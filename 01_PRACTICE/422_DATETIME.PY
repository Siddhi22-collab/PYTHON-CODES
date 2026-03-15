from datetime import time
t1=time(11,33,20,300)
print(t1)
print(t1.hour,t1.minute,t1.second,t1.microsecond)
print(t1.tzinfo,t1.tzname)
print(t1.strftime('%H:%H:%S:%F'))