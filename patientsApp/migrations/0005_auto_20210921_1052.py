# Generated by Django 3.2.5 on 2021-09-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientsApp', '0004_alter_patients_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hopitaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='patients',
            name='sex',
            field=models.CharField(choices=[('MASCULIN', 'masculin'), ('FEMININ', 'feminin')], default='', max_length=200),
        ),
    ]