from django.db import models

class Incidents(models.Model):
    nameOfIncident = models.TextField(null = False, blank = False)
    Description = models.TextField(null = False, blank = False)
    Source = models.TextField(null = False, blank = False)
    Attack = models.TextField(null=False, blank=False)
    Status = models.TextField(null=False, blank=False)
    Date = models.DateField(auto_now_add=True)
    Author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )