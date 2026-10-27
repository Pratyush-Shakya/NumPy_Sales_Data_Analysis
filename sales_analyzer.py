
import numpy as np

# Daily sales data
sales = np.array([1200, 1500, 900, 2000, 1800, 2200, 1700])

print("===== NUMPY SALES ANALYZER =====")

# 1. Display sales
print("\nDaily Sales:")
print(sales)

# 2. Total sales
print("\nTotal Sales:", np.sum(sales))

# 3. Average salesc
print("Average Sales:", np.mean(sales))

# 4. Highest and lowest sales
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))

# 5. Highest sales day index
print("Highest Sales Day Index:", np.argmax(sales))

# 6. Sales above 1500
print("\nSales Above 1500:")
print(sales[sales > 1500])

# 7. Count days with sales >= 1500
print("Days Meeting Target:", np.sum(sales >= 1500))

# 8. Sorted sales
print("\nSorted Sales:")
print(np.sort(sales))

# 9. Product-wise sales for 3 products over 3 days
product_sales = np.array([
    [1000, 1200, 1500],
    [800, 900, 1100],
    [1300, 1400, 1600]
])

print("\nProduct Sales Data:")
print(product_sales)

# Total sales for each product (each row)
print("\nProduct-wise Total:")
print(np.sum(product_sales, axis=1))

# Total sales for each day (each column)
print("\nDay-wise Total:")
print(np.sum(product_sales, axis=0))
