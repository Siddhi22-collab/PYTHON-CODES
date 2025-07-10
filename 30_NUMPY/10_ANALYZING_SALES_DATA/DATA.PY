import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
num_records = 10
product_ids = np.arange(1001, 1001 + num_records)
products = np.array(['Laptop', 'Tablet', 'Mobile', 'Monitor', 'Keyboard'])

product_names = np.random.choice(products, num_records)


prices = np.random.randint(50, 50001, num_records)

# Random quantities sold
quantities = np.random.randint(1, 10, num_records)

# Total sales calculation
total_sales = prices * quantities

# Create DataFrame
df = pd.DataFrame({
    'ProductID': product_ids,
    'Product': product_names,
    'Price': prices,
    'Quantity': quantities,
    'TotalSales': total_sales
})

# Display the DataFrame
print("Sales Data:\n", df)

# Pandas operations
print("\nTotal Revenue:", df['TotalSales'].sum())
print("\nAverage Sales per Product:\n", df.groupby('Product')['TotalSales'].mean())

# Filter data: Products with total sales > 200000
high_sales = df[df['TotalSales'] > 200000]
print("\nHigh Sales Products:\n", high_sales)
