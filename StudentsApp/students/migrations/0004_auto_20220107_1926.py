# Generated by Django 3.2 on 2022-01-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_subject_techars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='techars',
        ),
        migrations.AddField(
            model_name='subject',
            name='techars',
            field=models.ManyToManyField(to='students.Teacher'),
        ),
    ]
