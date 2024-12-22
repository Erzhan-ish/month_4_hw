from django.db import models

class KinoogoModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField()
    watch_online = models.URLField()

    def __str__(self):
        return self.title