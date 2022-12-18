from django.contrib import admin
from django.urls import path, include

from ham_radio_quiz.exception_handler import custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ham_radio_quiz.quiz.urls')),
    path('accounts/', include('ham_radio_quiz.accounts.urls')),
    path('exam/', include('ham_radio_quiz.examination.urls')),
    path('propositions/', include('ham_radio_quiz.propositions.urls')),
]

handler404 = custom_handler404
handler500 = custom_handler500
