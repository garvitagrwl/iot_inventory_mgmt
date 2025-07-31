from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE




from django.db import models
class Component(models.Model):
        CATEGORY_CHOICES = [
            ('Microcontroller', 'Microcontroller/Board'),
            ('Sensor', 'Sensor'),
            ('Actuator', 'Actuator'),
            ('Electronic', 'Electronic Component'),
            ('Display', 'Display'),
            ('Misc', 'Miscellaneous'),
        ]

        name_comp = models.CharField(max_length=100)
        quantity = models.IntegerField()
        category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

        def _str_(self):
            return f"{self.name_comp} ({self.category})"