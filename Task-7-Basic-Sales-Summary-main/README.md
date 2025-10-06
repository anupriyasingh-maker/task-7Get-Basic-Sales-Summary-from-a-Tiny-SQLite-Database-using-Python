# Task 7 – Basic Sales Summary (SQLite + Python)
#  Overview
This project connects Python to a small SQLite database, runs SQL queries to get basic sales summaries, and visualizes the results in a bar chart.<br>

# Tools Used
Python (sqlite3, pandas, matplotlib)<br>
SQLite (built into Python)

# Files in Repository
create_db.py → Creates sales_data.db with sample sales data<br>
sales_data.db → SQLite database file<br>
sales_summary.py → Runs SQL queries, prints summary, and generates bar chart<br>
sales_chart.png → Bar chart of revenue by product<br>

# What I Did
Created a sales table and inserted sample sales records.<br>
Queried total quantity sold and total revenue per product using SQL with GROUP BY.<br>
Loaded results into pandas for easy manipulation.<br>
Printed the results in the terminal.<br>
Plotted and saved a bar chart showing revenue by product.

# Outcome
Learned to connect Python with SQLite.<br>
Practiced SQL queries inside Python.<br>
Generated and saved a simple sales visualization.
