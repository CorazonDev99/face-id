from django.db import models

class UserProfile(models.Model):
    user_id = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='photos/')
    encoding = models.BinaryField()

    def __str__(self):
        return f'User {self.user_id}'
