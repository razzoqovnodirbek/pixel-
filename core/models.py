from django.db import models

class Leader(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Jamoa yetakchisi")
    bio = models.TextField()
    photo = models.ImageField(upload_to='leaders/')  # rasm joylashadigan papka

    def __str__(self):
        return self.name
