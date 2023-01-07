from django.db import models

# Create your models here.


class Items(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self) -> str:
        return self.name
