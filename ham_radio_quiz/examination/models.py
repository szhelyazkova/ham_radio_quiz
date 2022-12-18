from django.contrib.auth import get_user_model
from django.db import models

from ham_radio_quiz.accounts.models import AppUser
from ham_radio_quiz.quiz.models import Question, Answer

UserModel = get_user_model()


class ExamModel(models.Model):
    user_test = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
    )
    user_test_question_id = models.PositiveIntegerField(
        default=None,
    )
    user_test_answer_id = models.IntegerField(
        default=None,
        blank=True,
        null=True,
    )


class GeneratedQuestionsModel(models.Model):
    user_generated_id = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    questions_list = models.CharField(
        max_length=255,
    )


class ExamResultsModel(models.Model):
    user_exam = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    exam_date = models.DateTimeField(auto_now_add=True)
    exam_is_passed = models.BooleanField()
    points = models.PositiveIntegerField()
