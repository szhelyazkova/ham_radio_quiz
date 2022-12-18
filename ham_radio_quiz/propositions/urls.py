from django.urls import path

from ham_radio_quiz.propositions.views import AddQuestionView, edit_question_view, ShowMyQuestionsView, \
    details_question_view, delete_question_view

urlpatterns = (
    path('add/<int:pk>/', AddQuestionView.as_view(), name='question add'),
    path('edit/<int:q_id>/', edit_question_view, name='question edit'),
    path('show/', ShowMyQuestionsView.as_view(), name='questions show'),
    path('details/<int:q_id>/', details_question_view, name='questions details'),
    path('delete/<int:q_id>/', delete_question_view, name='question delete'),
)
