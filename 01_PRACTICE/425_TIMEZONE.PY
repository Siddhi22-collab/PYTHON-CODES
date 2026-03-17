from datetime import datetime,timezone
c1=datetime.now()
print(c1)
c1.strftime('%Y-%m-%d %H:%M:%S.%f %z')