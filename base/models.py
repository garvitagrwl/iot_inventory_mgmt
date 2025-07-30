from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# class Topic(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Room(models.Model):
#     host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) 
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    
# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE)
#     room = models.ForeignKey(Room, on_delete=CASCADE)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body[0:50]

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

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date_of_purchase = models.DateField()  # Optional: remove auto_now_add if you want to enter manually

    @property
    def status(self):
        return "Empty" if self.quantity == 0 else "Present"

    def __str__(self):
        return f"{self.name} ({self.category})"

class IssueRecord(models.Model):
    student_name = models.CharField(max_length=100)  #  ForeignKey to a User model
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)  # can be updated later

    @property
    def status(self):
        if self.return_date:
            return f"Returned on {self.return_date.strftime('%Y-%m-%d')}"
        return "Not Returned"

    def __str__(self):
        return f"{self.component.name} issued to {self.student_name}"



     