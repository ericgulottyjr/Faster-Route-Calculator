from driver import download_csv
from csv_parser import parse_csv

# Ask the user for the date in YYYY-MM-DD format
date_input = input("Enter a date in the format YYYY-MM-DD: ")

path = download_csv(date_input)

df, faster_route = parse_csv(str(path))

# Calculate MBTA faster percentage
mbta_faster_percentage = len(faster_route) / len(df)
print(f"Percentage of Faster MBTA Route Notifications for {date_input}: {mbta_faster_percentage}")