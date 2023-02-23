# named entity recognition (NER) seeks to locate and classify named entity mentions in unstructured text into pre-defined categories such as the person names, organisations, localtions, medical codes, time expressions, quantities, monetary values, percentages etc.
# from types import NoneType
import spacy
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + ent.label_)
    else:
        print('no entities found')


# doc = nlp("Hi, How are you?")

# show_ents(doc)

doc = nlp('May I go to Washington DC next May to see the Washington monument?')
show_ents(doc)

doc = nlp('Tesla is going to set up a factory in U.K. for $6 million dollars')
# defining our own label
VERB = doc.vocab.strings['COMPANY']
new_ent = Span(doc, 9, 10, label=VERB)   # from 0 upto (not including) 1

doc.ents.__add__(tuple(new_ent))
show_ents(doc)

doc9 = nlp(
    'Our Company created a brand new vacuum cleaner. This vacuum-cleaner is the best in show'
)


matcher = PhraseMatcher(nlp.vocab)

phrase_list = ['vacuum cleaner', 'vacuum-cleaner']
phrase_patterns = [nlp(text) for text in phrase_list]

matcher.add('newproduct', None, *phrase_patterns)

found_matches = matcher(doc)

PROD = doc9.vocab.strings(u'PRODUCT')

new_ents = [
    Span(doc9, match[1], match[2], label=PROD) for match in found_matches
]

doc.ents = list(doc9.ents) + new_ents
