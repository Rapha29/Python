import tika
from tika import parser
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import re

tika.initVM()

# Extrai o texto do PDF
file_data = parser.from_file('livro.pdf')
pdf_content = file_data['content']

# Preprocessa o texto
sentences = sent_tokenize(pdf_content)
words = []
for sent in sentences:
    words.extend(word_tokenize(sent.lower()))
stop_words = set(stopwords.words('portuguese'))
filtered_words = [word for word in words if word not in stop_words]
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
clean_sentences = [' '.join(stemmed_words[i:i+10]) for i in range(0, len(stemmed_words), 10)]

# Codifica as perguntas e respostas como vetores numéricos
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(clean_sentences)
y = clean_sentences

# Divide o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X.toarray(), y, test_size=0.2, random_state=42)

# Treina o modelo com base nas perguntas e respostas
clf = MLPClassifier(max_iter=1500)
clf.fit(X_train, y_train)

# Integra o modelo em um sistema que possa receber perguntas do usuário e gerar respostas
while True:
    user_input = input("Faça uma pergunta: ")
    if user_input.lower() == "sair":
        break
    # Preprocessa a pergunta do usuário
    question_words = []
    for word in word_tokenize(user_input.lower()):
        if word not in stop_words:
            question_words.append(stemmer.stem(word))
    question = ' '.join(question_words)
    # Encontra a sentença mais similar à pergunta do usuário
    max_similarity = -1
    best_sentence = ""
    for sent in clean_sentences:
        similarity = clf.predict_proba(vectorizer.transform([question + " " + sent]))[0][1]
        if similarity > max_similarity:
            max_similarity = similarity
            best_sentence = sent
    # Imprime a resposta encontrada
    print("Resposta: ")
    print(re.sub(r'\[[^\]]*\]', '', best_sentence).strip())