from django.db import models

class Attacks(models.Model):
    nameOfAttack = models.TextField(null = False, blank = False)
    Description = models.TextField(null = False, blank = False)
    ShortDescription = models.TextField(null = False, blank = False)
    Date = models.DateField(auto_now_add=True)
    Author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )