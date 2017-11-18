import celery
from celery import shared_task, chain
import sys
import json
from django.core import serializers
from .models import Val


class TaskTracker(celery.Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        val = Val.objects.get(pk=kwargs['pk'])
        if not val.exception:
            val.exception = True
            val.save()
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        val = Val.objects.get(pk=kwargs['pk'])
        val.exception = False
        val.save()
        print ('after_return status: {}; {}; {}'.format(status, args, kwargs))


def chain_calc(pk):
    chain = import_value.s(pk=pk) | calc_value.s(pk=pk) | save_value.s(pk=pk)
    res = chain()
    return res


@shared_task(base=TaskTracker)
def import_value(pk=None):
    data = None
    object_pk = int(pk)
    if pk:
        data = serializers.serialize('json', Val.objects.filter(pk=object_pk))
    return data

@shared_task(base=TaskTracker)
def calc_value(data, pk=None):
    result = None
    if data:
        d = json.loads(data)
        result = d[0]['fields']['first'] + d[0]['fields']['second']
        d[0]['fields']['result'] = result
    return d

@shared_task(base=TaskTracker)
def save_value(data, pk=None):
    if data:
        for deserialized_object in serializers.deserialize("json", json.dumps(data)):
            deserialized_object.save()
    return 'result = {}'.format(deserialized_object.object.result)
