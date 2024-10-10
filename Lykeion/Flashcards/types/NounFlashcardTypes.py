from enum import Enum


class NounFlashcardTypes(Enum):
    Unknown = -1
    ImageToTarget = 0
    ReferenceToTarget = 1
    TargetToReference = 2
    SoundToTarget = 3
    SoundToReference = 4
