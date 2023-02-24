#spaCy stores all shared data in a vocabulary, the Vocab.

# This includes words, but also the labels schemes for tags and entities.

# To save memory, all strings are encoded to hash IDs. If a word occurs more than once, we don't need to save it every time.

# Instead, spaCy uses a hash function to generate an ID and stores the string only once in the string store. The string store is available as nlp.vocab.strings.

# It's a lookup table that works in both directions. You can look up a string and get its hash, and look up a hash to get its string value. Internally, spaCy only communicates in hash IDs.

# Hash IDs can't be reversed, though. If a word is not in the vocabulary, there's no way to get its string. That's why we always need to pass around the shared vocab.

import spacy
nlp = spacy.blank("en")

nlp.vocab.strings.add("coffee")
coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]

# To get the hash for a string, we can look it up in nlp.vocab.strings.

# To get the string representation of a hash, we can look up the hash.

# A Doc object also exposes its vocab and strings.

doc = nlp("I love coffee")
print("hash value:", nlp.vocab.strings["coffee"])
print("string value:", nlp.vocab.strings[3197928453018144401])

# The doc also exposes the vocab and strings
doc = nlp("I love coffee")
print("hash value:", doc.vocab.strings["coffee"])

#Lexemes are context-independent entries in the vocabulary.

# You can get a lexeme by looking up a string or a hash ID in the vocab.

# Lexemes expose attributes, just like tokens.

# They hold context-independent information about a word, like the text, or whether the word consists of alphabetic characters.

# Lexemes don't have part-of-speech tags, dependencies or entity labels. Those depend on the context.

doc = nlp("I love coffee")
lexeme = nlp.vocab["coffee"]

# Print the lexical attributes
print(lexeme.text, lexeme.orth_, lexeme.is_alpha)
