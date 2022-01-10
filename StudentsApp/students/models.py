from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False, default='')
    last_name = models.CharField(max_length=50, null=False, default='')
    email = models.EmailField(null=False, default='')
    enrollment = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'Profesor: {self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    age = models.IntegerField()
    enrollment = models.IntegerField(null=False)
    active = models.BooleanField(default=False)
    semester = models.CharField(max_length=50, default="")
    photo = models.ImageField(blank=True, upload_to='media')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Subject(models.Model):
    subject = models.CharField(max_length=100, null=False)
    semester = models.CharField(max_length=50, default="")
    formation = models.CharField(max_length=100, default="")
    students = models.ManyToManyField(Student, related_name='classs')
    techars = models.ManyToManyField(Teacher, related_name='classs')

    def __str__(self):
        return self.subject
