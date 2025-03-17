import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "tesla_stock_data.csv"  # Ensure the dataset is in the same folder as this script
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set the style for seaborn
sns.set(style="whitegrid")

# Create a figure and axis
plt.figure(figsize=(12, 6))

# Plot Closing Price over Time
sns.lineplot(x=df['Date'], y=df['Close'], label="Closing Price", color='blue')

# Formatting the plot
plt.title("Tesla Stock Closing Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
