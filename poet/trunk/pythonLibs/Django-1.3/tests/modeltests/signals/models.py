"""
Testing signals before/after saving and deleting.
"""

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s %s" % (self.make, self.model)
