from django.db import models


class Exam(models.Model):
    """Exam model representing a quiz examination session."""
    title = models.CharField(
        max_length=200,
        help_text="Short title identifying the exam"
    )
    description = models.TextField(
        help_text="Detailed description of the exam content and scope"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Automatic timestamp when the exam record is created"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

    def __str__(self):
        return self.title


class Question(models.Model):
    """Question model representing a single question within an exam."""
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    text = models.TextField(
        help_text="The question prompt or statement presented to the student"
    )
    score = models.IntegerField(
        default=1,
        help_text="Points awarded for answering this question correctly"
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return f"Q{self.id}: {self.text[:50]}..."


class Choice(models.Model):
    """Choice model representing an answer option for a question."""
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
    )
    text = models.CharField(
        max_length=500,
        help_text="The text content of this answer option"
    )
    is_correct = models.BooleanField(
        default=False,
        help_text="Whether this option is the correct answer"
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        correct_tag = " [CORRECT]" if self.is_correct else ""
        return f"Choice {self.id}: {self.text[:40]}...{correct_tag}"
