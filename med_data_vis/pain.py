import pandas as pd

# Sample data (make sure height is in METERS)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Weight_kg': [68, 85, 74],   # Weight in kilograms
    'Height_cm': [165, 180, 175]  # Height in centimeters (potential issue!)
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Height to meters if it's in cm
df['Height_m'] = df['Height_cm'] / 100  

# Calculate BMI
df['BMI'] = df['Weight_kg'] / (df['Height_m'] ** 2)

print(df[['Name', 'Weight_kg', 'Height_m', 'BMI']])
