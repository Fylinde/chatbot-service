from transformers import pipeline

class NLPEngine:
    def __init__(self):
        # Use text-generation or text2text-generation based on the use case
        self.model = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

    def process_input(self, text):
        return self.model(text)

nlp_engine = NLPEngine()
