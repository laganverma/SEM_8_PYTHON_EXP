import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define the text to be chunked
text = "The cat is a mammal. It sat on the mat, and it purred softly."

# Process the text with SpaCy
doc = nlp(text)

# Extract noun phrases, pronoun phrases, and verb phrases
noun_phrases = [chunk.text for chunk in doc.noun_chunks]
pronoun_phrases = [token.text for token in doc if token.pos_ == "PRON"]
verb_phrases = [chunk.lemma_ for chunk in doc if chunk.pos_ == "VERB"]

# Print the extracted phrases
print("Noun Phrases:", noun_phrases)
print("Pronoun Phrases:", pronoun_phrases)
print("Verb Phrases:", verb_phrases)
