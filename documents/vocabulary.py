from documents.base_models import AuditEntity
from constants.enums.languages import Language
from constants.enums.word_form import WordForm
from documents.typing import Typing


class Vocabulary(AuditEntity):
    def __init__(self, kwargs={}):
        self.word = kwargs.pop('word', '').lower()
        self.translations = {kwargs.pop('translations', '')}
        self.topics = {kwargs.pop('topics', '')}
        self.typing = kwargs.pop('typing', Typing())
        self.phonetics = {kwargs.pop('phonetics', None)}
        self.meanings = {kwargs.pop('meanings', None)}

        super(Vocabulary, self).__init__(kwargs)
