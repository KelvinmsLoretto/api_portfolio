from django.db import models
import os


def project_directory_path(instance, filename):
    project_name = instance.name
    upload_dir = os.path.join('project_images', str(project_name))
    return os.path.join(upload_dir, filename)

# Create your models here.
class Tecnology(models.Model):
    usage = (
        (0, 'back-end'),
        (1, 'front-end'),
        (2, 'ops'),
        (3, 'database'),
        (4, 'lib')
    )

    name = models.CharField(max_length=10, blank=False, null=False, verbose_name='tec name')
    use = models.IntegerField(choices=usage, verbose_name='tecnology usage')
    description = models.TextField(max_length=500, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='repo name')
    tecnologies = models.ManyToManyField(Tecnology)
    description = models.TextField(max_length=500, blank=False, null=False)
    link = models.URLField(verbose_name='link project', blank=True, null=True)
    photo_os = models.ImageField(upload_to=project_directory_path, blank=True, null=True)
    data = models.DateField()
    last_update = models.DateField(auto_now=True)
