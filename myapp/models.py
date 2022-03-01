from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date')
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.date = timezone.now()
    def __str__(self):
        return self.text
    def publish(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)