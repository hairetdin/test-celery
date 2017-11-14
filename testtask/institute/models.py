# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Val(models.Model):
    first = models.IntegerField()
    second = models.IntegerField()

    def __str__(self):
        return '{}, {}'.format(self.first, self.second)

    def get_absolute_url(self):
        return reverse('institute:val-update', kwargs={'pk': self.pk})
