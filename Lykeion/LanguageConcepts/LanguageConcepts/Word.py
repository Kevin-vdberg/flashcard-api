from ..types import WordTypes

class Word:
    def __init__(
            self,
            lemma: str,
            word_type: WordTypes,
            meaning: str = "",
            ipa: str = "",
            sound: str = "",
            is_variation: bool = False):

        self.lemma = lemma
        self.word_type = word_type
        self.meaning = meaning
        self.ipa = ipa
        self.sound = sound
        self.variations = {} if not is_variation else None

    def add_variation(self, variation):
        if self.variations is None:
            raise Exception (f'"{self.lemma}" is already a variation and cannot have variations, please add the variation to the higher level, or add is_variation=True')
        if variation.word_type != self.word_type:
            raise Exception(f'The variation type {variation.word_type} for the variation {variation.lemma} does not match the word type {self.word_type} of the word {self.lemma}')
        key = variation.lemma
        self.variations[key] = variation

    def get_variations_as_list(self):
        if self.variations is None:
            return []
        return list(self.variations.values())

    def get_as_dictionary(self):
        variation_dictionary = {key: value.get_as_dictionary() for key, value in self.variations.items()} if self.variations is not None else None
        object_as_dictionary = {
            "lemma": self.lemma,
            "meaning": self.meaning,
            "ipa": self.ipa,
            "sound":self.sound,
            "type": self.word_type.value,
            "variations": variation_dictionary
        }
        return object_as_dictionary
