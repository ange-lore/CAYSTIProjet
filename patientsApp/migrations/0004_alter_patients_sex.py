# Generated by Django 3.2.5 on 2021-08-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientsApp', '0003_alter_patients_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='sex',
            field=models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], default='', max_length=200),
        ),
    ]
