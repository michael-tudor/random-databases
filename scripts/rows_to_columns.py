import pandas as pd

# Load your CSV file
df = pd.read_csv('databases/us_fertility_1960_2021_old.csv', header=None)

# Transpose the DataFrame to make each year a separate row
df = df.transpose()

# Rename the columns
df.columns = ['year', 'us_birth_rate']

# Set the 'year' column as the first row, which contains the years
df['year'] = df['year'].astype(int) # Convert year from string to integer if necessary

# Save the transformed data back to a new CSV file
df.to_csv('databases/us_fertility_1960_2021.csv', index=False)
