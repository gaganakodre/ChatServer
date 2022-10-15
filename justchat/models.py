from django.db import models

# Create your models here.
from django.db import models

class Messages(models.Model):
    room_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    message = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["created_at"]

    # def __str__(self):
    #     return self.username
