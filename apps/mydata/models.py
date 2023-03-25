from django.db import models
from projects.models import Tecnology

# Create your models here.
class MyData(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='nome', blank=False, null=False)
    last_name = models.CharField(max_length=150, verbose_name='sobrenome', blank=False, null=False)
    ddd = models.IntegerField(verbose_name='ddd', null=False, blank=False)
    telephone = models.IntegerField(verbose_name='telefone', null=False, blank=False)
    email = models.EmailField(verbose_name='email', null=False, blank=False)
    about = models.TextField(verbose_name='sobre mim', null=False, blank=False)
    about_dev = models.TextField(verbose_name='sobre carreira', null=False, blank=False)
    stacks = models.ManyToManyField(Tecnology)

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self) -> str:
        return self.get_fullname()

