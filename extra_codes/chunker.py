import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

sentences = sent_tokenize(result["text"])