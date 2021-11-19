from documents.base_models import AuditEntity
from constants.enums.type_of_word import TypeOfWord
from constants.enums.languages import Language
from goslate import Goslate as gs


class Translation(AuditEntity):

    def __init__(self, kwargs={}):
        self.typeofword = kwargs.pop('typeofword', None)
        self.stem = kwargs.pop('stem', self.word)
        self.photos = {kwargs.pop('photos', '')}
        super(Translation, self).__init__(kwargs)

