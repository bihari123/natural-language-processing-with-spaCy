# You've already written this plenty of times by now: pass a string of text to
# the nlp object, and receive a Doc object.

# But what does the nlp object actually do?

# First, the tokenizer is applied to turn the string of text into a Doc object.
# Next, a series of pipeline components is applied to the doc in order.
# In this case, the tagger, then the parser, then the entity recognizer.
# Finally, the processed doc is returned, so you can work with it.
