import datetime

# Get current time in UTC
utc_now = datetime.datetime.utcnow()

# Convert to a specific timezone (replace with the actual timezone)
local_now = utc_now.astimezone(datetime.timezone(datetime.timedelta(hours=-5)))

print(f"UTC time: {utc_now}")
print(f"Local time: {local_now}")
