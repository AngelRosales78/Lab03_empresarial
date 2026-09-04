from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from .models import Exam, Question, Choice
from .forms import ExamForm, QuestionForm, ChoiceFormSet


def exam_list(request):
    """List all exams ordered by creation date descending."""
    exams = Exam.objects.order_by('-created_at')
    return render(request, 'quiz/exam_list.html', {'exams': exams})


def exam_detail(request, pk):
    """Display a single exam with all its questions and choices."""
    exam = get_object_or_404(Exam, pk=pk)
    questions = exam.questions.prefetch_related('choices').all()
    return render(request, 'quiz/exam_detail.html', {
        'exam': exam,
        'questions': questions,
    })


@transaction.atomic
def add_question(request, pk):
    """Create a new question with its choices for a given exam.

    Validates that exactly one choice is marked as correct.
    """
    exam = get_object_or_404(Exam, pk=pk)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        formset = ChoiceFormSet(request.POST)

        if question_form.is_valid() and formset.is_valid():
            # Validate exactly one correct choice
            correct_choices = [f for f in formset.forms if f.cleaned_data.get('is_correct')]
            if len(correct_choices) != 1:
                question_form.add_error(
                    None,
                    'Exactly one choice must be marked as correct.'
                )
                for form in formset.forms:
                    if form.cleaned_data.get('is_correct') and len(correct_choices) != 1:
                        form.add_error(
                            'is_correct',
                            'Ensure exactly one option is marked correct.'
                        )
            else:
                question = question_form.save(commit=False)
                question.exam = exam
                question.save()

                for form in formset.forms:
                    choice = form.save(commit=False)
                    choice.question = question
                    choice.save()

                return redirect('quiz:exam_detail', pk=exam.pk)
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet(queryset=Choice.objects.none())

    return render(request, 'quiz/add_question.html', {
        'exam': exam,
        'question_form': question_form,
        'formset': formset,
    })
