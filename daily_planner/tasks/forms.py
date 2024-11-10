from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']  # Добавляем поле due_date
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),  # Используем виджет типа "date"
        }