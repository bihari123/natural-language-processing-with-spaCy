from spacy.matcher import Matcher
import spacy
from spacy import displacy

# loading a model
nlp = spacy.load("en_core_web_sm")  # core english language (small veersion)

# appying this model on the sentence
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')  # u for unicode
# each of the word become token

for token in doc:
    print(token.text, token.pos_) # pos = part of speech

print(f'{nlp.pipeline}')

doc2=nlp(u'Tesla is not looking for startups anymore')

for token in doc2:
    print(token.text, token.pos_, token.dep_) # dep = dependency


doc4= nlp(u"This is the first sentence. This is another sentence. This is the last sentence")   
# looping over the sentences
for sentence in doc4.sents:
    print(f"{sentence}")
    

# is a particular token the start of a sentence

print(f"{doc4[6].is_sent_start}")

doc = nlp(u"Apple us going to build a UK factory for $6 million")
displacy.render(doc, style='dep', jupyter=False,options={'distance':50}) # for rendering in jupyter notebook
displacy.serve(doc, style='dep', port = 80)

doc5=nlp(u"I am runner running in a race because I love to run since I ran today")

# lemmatization
for token in doc5:
    print(token.text,'\t', token.pos_,'\t', token.lemma, '\t', token.lemma_)


matcher = Matcher(nlp.vocab)


pattern1= [{'LOWER':'solarpower'}]
pattern2=[{'LOWER':'solar'},{'IS_PUNCT':True},{'LOWER':'power'}]
patern3=[{'LOWER':'solar'},{}]
