import pandas as pd
import matplotlib.pyplot as plt
#load data
df = pd.read_csv("sales.csv")
#fix column spacing issues
df.columns = df.columns.str.strip()
#display original data
print("Original Data:\n")
print(df)
#add revenue column
df['Revenue'] = df['Quantity'] * df['Price']
#total revenue
total_revenue = df['Revenue'].sum()
print("\nTotal Revenue:",total_revenue)
#best selling product
top_product = df.groupby('Product')['Quantity'].sum().idxmax()
print("Best Selling Product:",top_product)
#revenue by product
product_sales = df.groupby('Product')['Revenue'].sum()
#plot graph
product_sales.plot(kind='bar')
#add values on top of bars
for i, value in enumerate(product_sales):
    plt.text(i, value, str(value), ha='center')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()
#save result to new file
df.to_csv("sales_result.csv", index=False)
#final clean output
print("\nFinal Data:\n")
print(df.to_string(index=False))
