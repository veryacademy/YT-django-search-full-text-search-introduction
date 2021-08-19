from django.db import models
from django.utils.translation import gettext as _


class Book(models.Model):

  title = models.CharField(_("title"), max_length=1000, null=False, db_index=True)
  authors = models.CharField(_("authors"), max_length=1000)
