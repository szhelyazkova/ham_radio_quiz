from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = ['id', 'username', 'email', 'last_login', 'is_staff']
    search_fields = ['username', 'email']
    list_filter = ['is_staff']
    readonly_fields = [
        'date_joined',
        'last_login',
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(is_superuser=False)
