from datetime import datetime
import uuid


class BaseEntity(object):
    def __init__(self, kwargs={}):
        self.id = kwargs.pop('id', str(uuid.uuid4()))
        self.deleted = kwargs.pop('deleted', False)


class AuditEntity(BaseEntity):

    def __init__(self, kwargs={}):
        self.created_date = kwargs.pop('created_date', datetime.now())
        self.updated_date = kwargs.pop('updated_date', datetime.now())
        super(AuditEntity, self).__init__(kwargs)
