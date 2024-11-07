from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd

# Bag of Words
from sklearn.feature_extraction.text import CountVectorizer
# TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer


def train_model(data):
    X = data['Content']
    y = data['Category']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    vectorizer = CountVectorizer(ngram_range=(1, 2))
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_vectorized, y_train)

    y_pred = model.predict(X_test_vectorized)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Độ chính xác của mô hình: {accuracy * 100:.2f}%")
    return model, vectorizer


data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetSC.csv')
train_model(data)



# ----------------------------------------------------------------------------------------------------------------------------------------------------


# Mô hình với dữu liệu cấp kí tự
# import pandas as pd

# # Đọc dữ liệu
# data = pd.read_csv('D:/PHANLOAIVANBAN/DatasetSCaLBT80%.csv')

# # Chia văn bản thành các đoạn không vượt quá 2096 ký tự
# data['text_segments'] = data['Content'].apply(lambda x: [x[i:i + 2096] for i in range(0, len(x), 2096)])
# data = data.explode('text_segments').reset_index(drop=True)

# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer

# vectorizer = CountVectorizer(analyzer='char')
# X = vectorizer.fit_transform(data['text_segments'])


# # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
# X_train, X_test, y_train, y_test = train_test_split(X, data['Category'], test_size=0.2, random_state=42)

# model = MultinomialNB()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred)
# print(f"Độ chính xác của mô hình: {accuracy * 100:.2f}%")


# ----------------------------------------------------------------------------------------------------------------------------------------------------


