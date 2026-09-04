from django import forms
from .models import Exam, Question, Choice
from django.forms import modelformset_factory


class ExamForm(forms.ModelForm):
    """Form for creating and editing Exam instances."""
    class Meta:
        model = Exam
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter exam title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter exam description'}),
        }


class QuestionForm(forms.ModelForm):
    """Form for creating and editing Question instances."""
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter the question text'}),
        }


ChoiceFormSet = modelformset_factory(
    Choice,
    fields=['text', 'is_correct'],
    extra=4,
    max_num=4,
    validate_max=True,
    widgets={
        'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter option text'}),
        'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
)
