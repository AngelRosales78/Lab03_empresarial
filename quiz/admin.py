from django.contrib import admin
from .models import Exam, Question, Choice
from django.contrib.admin import TabularInline


class ChoiceInline(TabularInline):
    """Inline display of Choices under each Question in admin."""
    model = Choice
    extra = 4
    fields = ('text', 'is_correct')
    can_delete = False


class QuestionInline(TabularInline):
    """Inline display of Questions under each Exam in admin."""
    model = Question
    extra = 2
    fields = ('text',)
    readonly_fields = ('text',)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    """Admin configuration for the Exam model."""
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Admin configuration for the Question model."""
    list_display = ('id', 'exam', 'text_preview')
    list_filter = ('exam',)
    search_fields = ('text',)
    readonly_fields = ('exam', 'text')

    def text_preview(self, obj):
        """Show a preview of the question text in the admin list."""
        return obj.text[:60] + '...' if len(obj.text) > 60 else obj.text
    text_preview.short_description = 'Question Text'


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """Admin configuration for the Choice model."""
    list_display = ('id', 'question', 'text_preview', 'is_correct')
    list_filter = ('is_correct', 'question__exam')
    search_fields = ('text',)
    readonly_fields = ('question', 'text', 'is_correct')

    def text_preview(self, obj):
        """Show a preview of the choice text in the admin list."""
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Choice Text'
