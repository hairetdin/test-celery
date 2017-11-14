# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Val


class ValList(ListView):
    model = Val


class ValDetail(DetailView):
    queryset = Val.objects.all()


class ValCreate(CreateView):
    model = Val
    fields = ['first','second']

class ValUpdate(UpdateView):
    model = Val
    fields = ['first','second']

class ValDelete(DeleteView):
    model = Val
    success_url = reverse_lazy('institute:val-list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect('/')
        else:
            return super(ValDelete, self).post(request, *args, **kwargs)
