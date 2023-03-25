from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(verbose_name='nome', max_length=150, null=False, blank=False)
    ddd = models.IntegerField(verbose_name='ddd', null=False, blank=False)
    telephone = models.IntegerField(verbose_name='telefone', null=False, blank=False)
    email = models.EmailField(verbose_name='email', null=False, blank=False)
    subject = models.CharField(verbose_name='assunto', max_length=150, null=False, blank=False)
    message = models.TextField(verbose_name='message', null=False, blank=False)

    def __str__(self) -> str:
        return self.subject