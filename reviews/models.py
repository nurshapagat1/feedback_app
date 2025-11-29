from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    username = models.CharField(max_length=100)
    reviewtext = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    upload_photo = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.rating}/5)"
