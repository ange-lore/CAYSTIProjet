# Generated by Django 3.2.5 on 2021-09-29 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientsApp', '0005_auto_20210929_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='user_permissions',
        ),
    ]
