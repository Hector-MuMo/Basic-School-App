from django.shortcuts import render
from .models import Student, Subject
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'students/home.html'


class StudentsListView(ListView):
    queryset = Student.objects.all()
    context_object_name = 'students'
    paginate_by = 2
    template_name = 'students/students_list.html'


class StudentsDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'students/student_detail.html'


class ClassListView(ListView):
    queryset = Subject.objects.all()
    context_object_name = 'classes'
    paginate_by = 2
    template_name = 'students/classes_list.html'


class ClassDetailView(DetailView):
    model = Subject
    context_object_name = 'class'
    template_name = 'students/class_detail.html'
