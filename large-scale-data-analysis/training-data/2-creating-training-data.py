import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span, DocBin

with open("exercises/en/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("en")
matcher = Matcher(nlp.vocab)

# Two tokens whose lowercase forms match "iphone" and "x"
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# Token whose lowercase form matches "iphone" and a digit
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# Add patterns to the matcher and create docs with matched entities
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id)
             for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)

doc_bin = DocBin(docs=docs)
doc_bin.to_disk("./train.spacy")

# Of course, you don't have to write the config files by hand, and in a lot of cases, you won't even need to customize it at all. spaCy can auto-generate a config file for you.

# The quickstart widget in the documentation lets you generate a config interactively by selecting the language and pipeline components you need, as well as optional hardware and optimization settings.

# Alternatively, you can also use spaCy's built-in init config command. It takes the output file as the first argument. We usually call this file config.cfg. The argument --lang defines the language class that should be used for the pipeline, for example, en for English. The --pipeline argument lets you specify one or more comma-separated pipeline components to include. In this example, we're creating a config with one pipeline component, the named entity recognizer.

# $ python -m spacy init config ./config.cfg --lang en --pipeline ner

# To train a pipeline, all you need is the config file and the training and development data. These are the .spacy files you already worked with in the previous exercises.

# The first argument of spacy train is the path to the config file. The --output argument lets you specify a directory for saving the final trained pipeline.

# You can also override different config settings on the command line. In this case, we override paths.train using the path to the train.spacy file and paths.dev using the dev.spacy file.


# all you need is the config.cfg and the training and development data
# config settings can be overwritten on the command line

# $ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy

# train: the command to run
# config.cfg: the path to the config file
# --output: the path to the output directory to save the trained pipeline
# --paths.train: override with path to the training data
# --paths.dev: override with path to the evaluation data


# ------------------------------------
