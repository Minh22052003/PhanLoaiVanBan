# from Caodulieu import Category
# import Caodulieu

# list_category = [
#     # Category('kinh-te', 'Kinh tế'),
#     # Category('the-thao', 'Thể thao'),
#     # Category('van-hoa', 'Văn hóa'),
#     # Category('xa-hoi', 'Xã hội'),
#     Category('oto-xe-may', 'Ô tô - Xe máy'),
# ]

# # new_categories = {
# #     'the-gioi': 'Thế giới',
# #     'xa-hoi': 'Xã hội',
# #     'kinh-te': 'Kinh tế',
# #     'thi-truong': 'Thị trường',
# #     'quan-su-quoc-phong': 'Quân sự - Quốc phòng',
# #     'the-thao': 'Thể thao',
# #     'oto-xe-may': 'Ô tô - Xe máy',
# #     'cong-nghe': 'Công nghệ',
# # }

# # # Thêm từng thể loại từ new_categories vào list_category
# # for url, name in new_categories.items():
# #     list_category.append(Category(url, name))

# for category in list_category:
#     dldv =Caodulieu.DLDV('https://vov.vn/', 'vovvn-title', 'article-content', category,50)
#     trangweb = dldv.get_trangweb()
#     class_title = dldv.get_class_title()
#     class_content = dldv.get_class_content()
#     category = dldv.get_category()
#     end = dldv.get_end()
#     filename = category.category_href+'.csv'
#     Caodulieu.cao1theloai(trangweb, category, end, filename, class_title, class_content)    

# Gộp thành 1 file csv
import pandas as pd
import glob

path = 'D:/PHANLOAIVANBAN/Datasets/'

all_files = glob.glob(path + "*.csv")
dfs = []

for filename in all_files:
    df = pd.read_csv(filename)
    dfs.append(df)
merged_df = pd.concat(dfs, ignore_index=True)

print(merged_df.head())

merged_df.to_csv('D:/PHANLOAIVANBAN/merged_dataset.csv', encoding='utf-8-sig', index=False)

