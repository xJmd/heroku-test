import spacy

nlp = spacy.load("en_core_web_sm")

class Formater():
    def __init__(self, transcript):
        self.transcript = transcript
    def update(self):
        doc = nlp(self.transcript)

        formatted_text = ""
        sentence_count = 0
        for sentence in doc.sents:

            capitalized_sentence = sentence.text.capitalize()
            
            if not capitalized_sentence.endswith("."):
                capitalized_sentence += "."
            # add the formatted sentence to the final text
            formatted_text += capitalized_sentence + " "
            sentence_count += 1
            # paragraph braeak after every 4 sentences
            if sentence_count % 4 == 0:
                formatted_text += "\n\n"

        return formatted_text.strip() #remove white spaces