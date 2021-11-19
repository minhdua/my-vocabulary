from documents.base_models import AuditEntity


class Typing(AuditEntity):
    def __init__(self, right=0, wrong=0):
        self.right = right
        self.wrong = wrong
