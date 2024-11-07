# # Tiền xử lý dữ liệu tổng quát
# import pandas as pd

# # Đọc file CSV
# df = pd.read_csv('D:/PHANLOAIVANBAN/merged_dataset.csv') 

# # Xóa các hàng có cột 'Content' bị trống
# df_cleaned = df.dropna(subset=['Content'])

# df_cleaned.to_csv('merged_dataset_after.csv', index=False, encoding='utf-8-sig')





# # Xử lý dữ liệu văn bản và để dữ liệu nguyên bản
# import pandas as pd
# import re

# # Bước 1: Đọc file CSV
# data = pd.read_csv('D:/PHANLOAIVANBAN/merged_dataset_after.csv')

# # Bước 2: Làm sạch dữ liệu
# def clean_text(text):
#     text = re.sub(r'<[^>]+>', '', text)
#     text = text.lower()
#     return text

# data['Content'] = data['Content'].apply(clean_text)
# data.to_csv('D:/PHANLOAIVANBAN/DatasetNB.csv', index=False, encoding='utf-8-sig')


# ----------------------------------------------------------------------------------------------------------------------------------------------------


# Xử lý dữ liệu văn bản và để dữ liệu sau khi loại bỏ các từ suất hiện hơn 80% đoạn văn bản

# import pandas as pd
# import re
# from collections import Counter

# data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetSC2.csv')


# all_content = ' '.join(data['Content'])
# words = all_content.split()
# word_counts = Counter(words)

# threshold = 0.8 * len(words)
# common_words = {word for word, count in word_counts.items() if count > threshold}

# def remove_common_words(text):
#     words = text.split()
#     filtered_words = [word for word in words if word not in common_words]
#     return ' '.join(filtered_words)

# data['Content'] = data['Content'].apply(remove_common_words)


# data.to_csv('D:/PHANLOAIVANBAN/DatasetTMP.csv', index=False, encoding='utf-8-sig')

# data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetTMP.csv')

# # Xóa các hàng có cột 'Content' bị trống
# data = data.dropna(subset=['Content'])
# data.to_csv('D:/PHANLOAIVANBAN/DatasetSCaLBT80%.csv', index=False, encoding='utf-8-sig')


# ----------------------------------------------------------------------------------------------------------------------------------------------------


# # Xử lý dữ liệu văn bản và để dữ liệu sau khi loại bỏ các từ dừng
# import pandas as pd
# import re
# from collections import Counter

# # Bước 1: Đọc file CSV
# data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetSC2.csv')

# with open('D:/PHANLOAIVANBAN/vietnamese-stopwords.txt', 'r', encoding='utf-8') as f:
#     stopwords = {line.strip() for line in f}

# def remove_stopwords(text):
#     words = text.split()
#     filtered_words = [word for word in words if word not in stopwords]
#     return ' '.join(filtered_words)

# data['Content'] = data['Content'].apply(remove_stopwords)

# data.to_csv('D:/PHANLOAIVANBAN/DatasetLBSTWTMP.csv', index=False, encoding='utf-8-sig')
# data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetLBSTWTMP.csv')

# # Xóa các hàng có cột 'Content' bị trống
# data = data.dropna(subset=['Content'])
# # Xóa các hàng có cột 'Content' bị trống
# data = data.dropna(subset=['Content'])
# data.to_csv('D:/PHANLOAIVANBAN/DatasetScaLBSTW.csv', index=False, encoding='utf-8-sig')

# ------------------------------------------------------------------------------------------------------------------------------------------------

# # Xử lý dữ liệu văn bản và để dữ liệu sau khi loại bỏ các từ dừng và từ suất hiện hơn 80% đoạn văn bản
# import pandas as pd
# import re
# from collections import Counter

# data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetNB.csv')

# with open('D:/PHANLOAIVANBAN/vietnamese-stopwords.txt', 'r', encoding='utf-8') as f:
#     stopwords = {line.strip() for line in f}

# def remove_stopwords(text):
#     words = text.split()
#     filtered_words = [word for word in words if word not in stopwords]
#     return ' '.join(filtered_words)


# all_content = ' '.join(data['Content'])
# words = all_content.split()
# word_counts = Counter(words)

# threshold = 0.8 * len(words)
# common_words = {word for word, count in word_counts.items() if count > threshold}

# def remove_common_words(text):
#     words = text.split()
#     filtered_words = [word for word in words if word not in common_words]
#     return ' '.join(filtered_words)


# data['Content'] = data['Content'].apply(remove_common_words)
# data['Content'] = data['Content'].apply(remove_stopwords)


# data.to_csv('D:/PHANLOAIVANBAN/DatasetLBSTWa80%TMP.csv', index=False, encoding='utf-8-sig')
# data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetLBSTWa80%TMP.csv')

# # Xóa các hàng có cột 'Content' bị trống
# data = data.dropna(subset=['Content'])

# data.to_csv('D:/PHANLOAIVANBAN/DatasetLBSTWa80%.csv', index=False, encoding='utf-8-sig')



# ------------------------------------------------------------------------------------------------------------------------------------------------

# Chia văn bản thành các đoạn không vượt quá 2096 ký tự
# import pandas as pd

# data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetNB.csv')

# def split_text(text):
#     words = text.split()
#     if len(words) > 1800 and len(words) <2500:
#         part1 = " ".join(words[:600])
#         part2 = " ".join(words[600:])
#         return [part1, part2]
#     else:
#         return [text]


# data['Content'] = data['Content'].apply(split_text)
# data = data.explode('Content').reset_index(drop=True)

# data.to_csv('D:/PHANLOAIVANBAN/DatasetSC3.csv', index=False, encoding='utf-8-sig')



