from recyclebin.models import Garbage
from datetime import datetime, timedelta
from iuse.settings import REST_TIME
from utils.modelshelpers.enums import DeleteStatus
from sources.SourceServer import SourceServer


class RecyclebinServer:

    @classmethod
    def get_query_set(cls, user=None):
        query_set = []
        if user is not None:
            query_set_ = Garbage.objects.filter(owner=user).all()
            for query in query_set_:
                if cls.get_rest_minute(query) > 0:
                    query_set.append(query)
        else:
            query_set_ = Garbage.objects.all()
            for query in query_set_:
                if cls.get_rest_minute(query) > 0:
                    query_set.append(query.id)
            query_set = Garbage.objects.filter(id__in=query_set)
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