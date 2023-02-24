import spacy

text = "My secret agent name is John McClane from Boston, hope my identity remains anonymous."

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

for entity in doc.ents:
    print(entity.label_ +": "+ entity.text)
