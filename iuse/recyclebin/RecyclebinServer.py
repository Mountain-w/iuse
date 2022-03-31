from recyclebin.models import Garbage
from datetime import datetime, timedelta
from iuse.settings import REST_TIME
from utils.modelshelpers.enums import DeleteStatus
from sources.SourceServer import SourceServer


class RecyclebinServer:

    @classmethod
    def get_query_set(cls, user):
        query_set_ = Garbage.objects.filter(owner=user).all()
        query_set = []
        for query in query_set_:
            if cls.get_rest_minute(query) > 0:
                query_set.append(query)
        return query_set

    @classmethod
    def get_rest_day(cls, garbage):
        pass

    @classmethod
    def get_rest_minute(cls, garbage):
        minute = datetime.now() - garbage.created_at
        return REST_TIME - minute.seconds//60

    @classmethod
    def recover(cls, garbage):
        source = garbage.source
        source.on_delete = DeleteStatus.exists
        source.save()
        garbage.delete()

    @classmethod
    def recycle(cls, garbage):
        source = garbage.source
        SourceServer.delete(source)
        garbage.delete()