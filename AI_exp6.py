import nltk
from nltk.corpus import treebank
from nltk.tag import hmm

# Download the Penn Treebank dataset for training
nltk.download('treebank')

# Load the Penn Treebank tagged sentences
tagged_sentences = treebank.tagged_sents()

# Split the data into training and testing sets
train_size = int(0.8 * len(tagged_sentences))
train_data = tagged_sentences[:train_size]
test_data = tagged_sentences[train_size:]

# Train the Hidden Markov Model
hmm_tagger = hmm.HiddenMarkovModelTagger.train(train_data)

# Evaluate the model on the test data
accuracy = hmm_tagger.evaluate(test_data)
print("HMM POS Tagging Accuracy: {:.2%}".format(accuracy))

# Sample text for tagging
sample_text = "This is a sample sentence."

# Tokenize the sample text
tokens = nltk.word_tokenize(sample_text)

# Use the trained HMM model to tag the tokens
pos_tags = hmm_tagger.tag(tokens)

# Display the POS tags for the sample text
print("POS Tags for Sample Text:")
for token, pos_tag in pos_tags:
    print(f"{token}: {pos_tag}")