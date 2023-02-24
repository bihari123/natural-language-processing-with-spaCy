# Loading a trained pipeline
# output after training is a regular loadable spaCy pipeline
# model-last: last trained pipeline
# model-best: best trained pipeline
# load it with spacy.load
# import spacy
#

import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span, DocBin


nlp = spacy.load("./output/model-best/")
doc = nlp("iPhone 11 vs iPhone 8: What's the difference?")
print(doc.ents)

# Tip: Packaging your pipeline
# ---spacy package: create an installable Python package containing your pipeline
# ---easy to version and deploy

# $ python -m spacy package /path/to/output/model-best ./packages --name my_pipeline --version 1.0.0
# $ cd ./packages/en_my_pipeline-1.0.0
# $ pip install dist/en_my_pipeline-1.0.0.tar.gz

# Load and use the pipeline after installation:

# nlp = spacy.load("en_my_pipeline")
