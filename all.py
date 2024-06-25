import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Sample text
text = "New Study Reveals Surprising Health Benefits of Plant-Based Diets"


# Tokenize the text
tokens = word_tokenize(text)

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Get the list of stop words
stop_words = set(stopwords.words('english'))

# Perform stemming, lemmatization, and remove stop words
stemmed_words = [stemmer.stem(word) for word in tokens]
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
filtered_words = [word for word in tokens if word.lower() not in stop_words]

# Print results
print("Original Tokens:", tokens)
print("Stemmed Words:", stemmed_words)
print("Lemmatized Words:", lemmatized_words)
print("Filtered Words (Stop Words Removed):", filtered_words)
