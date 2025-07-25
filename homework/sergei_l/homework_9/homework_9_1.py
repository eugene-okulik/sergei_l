from datetime import datetime


date_str = "Jan 15, 2023 - 12:05:33"

parsed_date = datetime.strptime(date_str, '%b %d, %Y - %H:%M:%S')

print(f"Full month name is: {datetime.strftime(parsed_date, '%B')}")
print(f"New date format is: {datetime.strftime(parsed_date, '%d.%m.%Y, %H:%M')}")
