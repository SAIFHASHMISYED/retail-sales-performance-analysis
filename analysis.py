import pandas as pd

sales_data = pd.read_csv('../data/raw/retail_sales_data.csv')

sales_data.dropna(inplace=True)

sales_data['Date'] = pd.to_datetime(sales_data['Date'])

sales_data['Total_Sales'] = (
    sales_data['Quantity'] * sales_data['Unit_Price']
).round(2)

sales_data.drop_duplicates(inplace=True)

sales_data.to_csv('../data/processed/cleaned_sales_data.csv', index=False)

print('Data cleaned successfully')
