import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iuse.settings')

app = Celery('iuse')

app.config_from_object('django.conf:settings', namespace='CELERY')
from datetime import datetime, timedelta
from celery.schedules import crontab
app.autodiscover_tasks(['recyclebin.Timed_recycling.timed_recycling'])
app.conf.update(
    CELERYBEAT_SCHEDULE={
        'del_test': {
            'task': 'recyclebin.Timed_recycling.timed_recycling',
            'schedule': timedelta(seconds=10),
            'args': (),
        }
    }
)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
