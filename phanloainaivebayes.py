text = "Lỗi đầu tiên là có thể lợi dụng lỗ hổng WMF này để tung ra các cuộc tấn công từ chối dịch vụ. Lỗi thứ hai là nó đã ảnh hưởng đến một file hạt nhân của Windows là explorer.exe và sẽ gây nên hiện tượng sập hệ thống Windows khi người dùng ngây thơ lỡ bật ra xem các file ảnh WMF đã được chế tạo chuyên dùng để tấn công vào lỗi bảo mật này. Trình Explorer ảnh hưởng đến toàn bộ giao diện Windows bao gồm cả Start Menu, Taskbar, Desktop và File manager. "

from tienxuly import bag_of_words



def train_naive_bayes(data):
    label_word_counts = {}
    label_counts = {}

    for words, label in data:
        if label not in label_word_counts:
            label_word_counts[label] = {}
            label_counts[label] = 0
        label_counts[label] += 1
        for word, count in words.items():
            if word not in label_word_counts[label]:
                label_word_counts[label][word] = 0
            label_word_counts[label][word] += count
    
    return label_word_counts, label_counts

def predict_naive_bayes(sample, label_word_counts, label_counts):
    total_samples = sum(label_counts.values())
    max_prob = -1
    best_label = None

    for label in label_counts:
        prob = label_counts[label] / total_samples
        for word, count in sample.items():
            word_prob = (label_word_counts[label].get(word, 0) + 1) / (sum(label_word_counts[label].values()) + len(sample))
            prob *= word_prob ** count
        if prob > max_prob:
            max_prob = prob
            best_label = label
            
    return best_label

# Dữ liệu huấn luyện (giả sử đã xử lý bằng bag_of_words)
data = [
    (bag_of_words("liveshow âm nhạc tháng 4 ..."), "Âm nhạc"),
    (bag_of_words("chương trình thể thao ..."), "Thể thao")
]

label_word_counts, label_counts = train_naive_bayes(data)
sample = bag_of_words("Đoạn văn về âm nhạc ...")
print("Dự đoán:", predict_naive_bayes(sample, label_word_counts, label_counts))
