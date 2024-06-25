1)all.py:    Text Preprocessing with NLTK
This script demonstrates basic text preprocessing techniques using the Natural Language Toolkit (NLTK) in Python. The code performs the following steps:

Download Required NLTK Data:

punkt: For tokenization.
stopwords: For stop words removal.
wordnet and omw-1.4: For lemmatization.
Tokenization:

The input text is tokenized into individual words.
Initialization:

A stemmer (PorterStemmer) and a lemmatizer (WordNetLemmatizer) are initialized.
Stop Words List:

A list of English stop words is retrieved.
Text Processing:

Stemming: Each token is reduced to its root form using the Porter Stemmer.
Lemmatization: Each token is converted to its base or dictionary form using WordNet Lemmatizer.
Stop Words Removal: Tokens that are stop words are removed from the list.
Output:

The script prints the original tokens, the stemmed words, the lemmatized words, and the filtered words (tokens with stop words removed).


2) news.py :  Text Preprocessing with SpaCy and Gensim
This script demonstrates advanced text preprocessing techniques using SpaCy and Gensim in Python. The code performs the following steps:

Load SpaCy Model:

The SpaCy English model (en_core_web_sm) is loaded with unnecessary components (parser and named entity recognizer) disabled for faster processing.
Sample Text:

A sample text is provided for preprocessing.
Tokenization and Lemmatization:

The text is tokenized and lemmatized using SpaCy.
Stop words are removed during the lemmatization process.
Stemming with Gensim:

The Porter Stemmer from Gensim is used to stem each token.
Stop Words Removal:

Stop words are filtered out using a combined list from SpaCy and Gensim.
Output:

The script prints the original tokens, the lemmatized words (excluding stop words), the stemmed words, and the filtered words (tokens with stop words removed).

3) tokens.py : Text Tokenization with NLTK
This script demonstrates basic text tokenization techniques using the Natural Language Toolkit (NLTK) in Python. The code performs the following steps:

Download Required NLTK Data:

The punkt package is downloaded, which is necessary for tokenization.
Sample Text:

A sample text is provided for tokenization.
Word Tokenization:

The text is tokenized into individual words using NLTK's word_tokenize function.
Sentence Tokenization:

The text is tokenized into individual sentences using NLTK's sent_tokenize function.
Output:

The script prints the word tokens and the sentence tokens.
