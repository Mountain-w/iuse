from recyclebin.models import Garbage
from datetime import datetime, timedelta
from iuse.settings import REST_TIME


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
        minute = garbage.created_at.minute
        now = datetime.now().minute
        return REST_TIME - (now - minute)
