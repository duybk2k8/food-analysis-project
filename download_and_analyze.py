import urllib.request
import gzip #để giải nén file .gz
import csv #để đọc file CSV (dạng bảng)
import os #để thao tác với file
import sqlite3

# B1: Tải file
url = "https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz"
compressed_file = "products.csv.gz"
csv_file = "products.csv"

print("Processing data...")
urllib.request.urlretrieve(url, compressed_file) #compressed_file để lưu file .gz khi tải về, urlretrieve để tải file từ url và lưu vào compressed_file => thư mục products.csv.gz
print(compressed_file)


# B2: Giải nén file
print("Extracting file...")
with gzip.open(compressed_file, 'rb') as f_in:
    with open(csv_file, 'wb') as f_out:
        f_out.write(f_in.read())
print(csv_file)
#gzip.open(..., 'rb') dùng để mở file .gz để đọc
#open(..., 'wb'): tạo file mới .csv để ghi dữ liệu giải nén
#f_out.write(f_in.read()): đọc toàn bộ nội dung file nén và ghi ra file .csv => tạo file products.csv

# B3: Phân tích dữ liệu đơn giản
print("Analyzing data...")
print("Saving to SQLite...")

conn = sqlite3.connect("products.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT
    )
""")
cursor.execute("DELETE FROM products")

with open(csv_file, encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    #đọc mỗi dòng trong file CSV thành 1 dictionary
    #delimiter là dùng tab ngăn cách
    count = 0
    categories = {}

    for row in reader:
        category = row.get('categories', '').split(',')[0].strip()
        #row.get: lấy nội dung cột categories
        if category:
            categories[category] = categories.get(category, 0) + 1
            cursor.execute("INSERT INTO products (category) VALUES (?)", (category,))
        count += 1
        #đếm số lần xuất hiện của từng danh mục
        if count > 10000:
            break

conn.commit()
conn.close()


print(count)
print("Top 5 common:")
top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]
for cat, num in top_categories:
    print(f"- {cat}: {num} sản phẩm")
    
#in ra danh mục và số sản phẩm tương ứng

# B4: Ghi kết quả ra file
with open("top_categories.txt", "w", encoding="utf-8") as f:
    for cat, num in top_categories:
        f.write(f"{cat}: {num}\n")
print("Saved in top_categories.txt")
