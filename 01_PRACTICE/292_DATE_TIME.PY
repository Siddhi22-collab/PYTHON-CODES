from datetime import date, datetime
# Get today's Date
today=date.today()
print("Today's Date:",today)

#Get the current Date and Time
now=datetime.now()
print("Current Date and Time:",now)

#Optional: Print Time only
print("Current Time:",now.time())
