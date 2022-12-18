from django.contrib import admin
from django.contrib.auth import get_user_model

from ham_radio_quiz.propositions.models import ProposedQuestionModel

UserModel = get_user_model()


@admin.register(ProposedQuestionModel)
class ProposedQuestionAdmin(admin.ModelAdmin):

    list_display = ['id', 'username', 'content', 'is_approved']
    search_fields = ['content']
    list_filter = ['is_approved']
    ordering = ('is_approved', )
    readonly_fields = ['user', 'content']

    @staticmethod
    def username(obj):
        queryset = UserModel.objects.filter(pk=obj.user_id).get()
        username = queryset.username
        return username
