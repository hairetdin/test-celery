# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

import json
from django.core import serializers

from .models import Val
from .tasks import chain_calc


def calculate(request, pk=None):
    #import ipdb; ipdb.set_trace()
    chain = chain_calc(pk)

    messages.success(request, 'Result is calculating! Wait a moment and refresh this page. chain={}'.format(chain))
    return HttpResponseRedirect(reverse_lazy('institute:val-list'))


class ValList(ListView):
    model = Val


class ValDetail(DetailView):
    queryset = Val.objects.all()


class ValCreate(CreateView):
    model = Val
    fields = ['first','second']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse_lazy('institute:val-list'))


class ValUpdate(UpdateView):
    model = Val
    fields = ['first','second']

class ValDelete(DeleteView):
    model = Val
    success_url = reverse_lazy('institute:val-list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse_lazy('institute:val-list'))
        else:
            return super(ValDelete, self).post(request, *args, **kwargs)
