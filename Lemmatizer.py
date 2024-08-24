# import snowballstemmer # pip install snowballstemmer
from snowballstemmer import stemmer

# Instanting the Indicstemmer object for hindi Language.
stemmer = stemmer('hindi')

# collecting the preprocessing text strings 
with open('HindiSampleText.Txt', 'r', encoding='utf-8') as f:
    text = f.read()

def Lemmatizer():
    # Tokenize text into words.
    words = text.split()
    # stemming each word in text.
    stemmed_words = [stemmer.stemWord(word) for word in words]
    # joining the stemmed words back into a single string.
    stemmed_text = ' '.join(stemmed_words)
    # Generating the stemmed text.
    with open('LemmatizedSample.Txt', 'w', encoding='utf-8') as f:
        f.write(stemmed_text)

Lemmatizer()
