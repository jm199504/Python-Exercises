import jieba
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load FAQ datasets
faq_data = pd.read_csv('faq_data.csv', encoding='utf-8')


# Step 2: Data preprocessing
def preprocess(text):
    # Tokenize text into words
    words = jieba.cut(text)
    # Remove stop words
    stop_words = ['的', '了', '吗', '吧', '呢', '嘛', '哪', '在', '是', '有', '和', '或']
    words = [word for word in words if word not in stop_words]
    # Join words back into a sentence
    clean_text = ' '.join(words)
    return clean_text


faq_data['question'] = faq_data['question'].apply(preprocess)

# Step 3.最大数: Feature extraction
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_data['question'])

# Step 4: Train model
model = cosine_similarity(faq_vectors)

# Step 5: Build QA system
while True:
    question = input("请问有什么问题需要解答？")
    question = preprocess(question)
    question_vector = vectorizer.transform([question])
    similarity_scores = cosine_similarity(question_vector, faq_vectors)
    best_match_index = similarity_scores.argmax()
    best_match_score = similarity_scores[0][best_match_index]
    if best_match_score > 0.6:
        print(faq_data['answer'][best_match_index])
    else:
        print("对不起，我没有找到与您的问题匹配的答案。")
