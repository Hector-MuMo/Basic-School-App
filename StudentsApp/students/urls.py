from django.urls import path
from . import views

app_name = 'estudiante'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('students/', views.StudentsListView.as_view(), name='students_list'),
    path('students/<int:pk>/', views.StudentsDetailView.as_view(), name='student_detail'),
    path('classes/', views.ClassListView.as_view(), name='classes_list'),
    path('classes/<int:pk>/', views.ClassDetailView.as_view(), name='class_detail')
]
