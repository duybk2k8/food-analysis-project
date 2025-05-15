import sqlite3
import plotly.graph_objects as go

# Kết nối đến database
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Truy vấn top 5 category phổ biến
cursor.execute("""
    SELECT category, COUNT(*) as count
    FROM products
    GROUP BY category
    ORDER BY count DESC
    LIMIT 20
""")
rows = cursor.fetchall()
conn.close()

# Tách dữ liệu ra hai danh sách: category và count
categories = [row[0] for row in rows]
counts = [row[1] for row in rows]

# Tạo biểu đồ bằng plotly.graph_objects (không cần numpy hoặc pandas)
fig = go.Figure(data=[go.Bar(x=categories, y=counts)])

fig.update_layout(
    title="Top 5 Danh Mục Sản Phẩm",
    xaxis_title="Danh mục",
    yaxis_title="Số lượng sản phẩm",
)

# Lưu ra file HTML
fig.write_html("chart.html")
print("Đã lưu biểu đồ vào chart.html")
