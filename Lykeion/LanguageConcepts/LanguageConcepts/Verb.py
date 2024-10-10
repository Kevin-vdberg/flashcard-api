from Word import Word
from ..types import Aspects,Genders,Moods,Numbers,Persons,Tenses,WordTypes

import json

class Verb(Word):

    def __init__(
            self,
            lemma: str,
            meaning: str = "",
            ipa: str = "",
            sound: str = "",
            mood: Moods = Moods.UNKNOWN,
            tense: Tenses = Tenses.UNKNOWN,
            aspect: Aspects = Aspects.UNKNOWN,
            person: Persons = Persons.UNKNOWN,
            gender: Genders = Genders.UNKNOWN,
            number: Numbers = Numbers.UNKNOWN,
            direct_object: str = None,
            indirect_object: str = None,
            valency: int = -1,
            is_variation=False):

        super().__init__(lemma,WordTypes.VERB,meaning=meaning,ipa=ipa,sound=sound, is_variation=is_variation)

        self.mood = mood
        self.tense = tense
        self.aspect = aspect
        self.person = person
        self.gender = gender
        self.number = number
        self.direct_object = direct_object
        self.indirect_object = indirect_object

        self.valency = valency if not is_variation else None

    def get_as_dictionary(self):
        word_as_dictionary = super().get_as_dictionary()
        verb_as_dictionary = {
            "mood":self.mood.value,
            "tense":self.tense.value,
            "aspect":self.aspect.value,
            "person":self.person.value,
            "gender":self.gender.value,
            "number": self.number.value,
            "direct_object": self.direct_object,
            "indirect_object": self.indirect_object,
            "valency": self.valency
        }
        return word_as_dictionary | verb_as_dictionary

    def get_as_json(self):
        object_as_dictionary = self.get_as_dictionary()
        json_data = json.dumps(object_as_dictionary)
        return json_data

