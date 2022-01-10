# Generated by Django 3.2 on 2022-01-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20220110_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(related_name='classs', to='students.Student'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='techars',
            field=models.ManyToManyField(related_name='classs', to='students.Teacher'),
        ),
    ]
