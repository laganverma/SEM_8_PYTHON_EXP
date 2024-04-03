import spacy

nlp = spacy.load("en_core_web_sm")
text = "I am Lagan and I am a student."

doc = nlp(text)

for token in doc:
    print(token.text, token.pos_, spacy.explain(token.pos_))