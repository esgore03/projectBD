from django.forms import ModelForm
from .models import Course
from django import forms
from django.contrib.auth.models import User

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_schedule']
        labels = {
            'course_name': 'Nombre del curso',
            'course_schedule': 'Descripcion del Horario del Curso',
        }
