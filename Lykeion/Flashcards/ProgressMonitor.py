from datetime import datetime, timedelta
from Lykeion.Flashcards.RepitionAlgorithm import RepetitionAlgorithm
from Lykeion.Flashcards.types.LearningPhases import LearningPhases


#It is assumed that:
# learning phase is in minutes
# Studying phase is in days
# Complete phase is in months

class ProgressMonitor:

    def __init__(
            self,
            starting_date:datetime,
            last_practice_date:datetime,
            next_practice_date:datetime,
            progress_score:int,
            times_reset:int,
            completed:bool,
            learning_phase: int):

        self.starting_date: datetime = starting_date
        self.last_practice_date: datetime = last_practice_date
        self.next_practice_date: datetime = next_practice_date
        self.practice_needed: bool = next_practice_date <= datetime.today()
        self.progress_score: int = progress_score
        self.times_reset:int = times_reset
        self.completed:bool = completed


        learning_phase = LearningPhases(learning_phase)

        #TODO: Repetition algorithm is determined here when building object. In future this might be dynamic
        self._repetition_algorithm: RepetitionAlgorithm = RepetitionAlgorithm(learning_phase,self.progress_score)

    def update_card(self,correct:bool) -> None:
        today = datetime.today()
        self.last_practice_date = today
        interval_next = self._repetition_algorithm.get_next_interval(correct)
        if not correct:
            self.times_reset = self.times_reset + 1

        #translate intervals to time
        phase = self._repetition_algorithm.get_phase()

        if phase == LearningPhases.Learning:
            time = timedelta(minutes=interval_next)
        elif phase == LearningPhases.Studying:
            time = timedelta(days=interval_next)
        elif phase == LearningPhases.Complete:
            time = timedelta(days=interval_next * 31)
        else:
            raise Exception(f'Learning phase {phase} not recognized')

        self.next_practice_date = today + time
        self.progress_score = self._repetition_algorithm.get_progress()
        self.practice_needed: bool = self.next_practice_date <= datetime.now()

    def get_as_dict(self) -> dict:
        return {
            'starting_date': self.starting_date,
            'last_practice_date': self.last_practice_date,
            'next_practice_date': self.next_practice_date,
            'practice_needed': self.practice_needed,
            'progress_score': self.progress_score,
            'times_reset': self.times_reset,
            'completed': self.completed,
            'learning_phase': self._repetition_algorithm.get_phase().value
        }




