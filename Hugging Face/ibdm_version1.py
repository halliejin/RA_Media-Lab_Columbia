import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 读取CSV文件
df = pd.read_excel("D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Media Lab/RA_Media-Lab_Columbia/Hugging Face/imdb_dataset_train.xlsx")

# 确保列名正确
df.columns = ['text', 'label']

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# 文本向量化
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# 训练模型
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# 预测
y_pred = model.predict(X_test_vectorized)

# 评估模型
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:', classification_report(y_test, y_pred))
