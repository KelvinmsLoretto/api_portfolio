# Generated by Django 4.1.7 on 2023-03-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='email@teste.com.br', max_length=254, verbose_name='email'),
            preserve_default=False,
        ),
    ]