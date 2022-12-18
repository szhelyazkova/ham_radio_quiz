from django.urls import path

from ham_radio_quiz.examination.views import ExamGenerateView, ExamPointsView, ExamSolvingView, ExamResultsView

urlpatterns = (
    path('create/', ExamGenerateView.as_view(), name='create exam'),
    path('solving/', ExamSolvingView.as_view(), name='solve exam'),
    path('points/', ExamPointsView.as_view(), name='points exam'),
    path('results/', ExamResultsView.as_view(), name='result exam'),
)
