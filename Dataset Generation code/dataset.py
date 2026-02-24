import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


#Create Stores

states = ["VIC", "NSW", "QLD", "WA"]
regions = ["Metro", "Regional"]

stores = []

for i in range(1, 21):
    region = random.choice(regions)
    stores.append({
        "Store_ID": f"S{i:03}",
        "Store_Name": f"Coles Store {i}",
        "State": random.choice(states),
        "Region": region,
        "Store_Size_sqft": random.randint(25000, 55000),
        "Volume_Multiplier": 1.3 if region == "Metro" else 0.9
    })

df_stores = pd.DataFrame(stores)
df_stores.to_csv("stores.csv", index=False)

#Create Products
category_config = {
    "Dairy": (20, (0.20, 0.28), 7),
    "Meat": (20, (0.25, 0.35), 5),
    "Produce": (25, (0.30, 0.40), 4),
    "Bakery": (15, (0.40, 0.50), 2),
    "Pantry": (25, (0.25, 0.35), 180),
    "Beverages": (15, (0.30, 0.45), 365)
}

products = []
pid = 1

for category, (count, margin_range, shelf_life) in category_config.items():
    for _ in range(count):
        cost = round(np.random.uniform(1.5, 12.0), 2)
        products.append({
            "Product_ID": f"P{pid:03}",
            "Category": category,
            "Cost_Price": cost,
            "Margin_Min": margin_range[0],
            "Margin_Max": margin_range[1],
            "Shelf_Life_Days": shelf_life
        })
        pid += 1

df_products = pd.DataFrame(products)
df_products.to_csv("products.csv", index=False)

#Create Calendar

start_date = datetime(2024,1,1)
dates = [start_date + timedelta(days=i) for i in range(365)]

calendar = pd.DataFrame({
    "Date": dates,
    "Year": [d.year for d in dates],
    "Month": [d.month for d in dates],
    "Month_Name": [d.strftime("%B") for d in dates],
    "Quarter": [f"Q{((d.month-1)//3)+1}" for d in dates]
})

calendar.to_csv("calendar.csv", index=False)

#Generate Sales (50,000 Rows with Seasonality)

sales = []

for _ in range(50000):
    store = df_stores.sample(1).iloc[0]
    product = df_products.sample(1).iloc[0]
    date = random.choice(dates)

    base_units = random.randint(5, 100)

    # Metro multiplier
    base_units *= store["Volume_Multiplier"]

    # December spike
    if date.month == 12:
        base_units *= 1.35

    units = int(base_units)

    # Margin logic
    margin = np.random.uniform(product["Margin_Min"], product["Margin_Max"])
    selling_price = round(product["Cost_Price"] * (1 + margin), 2)

    # Promotion
    discount = 0
    if random.random() < 0.15:
        discount = round(np.random.uniform(0.05, 0.25),2)

    revenue = units * selling_price * (1 - discount)

    sales.append({
        "Date": date,
        "Store_ID": store["Store_ID"],
        "Product_ID": product["Product_ID"],
        "Units_Sold": units,
        "Selling_Price": selling_price,
        "Discount_%": discount,
        "Revenue": round(revenue,2)
    })

df_sales = pd.DataFrame(sales)
df_sales.to_csv("sales.csv", index=False)


#Generate Inventory with Shelf-Life Logic

inventory = []

for _ in range(20000):
    store = df_stores.sample(1).iloc[0]
    product = df_products.sample(1).iloc[0]
    date = random.choice(dates)

    opening = random.randint(100, 600)

    # Higher wastage for short shelf life
    if product["Shelf_Life_Days"] <= 7:
        wastage = random.randint(0, 25)
    else:
        wastage = random.randint(0, 5)

    closing = max(opening - random.randint(20,120) - wastage, 0)

    inventory.append({
        "Date": date,
        "Store_ID": store["Store_ID"],
        "Product_ID": product["Product_ID"],
        "Opening_Stock": opening,
        "Closing_Stock": closing,
        "Wastage_Units": wastage,
        "Reorder_Level": random.randint(80,200)
    })

df_inventory = pd.DataFrame(inventory)
df_inventory.to_csv("inventory.csv", index=False)