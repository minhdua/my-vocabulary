from documents.base_models import AuditEntity


class Topic(AuditEntity):

    def __init__(self, kwargs={}):
        self.unit_code = kwargs.pop('unit_code', None)
        self.unit_name = kwargs.pop('unit_name', None)
        self.import_path = kwargs.pop('import_path', [])
        super(Topic, self).__init__(kwargs)

