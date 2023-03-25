from .models import Project
from django.db import models
from django.dispatch import receiver

@receiver(models.signals.pre_save, sender=Project)
def delete_old_profile_picture(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.profile_picture and old_instance.profile_picture != instance.profile_picture:
                old_instance.profile_picture.delete(save=False)
        except sender.DoesNotExist:
            pass