# 🤖 AI-Assisted Sales Insights System for E-Commerce

This project showcases the integration of **Data Analytics + SQL + Python + AI (NLP + LLM Logic)** to automate real-world business insights for e-commerce.

Instead of manually writing conclusions after analysis…  
AI automatically:
- interprets sales data,
- reads customer feedback,
- and answers business questions in **natural language** — just like an Analyst!

---

## 🎯 Project Objective

The main goal of this project is to build a system that:

| Task | Technology |
|------|------------|
| Analyze sales performance | SQL |
| Visualize insights | Python (Matplotlib + Seaborn) |
| Understand customer feedback | NLP (Sentiment Analysis Model) |
| Generate business insights + suggestions | AI |
| Conversational Q&A on data | NLQ → SQL → AI response |

This project proves:  
✨ **AI empowers analysts — AI doesn’t replace them.**

---

## 📂 Dataset Description

Small but realistic dataset of **30 e-commerce transactions** embedded in code.

| Column | Description |
|--------|------------|
| order_id | Unique ID |
| product_category | Electronics / Fashion / Home Appliances |
| quantity | Units purchased |
| price | Selling price (₹) |
| purchase_date | Order date |
| customer_feedback | Customer review text |

> Mixed numerical + textual data → perfect for combining Analytics + NLP.

---

## 🧠 Tech Stack

- **Python**
- **SQLite**
- **Pandas**
- **Matplotlib + Seaborn**
- **HuggingFace Transformers** (`sentiment-analysis` pipeline)

---

🧮 SQL Analysis Examples

✔ Total Revenue
✔ Revenue by Category
✔ Orders by Category
✔ Average Price by Category

Example Query:

SELECT product_category,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product_category
ORDER BY revenue DESC;


📌 Result:

Electronics → highest revenue 💰

Fashion → most orders 🛍️

Home Appliances → high price but complaints ⚠️

📊 Visualizations

Revenue by Category — Bar Chart

Orders by Category — Bar Chart

Sentiment Distribution — Positive vs Negative

These validate SQL findings visually for leadership understanding.

🗣 NLP Sentiment Analysis

Customer reviews are analyzed using HuggingFace’s sentiment pipeline.

Example insights:

Electronics: Mostly positive

Fashion: Good satisfaction

Home Appliances: Higher negative sentiment

“damaged”

“wrong item”

“stopped working”

📌 Action Needed: Improve quality control & delivery.

🤖 AI-Generated Insights

AI automatically writes:

Key Findings

Business Risks

Data-Driven Recommendations

1-Line Executive Summary

Example Output:

Electronics drives the highest revenue due to strong demand.
Focus marketing here & optimize pricing for greater ROI.

💬 Natural Language Query System (NLQ)

Ask business questions without writing SQL:

ai_query("Which category earns the most revenue?")


Output (example):

Electronics generates highest revenue of ₹X.
Recommendation: Expand product range & promotions.

📌 This enables Conversational BI — future of data analytics.

🚀 How to Run This Project
1️⃣ Clone Repository
git clone https://github.com/your-username/AI-Sales-Insights.git
cd AI-Sales-Insights

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Notebook or Script
jupyter notebook
# OR
python "AI-Assisted Sales Insights System for E-Commerce.py"

📌 Folder Structure
📁 AI-Ecommerce-Insights
│── README.md
│── AI-Assisted Sales Insights System.py
│── sales_data.db
│── requirements.txt
│── 📊 visuals_output/
│     │── revenue_chart.png
│     │── orders_chart.png
│     │── sentiment_chart.png

📈 Key Takeaways
Area	Results
Revenue Insight	Electronics dominates
Customer Insight	Home Appliances need improvement
Analyst Skill	SQL + Python + AI combined
Business Value	Faster decisions with automated insights
🌱 Future Improvements

Add real dataset from Kaggle

Add dashboard UI (Streamlit or Power BI)

Let AI generate SQL automatically (full NLQ)

Deploy as an interactive BI tool

👩‍💻 Author

Neha Jhakra
Data Analyst | Python | SQL | NLP | Generative AI
📌 Passionate about Data + AI integration

🔗 LinkedIn: www.linkedin.com/in/neha-jhakra-395a201a2

⭐ If you like this project, consider giving it a Star!

📌 Conclusion

This project shows how AI supercharges the role of a Data Analyst, by:

✔ Automating insights
✔ Understanding customer voice
✔ Enabling natural language exploration of data

🚀 The future belongs to AI-assisted analytics.
