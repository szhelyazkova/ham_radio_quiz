from django.urls import path
from ham_radio_quiz.quiz.views import IndexView, RandomQuestionView, ShowQuestionsByCategoryView, ShowAnswersView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('random/', RandomQuestionView.as_view(), name='show random question'),
    path('category/<str:category>/', ShowQuestionsByCategoryView.as_view(), name='questions by category'),
    path('answers/<int:question_pk>', ShowAnswersView.as_view(), name='show answers'),
)
