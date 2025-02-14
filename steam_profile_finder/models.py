from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    class Mode(models.TextChoices):
        DARK = 'Dark'
        LIGHT = 'Light'
        SYSTEM = 'System'

    mode = models.TextField(choices=Mode,
                            default=Mode.SYSTEM)


class HistoryEntry(models.Model):
    viewer = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='%(app_label)s_%(class)s_history')
    viewed_user = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='%(app_label)s_%(class)s_referenced_histories')

    # idk if auto_now works correctly if no changes are made
    # maybe add a count that can be updated, so this field auto updates
    last_viewed = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ('viewer', 'viewed_user')


class Layout(models.Model):
    owner = models.OneToOneField(User,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    data = models.TextField()