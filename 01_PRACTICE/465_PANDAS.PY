import pandas as pd

data = {
    "Region": ["East", "West", "East", "North"],
    "Sales": [1000, 2000, 1500, 3000],
    "Profit": [200, 500, 300, 800]
}

df = pd.DataFrame(data)

summary = df.groupby("Region").agg({
    "Sales": "sum",
    "Profit": "mean"
})

summary["Profit Margin"] = (
    summary["Profit"] / summary["Sales"]
) * 100

print(summary)