#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Step 1 — Create Dataset
import pandas as pd

data = {
    "order_id": range(1, 31),
    "product_category": [
        "Electronics","Fashion","Home Appliances","Fashion","Electronics",
        "Electronics","Fashion","Home Appliances","Electronics","Home Appliances",
        "Fashion","Electronics","Home Appliances","Fashion","Electronics",
        "Home Appliances","Fashion","Electronics","Fashion","Home Appliances",
        "Electronics","Fashion","Home Appliances","Electronics","Fashion",
        "Electronics","Home Appliances","Fashion","Electronics","Home Appliances"
    ],
    "quantity": [1,2,1,3,1,2,1,2,1,1,3,1,2,1,2,1,2,1,3,1,2,1,1,3,1,2,1,2,1,1],
    "price": [1200,800,3000,700,1500,1800,1200,2500,2000,2800,
              900,2200,2500,850,1900,2600,750,2100,1000,2700,
              1600,950,2400,1400,1000,2300,2600,900,1750,2900],
    "purchase_date": [
        "2025-11-01","2025-11-01","2025-11-02","2025-11-02","2025-11-03",
        "2025-11-03","2025-11-04","2025-11-04","2025-11-05","2025-11-05",
        "2025-11-06","2025-11-06","2025-11-07","2025-11-07","2025-11-08",
        "2025-11-08","2025-11-09","2025-11-09","2025-11-10","2025-11-10",
        "2025-11-11","2025-11-11","2025-11-12","2025-11-12","2025-11-13",
        "2025-11-13","2025-11-14","2025-11-14","2025-11-15","2025-11-15"
    ],
    "customer_feedback": [
        "Great quality and fast delivery","Size was too small","Works well but noisy",
        "Color was different than expected","Very happy with the phone",
        "Good performance but battery drains fast","Loved the design",
        "Late delivery and expensive","Amazing display and speed","Helpful product",
        "Perfect fitting and good price","Delivery was late","Very useful in kitchen",
        "Material was not good","High performance laptop","Packaging was damaged",
        "Stylish look and affordable","Recommended by friend and good experience",
        "Comfortable but little pricey","Not worth the price",
        "Value for money!","Product quality average","Super easy to use",
        "Received wrong item","Very comfortable","Camera is not good",
        "Energy efficient and helpful","Color faded after wash",
        "Very smooth performance","Product stopped working after 2 days"
    ]
}

df = pd.DataFrame(data)
df.head()


# In[6]:


# Step 2 — Store the data into SQL & Run Queries
import sqlite3

# Create a connection
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Store dataframe into SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data inserted into SQL successfully!")


# In[7]:


# 2.2 — Run SQL Queries- Query 1️⃣ — Total Revenue
query1 = """
SELECT SUM(quantity * price) AS total_revenue
FROM sales;
"""
pd.read_sql_query(query1, conn)


# In[8]:


#Query 2️⃣ — Revenue by Category
query2 = """
SELECT product_category,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product_category
ORDER BY revenue DESC;
"""
pd.read_sql_query(query2, conn)


# In[9]:


#Query 3️⃣ — Total Orders by Category
query3 = """
SELECT product_category,
       COUNT(order_id) AS total_orders
FROM sales
GROUP BY product_category;
"""
pd.read_sql_query(query3, conn)


# In[10]:


# Query 4️⃣ — Average Price by Category
query4 = """
SELECT product_category,
       AVG(price) AS avg_price
FROM sales
GROUP BY product_category;
"""
pd.read_sql_query(query4, conn)


# In[11]:


# Step 3 — Python Data Visualization
#Visualization 1 — Revenue by Category
import matplotlib.pyplot as plt
import seaborn as sns

revenue_data = pd.read_sql_query("""
SELECT product_category,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product_category;
""", conn)

plt.figure(figsize=(6,4))
sns.barplot(data=revenue_data, x="product_category", y="revenue")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()


# In[12]:


#Visualization 2 — Number of Orders by Category
orders_data = pd.read_sql_query("""
SELECT product_category,
       COUNT(order_id) AS orders
FROM sales
GROUP BY product_category;
""", conn)

plt.figure(figsize=(6,4))
sns.barplot(data=orders_data, x="product_category", y="orders")
plt.title("Orders by Category")
plt.xlabel("Category")
plt.ylabel("Total Orders")
plt.show()


# In[15]:


# Step 4 — AI Insights (Alternative Free LLM)
get_ipython().system('pip install transformers torch')


# In[16]:


# 4.1 — Sentiment Analysis of Customer Feedback
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

df["sentiment"] = df["customer_feedback"].apply(lambda x: sentiment_model(x)[0]["label"])
df.head()


# In[17]:


#4.2 — Calculate Sentiment Summary
sent_summary = df["sentiment"].value_counts()
sent_summary


# In[18]:


#4.3 — Visualize Sentiment
sent_summary.plot(kind="bar", title="Customer Sentiment Distribution")
plt.show()


# In[19]:


#4.4 — AI-Generated Insights Using Sentiment + Revenue Data
total_rev = revenue_data["revenue"].sum()
best_cat = revenue_data.loc[revenue_data["revenue"].idxmax(), "product_category"]
worst_sent_cat = df[df["sentiment"]=="NEGATIVE"]["product_category"].mode()[0]

auto_insights = f"""
 AI Insights Report

• Total Revenue: {total_rev}
• Best Revenue Category: {best_cat}
• Most Customer Complaints: {worst_sent_cat}

Recommendation:
Focus on improving product quality and delivery service in {worst_sent_cat} category.
Electronics continues to drive major revenue.

Summary:
AI suggests focusing on customer satisfaction to boost repeat sales.
"""
print(auto_insights)


# In[20]:


# Step 5 — AI Natural Language Query System
# 5.1 Define a Function for NLQ (Natural Language Query)
def ai_query(question):
    
    # Identify intent using simple logic + keywords
    question_lower = question.lower()

    if "revenue" in question_lower:
        sql = """
        SELECT product_category, SUM(quantity * price) AS revenue
        FROM sales
        GROUP BY product_category
        ORDER BY revenue DESC;
        """
        result = pd.read_sql_query(sql, conn)
        
        top_cat = result.iloc[0]["product_category"]
        top_rev = result.iloc[0]["revenue"]
        
        return f"""
🤖 AI Analyst Response:

📌 Business Insight:
The **{top_cat}** category generates the highest revenue of **₹{top_rev}**.

💡 Strategy Suggestion:
Increase marketing focus and add more premium products in this category
to maximize revenue opportunities.

✨ Summary:
{top_cat} = high demand + strong revenue.
        """
    
    elif "orders" in question_lower or "sales" in question_lower:
        sql = """
        SELECT product_category, COUNT(order_id) AS order_count
        FROM sales
        GROUP BY product_category
        ORDER BY order_count DESC;
        """
        result = pd.read_sql_query(sql, conn)
        
        top_cat = result.iloc[0]["product_category"]
        top_orders = result.iloc[0]["order_count"]
        
        return f"""
🤖 AI Analyst Response:

📌 Insight:
**{top_cat}** category has the highest number of orders: **{top_orders}**.

🛍️ Customer Pattern:
High purchase count means strong customer interest and accessibility.

✨ Strategy:
Focus retention and loyalty programs for **{top_cat}** buyers.
        """
    
    else:
        return "I can currently answer questions about revenue and orders only."


# In[21]:


# 5.2 Ask Questions to Your AI
print(ai_query("Which category earns the most revenue?"))


# In[22]:


print(ai_query("Which category has most orders?"))


# In[ ]:




