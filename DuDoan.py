import pandas as pd
from Model import train_model

data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetSC.csv')


def predict_category(model, vectorizer, new_text):
    new_text_vectorized = vectorizer.transform([new_text])
    predicted_category = model.predict(new_text_vectorized)
    return predicted_category[0]

model, vectorizer = train_model(data)

new_text = """Mike Garvonic giơ biểu ngữ mang số 47 chúc mừng ứng viên đảng Cộng hòa sẽ trở thành tổng thống thứ 47 của nước Mỹ, trong sự kiện theo dõi bầu cử rạng sáng 6/11 tại trung tâm hội nghị Suburban Showplace Collection ở Novi, bang Michigan.
Ông Trump đã giành chiến thắng tại hàng loạt bang chiến trường trọng yếu gồm Pennsylvania, Bắc Carolia, Georgia, Wisconsin, vượt ngưỡng 270 đại cử tri để đắc cử tổng thống.Ông Trump phát biểu trên sân khấu ở West Palm Beach, Florida bên cạnh là vợ và con trai út.
Ông khẳng định đã "làm nên lịch sử", đồng thời cam kết đem tới "thời kỳ huy hoàng" cho nước Mỹ. "Đây là phong trào chưa từng có, thật lòng mà nói, tôi tin đây là phong trào chính trị vĩ đại nhất mọi thời đại. Chưa từng diễn ra điều tương tự ở đất nước này, có thể là cả sau này cũng không có chuyện tương tự",
 Trump đề cập về phong trào MAGA (Đưa nước Mỹ vĩ đại trở lại) của mình."""

predicted_category = predict_category(model, vectorizer, new_text)
print(f"Đoạn văn cần dự đoán: {new_text}")
print(f"Nhãn dự đoán cho văn bản mới: {predicted_category}")