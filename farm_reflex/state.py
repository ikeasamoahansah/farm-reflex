import reflex as rx

class State(rx.State):

    question:str

    chat_history: list[tuple[str, str]]

    def answer(self):
        answer = "I don't know"
        self.chat_history.append((self.question, answer))
        self.question = ""