#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


pd=pd.read_csv("customer_shopping_data.csv")
print(pd)


# In[4]:


print(pd.head(5))


# In[10]:


print(pd.info())


# In[13]:


#Check column names
print(pd.columns)


# In[15]:


#Check dataset shape (rows, columns)
print("Dataset Shape: ", pd.shape)


# In[19]:


#Check data types
print(pd.dtypes)


# In[21]:


#Find missing values
print(pd.isnull())


# In[30]:


#Remove duplicate rows
pd.drop_duplicates(inplace=True)
print(pd)


# In[36]:


#Convert a column (Price/Sales) to NumPy array
Price_array=pd['price'].to_numpy()
print(Price_array)


# In[41]:


#Find mean, median, standard deviation
mean_price=pd['price'].mean()
median_price=pd['price'].median()
standard_deviation_price=pd['price'].std()
print("Mean Price: ", mean_price)
print("Median Price: ", median_price)
print("Standard deviation Price: ", standard_deviation_price)


# In[46]:


#Find max and min values
max_price=pd['price'].max()
print("max price :",max_price)
min_price=pd['price'].min()
print("min price :",min_price)


# In[50]:


#Normalize a numeric column
pd['Normalized_Price'] = (pd['price'] - pd['price'].min()) / (pd['price'].max() - pd['price'].min())
print(pd) 


# In[53]:


#Apply mathematical operations (e.g., discount calculation)
pd['Discounted_Price'] = pd['price'] * 10
print(pd)  


# In[54]:


#Create new column (Total Sales = Price × Quantity)
pd['Total_sales'] = pd['price'] - pd['quantity']
print(pd) 


# In[55]:


#Find total revenue
pd['Total_revenue'] = pd['price'] * pd['quantity']
print(pd) 


# In[59]:


#Find average order value
avg_order_value=pd['quantity'].mean()
print("avg_order_value:",avg_order_value)


# In[63]:


#Find top-selling product
top_selling_product = pd.groupby('category')['Total_sales'].sum().idxmax()
print("Top Selling Product: ", top_selling_product)


# In[69]:


#Find customer who spent the most
top_customer=pd.groupby('customer_id')['Total_sales'].sum().idxmax()
print("top customer:",top_customer)


# In[74]:


revenue_by_category = pd.groupby('category')['Total_sales'].sum()
print("Total Revenue by Category: ",revenue_by_category)   


# In[78]:


#Sort data by sales descending
sorted_data = pd.sort_values(by='Total_sales', ascending=False)     
print("Data sorted by Total Sales:",sorted_data)


# In[80]:


#absFilter orders with high sales (> certain value)
very_high_value_orders = pd[pd['Total_sales'] > 5000]
print("Very High Value Orders: ",very_high_value_orders)


# In[94]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_shopping_data.csv")

# Create Total Sales column
df['Total_sales'] = df['price'] * df['quantity']

# Group by Region
region_sales = df.groupby('shopping_mall')['Total_sales'].sum()

# Bar Chart
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Shopping_mall")
plt.ylabel("Total_sales")
plt.legend()
plt.grid()
plt.show()


# In[96]:


category_count = df['category'].value_counts()

category_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Distribution")
plt.ylabel("")
plt.show()


# In[99]:


# Convert date
df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')

# Remove invalid dates
df = df.dropna(subset=['invoice_date'])

# Group by date
sales_trend = df.groupby('invoice_date')['Total_sales'].sum()

# Line chart
sales_trend.plot(kind='line', marker='o')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()


# In[ ]:




