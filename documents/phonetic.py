from documents.base_models import AuditEntity


class Phonetic(AuditEntity):
    def __init__(self, phonetic='', audio=''):
        self.phonetic = phonetic
        self.audio = audio
