from django.urls import path, include

from ham_radio_quiz.accounts.views import SignUpView, SignInView, SignOutView, UserEditView, UserDetailsView, \
    UserDeleteView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='user create'),
    path('login/', SignInView.as_view(), name='user login'),
    path('logout/', SignOutView.as_view(), name='user logout'),
    path('profile/<int:pk>/', include([
        path('edit/', UserEditView.as_view(), name='user edit'),
        path('details/', UserDetailsView.as_view(), name='user details'),
        path('delete/', UserDeleteView.as_view(), name='user delete'),
    ]), ),
)

