import datetime

# Get current UTC time
utc_now = datetime.datetime.utcnow()

# Convert to India Standard Time (IST)
india_now = utc_now.astimezone(datetime.timezone(datetime.timedelta(hours=5.5)))

# Print the time
print(f"Current time in India (IST): {india_now}")
