import json
import pandas as pd
from datetime import datetime, timedelta

# Load the JSON data
with open('injective_events.json', 'r') as file:
    data = json.load(file)

# Initial time for Round #167
round_167_end = datetime(2024, 9, 18, 22, 0)  # 2024/09/18 22:00 UTC+09:00
round_167_end_utc = round_167_end - timedelta(hours=9)  # Convert to UTC

# Create an empty list to store the rows
rows = []

# Iterate over the rounds in reverse order (from most recent to oldest)
for round_number, round_data in enumerate(data.items(), start=0):
    round_name, values = round_data
    # Calculate the timestamp for each round by subtracting 7 days
    round_end_utc = round_167_end_utc - timedelta(weeks=round_number)

    # Organize the data
    inj_value = next(filter(lambda x: "INJ" in x, values))
    usd_value = next(filter(lambda x: "usd" in x, values))
    
    # Append the row (UTC timestamp, round, INJ, USD, Unix timestamp)
    rows.append([round_end_utc.strftime("%Y-%m-%d %H:%M:%S"), round_name, inj_value, usd_value])

# Convert to a DataFrame
df = pd.DataFrame(rows, columns=["UTC Timestamp", "Round", "INJ Amount", "USD Amount"])

# Export the DataFrame to a CSV file
csv_file_path = 'injective_auction_data.csv'
df.to_csv(csv_file_path, index=False)

print(f"Data has been saved to {csv_file_path}")

