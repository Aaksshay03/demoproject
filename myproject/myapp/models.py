from django.db import models

# Create your models here.

class Study(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    sponsor_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name