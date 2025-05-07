# 🧠 Customer Segmentation using RFM Analysis (MySQL + Python)

This project performs customer segmentation using **Recency, Frequency, Monetary (RFM)** analysis based on purchase behavior data stored in a **MySQL database**. It helps identify top customers, loyal customers, frequent buyers, and more using advanced Python data analysis.

---

## 📊 Project Goals

- Connect Python to MySQL and fetch customer purchase data
- Calculate RFM metrics per customer
- Segment customers using RFM scores
- Visualize segments using bar charts
- Practice SQL + Python + EDA together

---

## 🛠 Tools & Libraries

- **MySQL** (Database)
- **Python 3.13+**
- **pandas**
- **matplotlib**
- **seaborn**
- **sqlalchemy**
- **pymysql**

---

## 📁 Dataset Info

**Table:** `customer_orders`  
**Total Records:** 500 rows  
**Fields:**
- `order_id`
- `customer_id`
- `order_date`
- `product_category`
- `product_name`
- `quantity`
- `price`
- `total_amount`
- `payment_method`
- `country`
- `city`

---

## 📈 RFM Segmentation Logic

Each customer is scored from 1–4 (higher is better) based on:
- **Recency:** Days since last purchase
- **Frequency:** Number of orders
- **Monetary:** Total amount spent

Then customers are classified into:
- `Top Customer`: R=4, F=4, M=4
- `Loyal Customer`: High Recency
- `Frequent Buyer`: High Frequency
- `Big Spender`: High Monetary
- `Others`

---

## 📷 Output Example

![RFM Chart](visuals/rfm_segments_chart.png)

---

## ▶️ How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the analysis script
python script/rfm-analysis.py
