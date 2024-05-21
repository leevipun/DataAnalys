import pandas as pd

# Read the data into a pandas DataFrame
df = pd.read_csv('vsk21aFysiikka.csv')

# Replace non-numeric values with NaN
df = df.apply(pd.to_numeric, errors='coerce')

# Calculate the average for each course column, skipping NaN values
averages = df.mean()

# Create a new row with the averages
average_row = pd.DataFrame(averages).transpose()

average_from_average = average_row.mean()

# Set the group column value for the average row
average_from_average['group'] = 'average'

# Append the average row to the original DataFrame
df = pd.concat([df, average_from_average], ignore_index=True)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_data.csv', index=False)

print("Averages appended and CSV file updated.")
