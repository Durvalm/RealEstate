from django.db import models
from houses.models import Property


class Page(models.Model):
    # not needed
    objects = None
    DoesNotExist = None

    # needed
    page_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.page_id


class Favorite(models.Model):
    # not needed
    DoesNotExist = None
    objects = None

    # needed
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=False)

