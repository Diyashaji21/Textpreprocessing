import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary data
nltk.download('punkt')
text = "Hello world! This is a tokenization example using NLTK."

# Tokenize into words
word_tokens = word_tokenize(text)
print("Word Tokens:", word_tokens)

# Tokenize into sentences
sentence_tokens = sent_tokenize(text)
print("Sentence Tokens:", sentence_tokens)