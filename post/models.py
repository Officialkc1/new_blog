from django.db import models
from django.db.models.base import Model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='medial/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:24]