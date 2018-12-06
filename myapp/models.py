from django.db import models
import json
from datetime import date
from dateutil.relativedelta import relativedelta


class Politoon(models.Model):
    """Model representing a Politoons."""
    name = models.CharField(max_length=200)
    dob = models.DateField(max_length=8)

    def get_age(self):
        today = date.today()
        delta = relativedelta(today, self.dob)
        return str(delta.years)

    area = models.CharField(max_length=200, help_text='Area of influence', default=' ')
    party = models.CharField(max_length=200, help_text='Political party')
    majorRole = models.CharField(max_length=200, help_text='major role today')
    date = models.DateTimeField()
    placeOfBirth = models.CharField(max_length=80, help_text='Enter the place of birth', default=' ')
    imageUrl = models.URLField()

    class Meta:
        ordering = ['dob']

    # def set_foo(self, x):
    #     self.highlights = json.dumps(x)
    #
    # def get_foo(self):
    #     return json.loads(self.highlights)

    def __str__(self):
        return str(self.name)
