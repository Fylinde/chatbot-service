# vendor_bot.py
from app.nlp_engine import nlp_engine

class VendorSupportBot:
    def __init__(self):
        self.engine = nlp_engine

    def handle_query(self, user_input):
        response = self.engine.process_input(user_input)
        return response

vendor_bot = VendorSupportBot()
