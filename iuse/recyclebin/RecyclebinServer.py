from recyclebin.models import Garbage
from datetime import datetime, timedelta
from iuse.settings import REST_TIME


class RecyclebinServer:

    @classmethod
    def get_rest_day(cls, garbage):
        pass

    @classmethod
    def get_rest_minute(cls, garbage):
        minute = garbage.created_at.minute
        now = datetime.now().minute
        return REST_TIME - (now - minute)
