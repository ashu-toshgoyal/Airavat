import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Hey Aria, can you please set a reminder for my meeting with John at 3 PM tomorrow?")

for ent in doc.ents:
    print(ent.text, ent.label_)  # John (PERSON), 3 PM (TIME), tomorrow (DATE)
