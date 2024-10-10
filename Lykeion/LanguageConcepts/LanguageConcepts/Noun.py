from Word import Word
from ..types import Genders, Numbers, Cases, WordTypes

import json

class Noun(Word):

    def __init__(
            self,
            lemma: str,
            meaning: str = "",
            ipa: str = "",
            sound: str = "",
            gender:Genders = Genders.UNKNOWN,
            number:Numbers = Numbers.UNKNOWN,
            case:Cases = Cases.UNKNOWN,
            unique: bool = False,
            diminutive: bool = False,
            is_variation: bool = False):

        super().__init__(lemma,WordTypes.NOUN, meaning=meaning,ipa=ipa,sound=sound, is_variation=is_variation)

        self.gender = gender
        self.number = number
        self.case = case
        self.unique = unique
        self.diminutive = diminutive

    def get_as_dictionary(self):
        word_as_dictionary = super().get_as_dictionary()
        noun_as_dictionary = {
            "number":self.number.value,
            "gender":self.gender.value,
            "case":self.case.value,
            "unique":self.unique,
            "diminutive":self.diminutive
        }

        return word_as_dictionary | noun_as_dictionary

    def get_as_json(self):
        object_as_dictionary = self.get_as_dictionary()
        json_data = json.dumps(object_as_dictionary)

        return json_data

