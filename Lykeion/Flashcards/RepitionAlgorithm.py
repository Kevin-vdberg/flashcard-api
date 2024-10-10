from Lykeion.Flashcards.types.LearningPhases import LearningPhases
from Lykeion.Flashcards.types.IntervalUnits import IntervalUnits

STANDARD_REPETITION_INTERVALS = {
    LearningPhases.Learning.name: (10,20,30),
    LearningPhases.Studying.name: (2,4,8,16,32,64),
    LearningPhases.Complete.name: (1,)}

INTERVAL_UNITS = (IntervalUnits.Minutes, IntervalUnits.Days, IntervalUnits.Months)

class RepetitionAlgorithm:
    def __init__(self, learning_phase,current_progress,repetition_intervals=None):
        self._learning_phase: LearningPhases = learning_phase
        self._current_progress = current_progress
        self._repetition_intervals: dict[str,tuple] = {   phase.name: tuple() for phase in LearningPhases  }

        if repetition_intervals is None:
            self._repetition_intervals = STANDARD_REPETITION_INTERVALS

    def get_next_interval(self, correct: bool) -> int:
        if correct:
            next_interval = self._calculate_next_interval()
        else:
            self.reset_progress()
            next_interval = self.get_current_interval()

        return next_interval

    def get_current_interval(self) -> int:
        try:
            current_interval = self._get_interval_per_stage(self._current_progress,self._learning_phase,self._repetition_intervals)
        except Exception as e:
            raise e
        return current_interval

    def get_progress(self) -> int:
        return self._current_progress

    def reset_progress(self):
        self._current_progress = 0

    def set_intervals(self, phase: LearningPhases, learning_intervals: tuple):

        self._repetition_intervals[phase.name] = learning_intervals

        if self._learning_phase == phase:
            self.reset_progress()

    def get_phase(self) -> LearningPhases:
        return self._learning_phase

    def _calculate_next_interval(self, update:bool=True):
        current_phase = self._learning_phase.value
        current_index = self._current_progress + 1
        current_intervals_length = len(self._repetition_intervals[LearningPhases(current_phase).name])

        if current_index >= current_intervals_length:
            current_phase = current_phase + 1
            current_index = 0

        if current_phase >= len(LearningPhases):
            current_phase = len(LearningPhases)

        phase = LearningPhases(current_phase)

        try:
            new_interval = self._get_interval_per_stage(current_index,phase,self._repetition_intervals)
        except Exception as e:
            raise e

        if update:
            self._learning_phase = phase
            self._current_progress = current_index

        return new_interval

    @staticmethod
    def _get_interval_per_stage(index: int,learning_phase: LearningPhases,repetition_intervals:dict[str,tuple]) -> int:
        intervals = repetition_intervals[learning_phase.name]

        if not learning_phase.name in repetition_intervals.keys():
            raise Exception (f'Learning phase {learning_phase.name} is not in the repetition intervals')
        if index >= len(repetition_intervals[learning_phase.name]):
            raise Exception (f'Index {index} is out of range for the tuple {intervals} with length {len(intervals)}')

        new_interval = intervals[index]
        return new_interval
