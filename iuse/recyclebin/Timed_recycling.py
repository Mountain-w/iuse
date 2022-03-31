from celery import shared_task
from recyclebin.RecyclebinServer import RecyclebinServer
from recyclebin.models import Garbage


@shared_task
def timed_recycling():
    query_set = Garbage.objects.all()
    for garbage in query_set:
        if RecyclebinServer.get_rest_minute(garbage) <= 0:
            RecyclebinServer.recycle(garbage)
