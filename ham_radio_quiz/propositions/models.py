from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ProposedQuestionModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    content = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    is_approved = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.content)
