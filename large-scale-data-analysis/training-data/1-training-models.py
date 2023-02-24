# The entity recognizer takes a document and predicts phrases and their labels
# in context. This means that the training data needs to include texts,
# the entities they contain, and the entity labels.
# Entities can't overlap, so each token can only be part of one entity.

# The easiest way to do this is to show the model a text and entity spans.
# spaCy can be updated from regular Doc objects with entities annotated as
# the doc.ents. For example, "iPhone X" is a gadget, starts at token 0 and
# ends at token 1.

# It's also very important for the model to learn words that aren't entities.

# In this case, the list of span annotations will be empty.

# Our goal is to teach the model to recognize new entities in similar contexts,
# even if they weren't in the training data.

# Import the Doc and Span classes
import spacy
import random
from spacy.tokens import Span, DocBin
nlp = spacy.blank("en")
# nlp = spacy.load("en_core_wb_sm")


doc = nlp("iPhone X is coming")
doc.ents = [Span(doc, 0, 2, label="GADGET")]

# When training your model, it's important to know how it's doing and
# whether it's learning the right thing. This is done by comparing the model's
# predictions on examples it hasn't seen during training to answers we already
# know. So in addition to the training data, you also need evaluation data,
# also called development data.

# The evaluation data is used to calculate how accurate your model is.
# For example, an accuracy score of 90% means that the model predicted 90%
# of the evaluation examples correctly.

# This also means that the evaluation data needs to be representative of the
# data your model will see at runtime. Otherwise, the accuracy score will be
# meaningless, because it won't tell you how good your model really is.


# spaCy can be updated from data in the same format it creates: Doc objects.
# You already learned all about creating Doc and Span objects in chapter 2.

# In this example, we're creating two Doc objects for our corpus: one that
# contains an entity and another one that doesn't contain any entities.
# To set the entities on the Doc, we can add a Span to the doc.ents.

# Of course, you'll need a lot more examples to effectively train your model to
# generalize and predict similar entities in context. Depending on the task,
# you usually want at least a few hundred to a few thousand representative
# examples.


# Create a Doc with entity spans
doc1 = nlp("iPhone X is coming")
doc1.ents = [Span(doc1, 0, 2, label="GADGET")]
# Create another doc without entity spans
doc2 = nlp("I need a new phone! Any tips?")

docs = [doc1, doc2]  # and so on...

# As I mentioned earlier, we don't just need data to train the model. We also
# want to evaluate its accuracy on examples it hasn't seen during training.
# This is usually done by shuffling and splitting your data in two: one portion
# for training and one for evaluation. Here, we're using a simple 50/50 split.

# split data into two portions:
#   training data: used to update the model
#    development data: used to evaluate the model

random.shuffle(docs)
train_docs = docs[:(len(docs)//2)]
dev_docs = docs[(len(docs)//2):]

# You typically want to store your training and development data as files on
# disk so you can load them into spaCy's training process.

# The DocBin is a container for efficiently storing and serializing Doc objects
# You can instantiate it with a list of Doc objects and call its to_disk method
# to save it to a binary file. We typically use the file extension .spacy for
# these files.

# Compared to other binary serialization protocols like pickle, the DocBin is
# faster and produces smaller file sizes because it only stores the shared
# vocabulary once. You can read more about how it works in the documentation.

# Create and save a collection of training docs
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Create and save a collection of evaluation docs
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")
