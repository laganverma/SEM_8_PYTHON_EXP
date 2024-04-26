from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# List of words
words = ['Likes', 'Liked', 'Likely', 'Hoping', 'Playing', 'Played', 'died', 'Laughed', 'Sleeping']

for w in words:
    print(w, ":", ps.stem(w))
