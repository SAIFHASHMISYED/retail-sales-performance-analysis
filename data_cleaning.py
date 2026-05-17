import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(365)]

quantity = np.random.randint(1, 100, size=365)
unit_price = np.random.uniform(50, 500, size=365).round(2)

categories = ['Electronics', 'Clothing', 'Home Goods', 'Books']
product_category = np.random.choice(categories, size=365)

sales_data = pd.DataFrame({
    'Date': dates,
    'Quantity': quantity,
    'Unit_Price': unit_price,
    'Product_Category': product_category
})

sales_data.to_csv('../data/raw/retail_sales_data.csv', index=False)

print('Dataset generated successfully')
