from django.db import models

# Create your models here.
class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tagi = models.CharField(max_length=20)

    def __str__(self):
        return self.title
