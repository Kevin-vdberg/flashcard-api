from Word import Word
from ..types import Cases,Genders,Numbers,WordTypes
import json


class Modifier(Word):
    def __init__(
            self,
            lemma: str,
            meaning: str = "",
            ipa: str = "",
            sound: str = "",
            gender:Genders=Genders.UNKNOWN,
            number:Numbers=Numbers.UNKNOWN,
            case:Cases=Cases.UNKNOWN,
            is_variation: bool = False):
        super().__init__(lemma, WordTypes.MODIFIER,meaning=meaning,ipa=ipa,sound=sound, is_variation=is_variation)

        self.gender = gender
        self.number = number
        self.case = case

    def get_as_dictionary(self):
        word_as_dictionary = super().get_as_dictionary()
        modifier_as_dictionary = {
            "number": self.number.value,
            "gender": self.gender.value,
            "case": self.case.value,
        }
        return word_as_dictionary | modifier_as_dictionary

    def get_as_json(self):
        object_as_dictionary = self.get_as_dictionary()
        json_data = json.dumps(object_as_dictionary)
        return json_data