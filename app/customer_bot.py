# customer_bot.py
from app.nlp_engine import nlp_engine

class CustomerSupportBot:
    def __init__(self):
        self.engine = nlp_engine

    def handle_query(self, user_input):
        response = self.engine.process_input(user_input)
        return response

customer_bot = CustomerSupportBot()
