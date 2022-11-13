from django.db import models

# Create your models here.

class Chat(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=150, default='', blank=False)
    time_sent = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username