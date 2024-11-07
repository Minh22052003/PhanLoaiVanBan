from bs4 import BeautifulSoup
import requests
import csv
import os

class Category:
    def __init__(self, category_href, category_text):
        self.category_href = category_href
        self.category_text = category_text
        pass
    def get_category_href(self):
        return self.category_href
    
    def get_category_text(self):
        return self.category_text
    



class DLDV:
    def __init__(self, trangweb, class_title, class_content, Category, end):
        self.trangweb = trangweb
        self.class_title = class_title
        self.class_content = class_content
        self.Category = Category
        self.end = end
        pass

    def get_trangweb(self):
        return self.trangweb
    
    def get_class_title(self):
        return self.class_title
    
    def get_class_content(self):
        return self.class_content
    
    def get_category(self):
        return self.Category
    
    def get_end(self):
        return self.end
    

# Lấy danh sách các URL bài báo từ một trang chuyên mục
def get_article_urls(category_url, trangweb, class_title):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    session = requests.Session()
    response = session.get(category_url, headers=headers, timeout=100)
    
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        base_url = str(trangweb)
        urls = [base_url + link['href'] for link in soup.find_all('a', class_=str(class_title)) if link.get('href')]
        
        return urls
    else:
        print("Không thể truy cập trang. Mã lỗi:", response.status_code)
        return []


# Lấy nội dung bài báo
def extract_article_content(article_url, category, class_content):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    session = requests.Session()
    response = session.get(article_url, headers=headers, timeout=100)
    
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        content_div = soup.find('div', class_=str(class_content))
        content_paragraphs = content_div.find_all('p') if content_div else []
        content = '\n'.join([p.get_text(strip=True) for p in content_paragraphs])

        return category, content

    else:
        print("Không thể truy cập trang. Mã lỗi:", response.status_code)
        return []
    

def cao1theloai(trangweb, Category, end, filename, class_title, class_content):
    base_category_url = str(trangweb)+str(Category.get_category_href())+'?page='
    article_urls =[]
    folder_path = "Datasetsadd"
    file_path = os.path.join(folder_path, filename)

    
    for page in range(55, int(60)):
        category_url = base_category_url + str(page)
        tmp = get_article_urls(category_url, trangweb, class_title)
        article_urls.extend(set(tmp))
    if not os.path.exists(file_path):
        with open(file_path, mode='w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['STT', 'Category', 'Content'])
            # Lặp qua các URL bài báo và trích xuất nội dung
            for i, url in enumerate(article_urls, start=1):
                category, content = extract_article_content(url, Category.get_category_href(), class_content)
                writer.writerow([i, Category.get_category_text(), content])
                
        print(f"Đã cào thể loại {Category.get_category_text()} số lượng {len(article_urls)} bài báo")

