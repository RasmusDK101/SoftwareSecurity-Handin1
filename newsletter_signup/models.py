
from django.db import models

class NewsletterSignup(models.Model):
    username = models.CharField(max_length = 100)
    firstnames = models.CharField(max_length = 100)
    lastnames = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
            return self.email
