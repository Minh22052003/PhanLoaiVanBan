import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
data = pd.read_csv('D:/PHANLOAIVANBAN/merged_dataset_after.csv')

print(data.head())

# Tạo thống kê số lượng dữ liệu trong từng thể loại
category_counts = data['Category'].value_counts()

# Tính tỷ lệ dữ liệu trống trong cột 'Content' cho từng thể loại
missing_data_by_category = data.groupby('Category')['Content'].apply(lambda x: x.isnull().mean() * 100)

# Gộp thống kê số lượng và tỷ lệ dữ liệu trống vào một DataFrame
combined_stats = pd.DataFrame({
    'Count': category_counts,
    'Missing_Percentage': missing_data_by_category
}).fillna(0)  # Điền giá trị 0 cho các ô không có dữ liệu trống

# Vẽ biểu đồ
fig, ax1 = plt.subplots(figsize=(12, 8))

# Vẽ cột cho số lượng dữ liệu
combined_stats['Count'].plot(kind='bar', color='skyblue', ax=ax1, position=1, width=0.4)
ax1.set_ylabel("Số lượng văn bản", color='skyblue')
ax1.set_xlabel("Thể loại")
ax1.tick_params(axis='y', labelcolor='skyblue')

# Tạo trục thứ hai để hiển thị tỷ lệ dữ liệu trống
ax2 = ax1.twinx()
combined_stats['Missing_Percentage'].plot(kind='bar', color='salmon', ax=ax2, position=0, width=0.4)
ax2.set_ylabel("Tỷ lệ dữ liệu trống (%)", color='salmon')
ax2.tick_params(axis='y', labelcolor='salmon')

# Thiết lập tiêu đề và hiển thị
plt.title("Số lượng dữ liệu trong từng thể loại và tỷ lệ dữ liệu trống sau chia cắt")
plt.xticks(rotation=45)
plt.show()

# Thống kê độ dài của mỗi văn bản để nhận diện ngoại lệ
data['Content_Length'] = data['Content'].apply(lambda x: len(str(x)))

plt.figure(figsize=(10, 6))
sns.histplot(data['Content_Length'], bins=30, kde=True, color='skyblue')
plt.title("Phân phối độ dài của văn bản")
plt.xlabel("Độ dài văn bản")
plt.ylabel("Tần suất")
plt.show()
