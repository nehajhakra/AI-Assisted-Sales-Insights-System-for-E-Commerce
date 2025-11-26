# AI-Assisted Sales Insights System for E-Commerce

This project shows how **traditional data analytics (SQL + Python)** can work together with **AI (NLP + simple LLM logic)** to generate business insights automatically.

Instead of only running queries and staring at tables, this system:
- calculates revenue and orders using **SQL**
- visualises patterns using **Python**
- analyses customer reviews using a **sentiment model**
- answers business questions in **natural language** like an AI Business Analyst :contentReference[oaicite:0]{index=0}  

---

## 🎯 Project Goal

**Objective:**  
Build a small end-to-end system that can:

1. Analyse e-commerce sales data (categories, price, quantity, dates)
2. Understand customer feedback using AI
3. Automatically generate human-readable business insights
4. Answer questions such as  
   > “Which category earns the most revenue?”  
   > “Which category has the most orders?”

This project demonstrates how **AI doesn’t replace data analysts** – it **helps them analyse faster and explain better**.

---

## 🧱 Tech Stack

- **Language:** Python
- **Database:** SQLite
- **Data Analysis:** pandas
- **Visualisation:** matplotlib, seaborn
- **NLP / AI:** HuggingFace `transformers` sentiment-analysis pipeline
- **Environment:** Jupyter Notebook / Python script

---

## 📂 Dataset

A tiny but realistic dataset of **30 e-commerce orders** is created inside the code (no external file needed).

Columns:

| Column            | Description                                        |
|-------------------|----------------------------------------------------|
| `order_id`        | Unique order ID                                    |
| `product_category`| `Electronics`, `Fashion`, `Home Appliances`        |
| `quantity`        | Units purchased                                    |
| `price`           | Selling price per order                            |
| `purchase_date`   | Date of purchase                                   |
| `customer_feedback` | Short review text from customer                 |

Why this dataset?

- Small → easy to understand
- Mixed **numeric + text features** → perfect to show both analytics and AI
- Looks like real e-commerce data → good for portfolio & interviews

---

## 🔁 Project Workflow

1. **Create dataset** in pandas  
2. **Store data in SQLite** (`sales` table)  
3. Run **SQL queries** for:
   - total revenue
   - revenue by category
   - total orders by category
   - average price by category  
4. Use **Python charts** to visualise revenue & orders  
5. Run **sentiment analysis** on `customer_feedback` using a HuggingFace model  
6. Combine revenue + sentiment → generate **AI Insights Report** in text  
7. Use a simple **NLQ (Natural Language Query) function**:
   - read your question (string)
   - decide which SQL query to run using keyword logic
   - run SQL
   - return an answer in business language

---

## 🧮 Key SQL Queries

```sql
-- Total Revenue
SELECT SUM(quantity * price) AS total_revenue
FROM sales;

-- Revenue by Category
SELECT product_category,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product_category
ORDER BY revenue DESC;

-- Orders by Category
SELECT product_category,
       COUNT(order_id) AS total_orders
FROM sales
GROUP BY product_category;

-- Average Price by Category
SELECT product_category,
       AVG(price) AS avg_price
FROM sales
GROUP BY product_category;
