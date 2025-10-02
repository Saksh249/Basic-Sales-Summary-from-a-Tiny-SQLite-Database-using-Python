import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
db_path = r"C:\Users\USER\Downloads\sales_data.db"
conn = sqlite3.connect(db_path)

# Step 2: SQL query - total quantity and revenue per product
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
"""

# Step 3: Load result into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Close connection
conn.close()

# Step 5: Display the result
print("=== Sales Summary ===")
print(df)

# Step 6: Plot bar chart of Revenue by Product
df.plot(kind="bar", x="product", y="revenue", legend=False)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart image (optional)
plt.savefig("sales_chart.png")
plt.show()
