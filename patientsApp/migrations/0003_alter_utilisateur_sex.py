# Generated by Django 3.2.5 on 2021-09-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientsApp', '0002_alter_utilisateur_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='sex',
            field=models.CharField(choices=[('MASCULIN', 'masculin'), ('FEMININ', 'feminin')], default='', max_length=200),
        ),
    ]
