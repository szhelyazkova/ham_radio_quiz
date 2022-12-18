from enum import Enum
from django.db import models
from ham_radio_quiz.core.model_mixins import ChoicesEnumMixin


class Category(ChoicesEnumMixin, Enum):
    technical = 'Technical'
    rules = 'Rules'
    regulations = 'Regulations'


class AmateurSkills(ChoicesEnumMixin, Enum):
    base = '2'
    advanced = '1'


class Question(models.Model):
    category = models.CharField(
        max_length=Category.max_len(),
        choices=Category.choices(),
        null=False,
        blank=False,
    )
    amateur_class = models.CharField(
        max_length=AmateurSkills.max_len(),
        choices=AmateurSkills.choices(),
        null=False,
        blank=False,
    )
    content = models.TextField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return str(self.content)


class Answer(models.Model):
    content = models.TextField(
        null=False,
        blank=False,
    )
    is_correct = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    question_id = models.ForeignKey(
        Question,
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
    )

    def __str__(self):
        return str(self.content)

