from celery import shared_task, chain
import sys
import json
from django.core import serializers
from .models import Val


def chain_calc(pk=None):
    chain = import_value.s(pk) | calc_value.s() | save_value.s()
    chain()



@shared_task
def import_value(pk=None):
    data = None
    object_pk = int(pk)
    if pk:
        data = serializers.serialize('json', Val.objects.filter(pk=object_pk))
    return data

@shared_task
def calc_value(data=None):
    result = None
    if data:
        d = json.loads(data)
        result = d[0]['fields']['first'] + d[0]['fields']['second']
        d[0]['fields']['result'] = result
    return d

@shared_task
def save_value(data=None):
    if data:
        for deserialized_object in serializers.deserialize("json", json.dumps(data)):
            obj = deserialized_object.save()
    return 'obj: {}'.format(obj)
