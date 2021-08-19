from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.postgres.indexes import GinIndex

class Book(models.Model):

  title = models.CharField(_("title"), max_length=1000, null=False, db_index=True)
  authors = models.CharField(_("authors"), max_length=1000)

  class Meta:
      indexes = [  
          GinIndex(name='NewGinIndex', fields=['title'], opclasses=['gin_trgm_ops']),
      ]