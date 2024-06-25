import spacy
from gensim.parsing.preprocessing import STOPWORDS

# Load SpaCy English model
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])  # Disable unnecessary components for faster processing

# Sample text
text = "New Study Reveals Surprising Health Benefits of Plant-Based Diets"

# Tokenize and lemmatize using SpaCy
doc = nlp(text)
tokens = [token.text for token in doc]
lemmatized_words = [token.lemma_ for token in doc if not token.is_stop]

# Use Gensim for stemming (Porter Stemmer)
from gensim.parsing.porter import PorterStemmer
porter_stemmer = PorterStemmer()
stemmed_words = [porter_stemmer.stem(word) for word in tokens]

# Filter out stop words using SpaCy and Gensim
filtered_words = [word for word in tokens if word.lower() not in STOPWORDS]

# Print results
print("Original Tokens:", tokens)
print("Lemmatized Words:", lemmatized_words)
print("Stemmed Words:", stemmed_words)
print("Filtered Words (Stop Words Removed):", filtered_words)
