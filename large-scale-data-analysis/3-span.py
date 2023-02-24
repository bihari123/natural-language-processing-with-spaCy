# A Span is a slice of a doc consisting of one or more tokens.
# The Span takes at least three arguments: the doc it refers to,
# and the start and end index of the span.
# Remember that the end index is exclusive!

# Import the Doc and Span classes
import spacy
from spacy.tokens import Doc, Span

nlp = spacy.blank("en")
# The words and spaces to create the doc from
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Create a doc manually
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Create a span manually
span = Span(doc, 0, 2)

# Create a span with a label
span_with_label = Span(doc, 0, 2, label="GREETING")

# Add span to the doc.ents
doc.ents = [span_with_label]

print(f"{doc.ents}")
