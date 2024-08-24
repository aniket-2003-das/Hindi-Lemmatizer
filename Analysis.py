# import snowballstemmer # pip install snowballstemmer
from snowballstemmer import stemmer
from collections import defaultdict

# Instanting the Indicstemmer object for hindi Language.
stemmer = stemmer('hindi')

def Analyser():
    # Opening the original text file.
    with open('HindiSampleText.Txt', 'r', encoding='utf-8') as f:
        original_text = f.read().split()

    # opening the Lemmatized file.
    with open('LemmatizedSample.Txt', 'r', encoding='utf-8') as f:
        lemmatized_text = f.read().split()

    # creating a dictionary to store count of original and Lemmatized text.
    results = defaultdict(int)

    # comparing the orignal_text and lemmatized text.
    for i in range(len(original_text)):
        if original_text[i] == lemmatized_text[i]:
            results["correct"] +=1
        else:
            results["incorrect"] += 1

    # calculating the accuracy of the Lemmatizations.
    accuracy = results["correct"] / (results["correct"] + results['incorrect']) * 100

    # Getting the Analysis Report.
    print(f"total words in File-: {len(original_text)}")
    print(f"correct lemmatizations-: {results['correct']}")
    print(f"incorrect lemmatizations-: {results['incorrect']}")
    print(f"accuracy-: {accuracy:.2f}%")

Analyser()
