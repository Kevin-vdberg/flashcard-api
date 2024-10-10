from Lykeion.Flashcards.Flashcard import Flashcard
from Lykeion.Flashcards.AnswerAnalyser import AnswerAnalyser
from Lykeion.Flashcards.ProgressMonitor import ProgressMonitor
from Lykeion.Flashcards.types.NounFlashcardTypes import NounFlashcardTypes
from datetime import datetime


class NounFlashcard(Flashcard):

    NEW_PROGRESS =  {
        'starting_date': datetime.today(),
        'last_practice_date': datetime.today(),
        'next_practice_date': datetime.today(),
        'progress_score': 0,
        'times_reset': 0,
        'completed': False,
        'learning_phase': 1
    }

    def __init__(self, reference_lemma:str, target_lemma:str, image_source:str, sound_source:str, ipa:str, card_type:int,
                 progress_tracker=None):

        if progress_tracker is None:
            progress_tracker = self.NEW_PROGRESS

        self.reference_lemma = reference_lemma
        self.target_lemma = target_lemma
        self.image_source = image_source
        self.sound_source = sound_source
        self.ipa = ipa
        self.card_type: NounFlashcardTypes = NounFlashcardTypes(card_type)

        question,answer,hint = self._get_type(self.card_type)
        answer_analyser = AnswerAnalyser()

        #create progress monitor from dict
        progress_monitor = ProgressMonitor(
            progress_tracker['starting_date'],
            progress_tracker['last_practice_date'],
            progress_tracker['next_practice_date'],
            progress_tracker['progress_score'],
            progress_tracker['times_reset'],
            progress_tracker['completed'],
            progress_tracker['learning_phase']
            )
        complete = progress_tracker['completed']
        super().__init__(question,answer,hint,complete,answer_analyser,progress_monitor)


    def get_card_type(self):
        return self.card_type

    def get_as_dict(self):
        return {
            'reference_lemma': self.reference_lemma,
            'target_lemma': self.target_lemma,
            'image_source': self.image_source,
            'sound_source': self.sound_source,
            'ipa': self.ipa,
            'card_type': self.card_type.value,
            'progress_tracker': self.progress_tracker.get_as_dict()
        }

    def _get_type(self, card_type: NounFlashcardTypes):

        if card_type == NounFlashcardTypes.ImageToTarget:
            self.card_type = NounFlashcardTypes.ImageToTarget
            question = self.image_source
            answer = self.target_lemma
            hint = self.reference_lemma

        elif card_type == NounFlashcardTypes.ReferenceToTarget:
            self.card_type = NounFlashcardTypes.ReferenceToTarget
            question = self.reference_lemma
            answer = self.target_lemma
            hint = self.ipa

        elif card_type == NounFlashcardTypes.TargetToReference:
            self.card_type = NounFlashcardTypes.TargetToReference
            question= self.target_lemma
            answer = self.reference_lemma
            hint = self.ipa

        elif card_type == NounFlashcardTypes.SoundToTarget:
            self.card_type = NounFlashcardTypes.SoundToTarget
            question = self.sound_source
            answer = self.target_lemma
            hint= self.ipa

        elif card_type == NounFlashcardTypes.SoundToReference:
            self.card_type = NounFlashcardTypes.SoundToReference
            question = self.sound_source
            answer = self.reference_lemma
            hint = self.ipa

        else:
            raise Exception(f'{card_type} is not a valid card type')

        return question, answer, hint

    def _set_type(self, card_type: NounFlashcardTypes):
        self.question, self.answer, self.hint = self._get_type(card_type)
