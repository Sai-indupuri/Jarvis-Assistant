import spacy

nlp = spacy.load("en_core_web_sm")

def process_command(command):
    doc = nlp(command)
    return doc
