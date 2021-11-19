from enum import Enum


class Collection(Enum):
    VOCABULARY = 'vocabulary'
    SENTENCE = 'sentence'
    PARAGRAPH = 'paragraph'
    TOPIC = 'topic'
    TRANSLATION = 'translation'

    def __str__(self):
        return
