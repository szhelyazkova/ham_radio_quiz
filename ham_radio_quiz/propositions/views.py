from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import mixins as auth_mixins

from ham_radio_quiz.propositions.forms import AddQuestionForm, EditQuestionForm, DeleteQuestionForm
from ham_radio_quiz.propositions.models import ProposedQuestionModel

UserModel = get_user_model()


class ShowMyQuestionsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'propositions/questions-show.html'
    model = ProposedQuestionModel

    def get(self, request, *args, **kwargs):
        user_id = request.user.pk
        questions = ProposedQuestionModel.objects.filter(user_id=user_id).all()

        context = {
            'questions': questions,
        }
        return render(request, self.template_name, context)


class AddQuestionView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'propositions/question-add.html'
    form_class = AddQuestionForm

    def form_valid(self, form):
        user = UserModel.objects.get(pk=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.user_id = user.pk
        self.object.save()
        return redirect('questions show')


@login_required
def edit_question_view(request, q_id):
    question = get_object_or_404(ProposedQuestionModel, pk=q_id)
    if request.method == 'GET':
        form = EditQuestionForm(instance=question)
    else:
        form = EditQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions show')
    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'propositions/question-edit.html', context)


@login_required
def details_question_view(request, q_id):
    question = get_object_or_404(ProposedQuestionModel, pk=q_id)
    context = {
        'question': question,
    }
    return render(request, 'propositions/question-details.html', context)


@login_required
def delete_question_view(request, q_id):
    question = get_object_or_404(ProposedQuestionModel, pk=q_id)
    if request.method == 'POST':
        form = DeleteQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions show')
    else:
        form = DeleteQuestionForm(instance=question)
    context = {
        'form': form,
        'question': question
    }
    return render(request, 'propositions/question-delete.html', context)
