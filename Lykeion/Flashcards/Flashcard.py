from Lykeion.Flashcards.AnswerAnalyser import AnswerAnalyser
from Lykeion.Flashcards.ProgressMonitor import ProgressMonitor


class Flashcard:

    def __init__(self, question: str, answer:str, hint:str, complete:bool, answer_analyser:AnswerAnalyser, progress_tracker:ProgressMonitor):
        self._question: str = question
        self._answer: str = answer
        self._hint:str  = hint
        self._complete:bool = complete
        self._answer_analyser: AnswerAnalyser = answer_analyser
        self.progress_tracker: ProgressMonitor = progress_tracker

    def get_question(self):
        return self._question

    def get_answer(self):
        return self._answer

    def get_hint(self):
        return self._hint

    def check_answer(self,given_answer) -> bool:
        correct = self._answer_analyser.check_answer(self._answer,given_answer)
        self.progress_tracker.update_card(correct)
        return correct