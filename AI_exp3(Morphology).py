import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def analyze_morphology(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Initialize lists to store prefixes, suffixes, and roots
    prefixes = []
    suffixes = []
    roots = []

    for word in words:
        # Extract prefixes, suffixes, and roots
        for i in range(1, len(word)):
            prefixes.append(word[:i])
            suffixes.append(word[-i:])
        roots.append(word)

    return {
        'prefixes': set(prefixes),
        'suffixes': set(suffixes),
        'roots': set(roots)
    }

# Example text
text = """ Organizing is a practice of leadership whereby we define leadership 
as enabling others to achieve shared purpose under conditions of uncertainty."""

# Analyze the morphology of the text
morphology_analysis = analyze_morphology(text)

# Print the results
print("\nPrefixes:", morphology_analysis['prefixes'])
print("\nSuffixes:", morphology_analysis['suffixes'])
print("\nRoots:", morphology_analysis['roots'])