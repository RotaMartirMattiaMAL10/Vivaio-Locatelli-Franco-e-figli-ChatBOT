# OpenAI Agent Configuration

class OpenAIAgent:
    def __init__(self, model='gpt-3.5-turbo', temperature=0.7):
        self.model = model
        self.temperature = temperature

    def generate_response(self, prompt):
        # Code to call the OpenAI API and get a response
        pass

    def set_temperature(self, temp):
        self.temperature = temp

    def set_model(self, model):
        self.model = model
