"""
19. OR lookups

To perform an OR lookup, or a lookup that combines ANDs and ORs, combine
``QuerySet`` objects using ``&`` and ``|`` operators.

Alternatively, use positional arguments, and pass one or more expressions of
clauses using the variable ``django.db.models.Q`` (or any object with an
``add_to_query`` method).
"""

from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    class Meta:
       ordering = ('pub_date',)

    def __unicode__(self):
        return self.headline
