from django.contrib import admin
from django import forms

from ham_radio_quiz.quiz.models import Question, Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    @staticmethod
    def question(obj):
        queryset = Question.objects.filter(pk=obj.question_id_id).get()
        question_content = queryset.content
        return question_content

    list_display = ['id', 'question', 'content', 'is_correct']
    search_fields = ['content']
    list_filter = ['is_correct']
    ordering_field = ('-question_id_id',)


class AnswerInlineFormset(forms.models.BaseInlineFormSet):
    fields = ('is_correct',)

    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data:
                is_correct = form.cleaned_data['is_correct']
                if is_correct:
                    count += 1
        if count != 1:
            raise forms.ValidationError('You must have one correct answer!')


class AnswerInline(admin.TabularInline):
    model = Answer
    formset = AnswerInlineFormset
    max_num = 4
    min_num = 2


@admin.register(Question)
class QuizAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]
    list_display = ['id', 'content', 'category', 'amateur_class']
    search_fields = ['category', 'content', 'amateur_class']
    list_filter = ['category', 'amateur_class']
    ordering = ('amateur_class', )
