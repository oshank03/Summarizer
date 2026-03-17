import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import heapq

text = """
Artificial Intelligence is transforming the world.
It is used in healthcare, finance, education, and many other fields.
AI helps automate tasks and improve efficiency.
However, it also raises ethical concerns.
Researchers are working to make AI systems more transparent and fair.
"""

sentences = sent_tokenize(text)

stop_words = set(stopwords.words('english'))

word_frequencies = {}

for sentence in sentences:
    words = word_tokenize(sentence)

    for word in words:
        if word not in stop_words and word not in string.punctuation:

            # Now counting frequencies
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1

max_frequency = max(word_frequencies.values())

for word in word_frequencies:
    word_frequencies[word] = word_frequencies[word] / max_frequency

sentence_scores = {}

for sentence in sentences:
    words = word_tokenize(sentence.lower())

    for word in words:
        if word in word_frequencies:

            if sentence in sentence_scores:
                sentence_scores[sentence] += word_frequencies[word]
            else:
                sentence_scores[sentence] = word_frequencies[word]

summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)

summary = " ".join(summary_sentences)

print(summary)