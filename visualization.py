import pandas as pd

sales_data = pd.read_csv('../data/processed/cleaned_sales_data.csv')

sales_data['Date'] = pd.to_datetime(sales_data['Date'])

monthly_sales = sales_data.groupby(
    sales_data['Date'].dt.to_period('M')
)['Total_Sales'].sum()

quarterly_sales = sales_data.groupby(
    sales_data['Date'].dt.to_period('Q')
)['Total_Sales'].sum()

category_sales = sales_data.groupby(
    'Product_Category'
)['Total_Sales'].sum().sort_values(ascending=False)

print(monthly_sales)
print(quarterly_sales)
print(category_sales)
