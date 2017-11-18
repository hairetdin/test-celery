from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testtask.settings')

app = Celery('testtask')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_routes = {
    'institute.tasks.import_value': {'queue': 'import_value'},
    'institute.tasks.calc_value': {'queue': 'calc_value'},
    'institute.tasks.save_value': {'queue': 'save_value'},
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
