+ Tên ứng dụng
  Phân loại văn bản tiếng Việt dựa trên thuật toán Naive Bayes
+ Nguồn dữ liệu
  Dữ liệu được lấy về từ trang web VOV.vn, 1 trang báo điện tử lớn của Việt Nam. 
 ![image](https://github.com/user-attachments/assets/31eefb55-12d3-4f9c-9aa1-912c1afeed01)

  Nội dung được đăng tải rất đa dạng, các bài viết đều được con người viết và phân loại nên độ chính xác của dữ liệu gần như 100%.
  Trang báo có các danh mục như Chính trị, Xã hội, Thế giới, ... mỗi 1 danh mục lại chứa rất nhiều các bài viết khác nhau nên rất thích hợp để làm dữ liệu cho bài toán phân loại văn bản
+ Cách thức thực hiện
  Quy trình thu thập dữ liệu từ website VOV.vn
    -	Công cụ sử dụng: thư viện BeautifulSoup của python
    -	Khi click vào 1 thể loại của trang web thì đường dẫn sẽ chuyển đổi thành https://vov.vn/chinh-tri với /chinh-tri là tên của các thể loại
    -	Phân tích cấu trúc trang web, các thẻ chứa thể loại nằm trong thẻ <a> có thuộc tính class=”nav-link fw-normal nowrap” href = “/thể-loại” và giá trị chính là tên thể loại
     ![image](https://github.com/user-attachments/assets/1fd6eed7-b8c1-4dc4-8808-73e0790fd59f)

    -	Trong mỗi 1 trang sau khi lựa chọn thể loại thì sẽ tìm ra đc các thẻ a có thuộc tính class=”vovvn-title” và thuộc tính href chứa liên kết tới các bài báo đó.
     ![image](https://github.com/user-attachments/assets/0a46ebc1-4d0e-461d-9c6f-ddf87d36a886)

    -	Trong mỗi bài báo nội dung bài báo nằm trong các thẻ <p> chúng ta sẽ tiến hành lấy nội dung này
     ![image](https://github.com/user-attachments/assets/2fa965a5-20c9-4bb8-b265-925be1dd1f2c)

    -	Dữ liệu được lấy 10 thể loại, mỗi loại sẽ lấy 490 bài báo, dữ liệu sẽ được lưu vào file csv theo định dạng gồm 3 cột STT, Category, Content
     ![image](https://github.com/user-attachments/assets/23deb0ab-4993-429f-bd3d-4c897b1148a7)

Tiền xử lý dữ liệu: 
  + Dữ liệu được chuyển đổi từ file csv sang DataFrame dựa trên thư viện Pandas để dễ dàng xử lý dữ liệu
 ![image](https://github.com/user-attachments/assets/72cba9dc-b45d-46a6-ad49-ca5edcae0adf)

  + Loại bỏ các kí tự html, icon còn sót lại sau quá trình cào dữ liệu từ trang web
  + Chuyển chữ hoa về chữ thường
	 - Công cụ thực hiện:
      ![image](https://github.com/user-attachments/assets/56538458-8f66-4b4c-8813-be3910381186)

	   ![image](https://github.com/user-attachments/assets/87a7cd52-6bca-4a66-ad3f-4835c00ecaeb)
          Thống kê bộ dữ liệu ban đầu.
     ![image](https://github.com/user-attachments/assets/023cbb9d-ab79-46de-910c-d7bd87a173ad)
          Thống kê phân phối độ dài văn bản
+ Công cụ thực hiệng: thư viện pandas và matplotlib để tính toán và hiển thị dữ liệu sau thống kê.
+ Đối với dữ liệu bị thiếu, tiến hành xóa các hàng dữ liệu đó. Với các dữ liệu bị thiếu > 5% thì thực hiện bổ xung thêm dữ liệu để đảm bảo sự tương quan giữa các thể loại.
   ![image](https://github.com/user-attachments/assets/031126dc-d741-453b-9775-ea7429e138e5)
  Bộ dữ liệu sau khi làm sạch

+ Loại bỏ các từ có tần suất xuất hiện lớn hơn 80% trong toàn bộ dữ liệu Content 
  - Công cụ thực hiện: hàm Counter từ thư viện collections giúp cho việc đếm và thống kê từ trong toàn bộ dữ liệu dễ dàng
+ Loại bỏ stopwords, các từ mà xuất hiện nhưng ít mang ý nghĩa quan trọng không ảnh hưởng nhiều đến ngữ nghĩa. Danh sách từ stopword cho tiếng Việt được tham khảo ở https://github.com/stopwords/vietnamese-stopwords do Van-Duyet Le tạo
	- Công cụ thực hiện: Python hỗ trợ đọc file stopwords sau đó tiến hành loại bỏ ở dữ liệu thông qua vòng lặp
	
Biểu diễn đặc trưng:
  + Có 3 cách tiếp cận để biểu diễn và phân tích văn bản là dựa trên kí tự, từ và hợp từ
    Kí tự 	Phân tích mức ký tự, hiệu quả cho văn bản phức tạp hoặc lỗi chính tả.
    Từ	Phân tích mức từ, phổ biến và hiệu quả trong việc biểu diễn ý nghĩa.
    Hợp từ	Phân tích mức hợp từ, giữ ngữ cảnh và biểu thị ý nghĩa cụm từ.
  + Sử dụng 3 cách tiếp cận trên để thực hiện đo độ chính xác của thuật toán naïve bayes với dữ liệu đầu vào.
  + Sử dụng Bag-of-word và TF-IDF để chuyển đổi văn bản thành các vector số 
    - Bag-of-word sẽ chuyển đổi dữ liệu văn bản dựa trên tần suất xuất hiện của các từ trong dữ liệu. Trong mô hình BoW, văn bản sẽ được biểu diễn bởi các từ đơn lẻ, không quan tâm đến ngữ pháp hay vị trí của câu.
    - TF-IDF: sẽ biểu diễn văn bản nhằm nhấn mạnh các từ có ý nghĩa hơn trong văn bản bằng cách xem xét tần cả tần suất từ trong tài liệu và tần suất của từ trong toàn bộ tập hợp tài liệu. 
     ![image](https://github.com/user-attachments/assets/b15cf58e-9067-4617-815b-29bc5a0f2ad9)

  	  TF (Term Frequency): Tần suất từ xuất hiện trong tài liệu. 
      Đo lường mức độ xuất hiện của từ trong tài liệu cụ thể. 
      Nếu TF cao là từ đó xuất hiện nhiều trong dữ liệu và có khả năng quan trọng trong ngữ cảnh của tài liệu đó
  	  IDF (Inverse Document Frequency): Tần suất nghịch đảo tài liệu.
  		Đo lường mức độ phổ biến của từ trong toàn bộ tập hợp tài liệu.
      Nếu một từ xuất hiện trong hầu hết tài liệu, IDF của từ đó sẽ thấp, vì nó không phải là một từ đặc biệt. Ngược lại, nếu một từ chỉ xuất hiện trong một vài tài liệu, IDF của từ đó sẽ cao, cho thấy từ này có tính đặc trưng cao hơn.
    - Công cụ thực hiện: thư viện sklearn.feature_extraction.text hỗ trợ cả 2 kiểu chuyển đổi trên thông qua hàm CountVectorizer cho Bag-of-word và TfidfVectorizercho TF-IDF
Áp dụng vào thuật toán:
	 ![image](https://github.com/user-attachments/assets/32dc3aba-2e49-4a5a-8d6c-a028b7902642)

Công cụ thực hiện: Thư viện sklearn.naive_bayes hỗ trợ các thuật toán Bayes như GaussianNB, MultinomialNB, BernoulliNB, với bài toán phân loại văn bản ta sử dụng MultinomialNB 
 ![image](https://github.com/user-attachments/assets/0884b0d1-d276-4f52-bc3b-eb733d8e476c)

Kết quả
 ![image](https://github.com/user-attachments/assets/c64fefb4-7a91-4a09-b544-1a97d800754f)

Bảng thống kê độ chính xác của thuật toán với các loại dữ liệu
	Dự đoán thử với 1 đoạn văn bản:
 ![image](https://github.com/user-attachments/assets/368c0221-02fe-434f-b0d8-d368ef3ccb25)
Kết luận:
Thuật toán Naive Bayes là 1 thuật toán đơn giản, cần ít dữ liệu huấn luyện nhưng vẫn đưa ra được độ chính xác tương đối: 87%-88%.
Phụ thuộc không nhiều vào dữ liệu huấn luyện đầu vào
Đạt hiệu quả cao nhất khi kết hợp với chuyển đổi dữ liệu văn bảng sang số liệu bằng Bag-of-word
