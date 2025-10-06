import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DB_PATH = Path("sales_data.db")

# 1) Connect to SQLite
conn = sqlite3.connect(DB_PATH)

# 2) Run SQL: total quantity and revenue per product
query = '''
SELECT
  product,
  SUM(quantity) AS total_qty,
  SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
'''
df = pd.read_sql_query(query, conn)

# Optional: overall totals
totals = pd.read_sql_query(
    "SELECT SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales;",
    conn
)
conn.close()

# 3) Print results
print("Per-product summary:")
print(df)
print("\nOverall totals:")
print(totals)

# 4) Plot a simple bar chart of revenue by product
plt.figure()
plt.bar(df["product"], df["revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
print("\nSaved chart to sales_chart.png")