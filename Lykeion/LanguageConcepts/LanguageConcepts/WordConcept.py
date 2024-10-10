from Modifier import Modifier
from Noun import Noun
from Verb import Verb
from ..types import WordTypes


class WordConcept:
    def __init__(self, word_type, lemma):
        self.word_type = word_type

        if self.word_type == WordTypes.NOUN:
            self.word = Noun(lemma)
        elif self.word_type == WordTypes.VERB:
            self.word = Verb(lemma)
        elif self.word_type == WordTypes.MODIFIER:
            self.word = Modifier(lemma)
        else:
            raise Exception(f'{word_type} is not a valid word type')

    def _create_unique_id(self):
        pass

    def get_image(self):
        pass

    def get_vector(self):
        pass