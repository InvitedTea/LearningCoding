from datetime import datetime, date

print("=== How Many Days Have You Lived? ===\n")

# Get birthday from user
birth_str = input("Enter your birthday (DD/MM/YYYY): ")

try:
    # Convert string to datetime
    birthday = datetime.strptime(birth_str, "%d/%m/%Y")
    today = date.today()
    
    # Calculate days lived
    days_lived = (today - birthday.date()).days
    
    # Calculate hours, minutes, and seconds
    hours_lived = days_lived * 24
    minutes_lived = hours_lived * 60
    seconds_lived = minutes_lived * 60
    
    print(f"\nYou have lived for {days_lived:,} days!")
    print(f"That's about {hours_lived:,} hours!")
    print(f"Or {minutes_lived:,} minutes!")
    print(f"Or {seconds_lived:,} seconds!")

except ValueError:
    print("Oops! Please use the format DD/MM/YYYY (like 15/03/2014)")