# Generated by Django 4.1.7 on 2023-03-16 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='alumno',
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='materia',
        ),
    ]