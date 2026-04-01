import pandas as pd

# Load data
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine
df = pd.concat([df1, df2, df3], ignore_index=True)

# ------------------ PROCESS ------------------

# Keep only Pink Morsel
df = df[df['product'] == 'pink morsel']

# Convert price to float
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

# Create sales column
df['sales'] = df['price'] * df['quantity']

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Keep only required columns
df = df[['sales', 'date', 'region']]

# ------------------ OUTPUT ------------------

# Save to new CSV
df.to_csv("output.csv", index=False)

print("File created: output.csv")