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
These queries give the core business KPIs: revenue, demand and pricing per category.
📊 Visualisations

The notebook / script plots:

Revenue by Category – bar chart
<img width="558" height="391" alt="image" src="https://github.com/user-attachments/assets/a687a431-9cfb-4259-ab01-880912119a0b" />


Orders by Category – bar chart
<img width="532" height="391" alt="image" src="https://github.com/user-attachments/assets/5711cbe7-a330-420b-9d6d-167912c705b4" />


Customer Sentiment Distribution – bar chart (Positive vs Negative)
<img width="556" height="508" alt="image" src="https://github.com/user-attachments/assets/dbb93a60-617a-4d79-9a05-71dac1eca549" />

🤖 AI & NLP Component

The AI part uses the HuggingFace pipeline("sentiment-analysis") model:

Takes each customer_feedback

Returns a label: POSITIVE or NEGATIVE

Adds a sentiment column to the dataframe

Then we:

Count how many positive vs negative reviews we have

Identify which category has the most complaints

Generate an AI-style text summary like:

Total Revenue: 𝑥
Best Revenue Category: Electronics
Most Customer Complaints: Home Appliances
Recommendation: Improve quality & delivery in Home Appliances.

This shows how AI can write short business reports automatically.

💬 Natural Language Query (NLQ) – “Ask the AI Analyst”

The function ai_query(question: str) lets you ask questions like:

print(ai_query("Which category earns the most revenue?"))
print(ai_query("Which category has most orders?"))


Internally it:

Looks for keywords like "revenue" or "orders"

Chooses the correct SQL query

Runs query on SQLite

Wraps the result in a friendly business explanation, e.g.:

The Electronics category generates the highest revenue of ₹XYZ.
Strategy: Increase marketing and premium offerings in this category.

This simulates how a junior BI Analyst + AI assistant would answer management.

🚀 How to Run the Project

Clone or download this repository.

Create a virtual environment (optional but recommended):

python -m venv .venv
source .venv/bin/activate   # on Linux/Mac
# or
.venv\Scripts\activate      # on Windows


Install dependencies:

pip install -r requirements.txt


Or, if you don’t have a requirements.txt yet, install directly:

pip install pandas sqlite3-binary matplotlib seaborn transformers torch


Run the script or notebook:

For notebook: open AI-Assisted Sales Insights System for E-Commerce.ipynb and run all cells

For script:

python "AI-Assisted Sales Insights System for E-Commerce.py"


Check:

console output for SQL results and AI insights

charts popping up for revenue, orders, sentiment

responses from ai_query() calls

📌 What This Project Demonstrates

✅ End-to-end mini analytics pipeline (data → SQL → charts → AI)

✅ How to connect SQL + Python + NLP in one workflow

✅ How AI can:

analyse customer text

generate business-style summaries

answer questions in natural language

✅ Clear, interview-friendly example for roles like:

Data Analyst

Business Analyst

Analytics Engineer

AI + Data Hybrid roles

🌱 Possible Extensions

Add more columns (city, channel, discount, return_flag)

Train / fine-tune your own sentiment model

Build a Streamlit or Gradio app for interactive Q&A

Connect to a real e-commerce dataset (Kaggle, etc.)

Replace rule-based ai_query with a small LLM that generates SQL

👩‍💻 Author

Neha Jhakra
Data & AI Enthusiast | SQL • Python • Analytics • Generative AI

Feel free to connect with me on LinkedIn and share feedback or suggestions!
